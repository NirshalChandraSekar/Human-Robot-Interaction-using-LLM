import time
import math
import numpy as np
import pybullet as p
import pybullet_data
from objects_dictionary import objects_in_env

class pybullet():
    def __init__(self):
        # INITIALIZING THE ENVIRONMENT
        # Setting the GUI
        physics_client = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.81)

        # Loading the robot, the gripper, the table, and the pan.
        # plane = p.loadURDF("plane.urdf")
        wall = p.loadURDF(r"URDF Models\wall.urdf",basePosition=[1.0, -0.2, 2.0])
        # wall2 = p.loadURDF(r"URDF Models\wall.urdf",basePosition=[1.0, -8, 2.0],baseOrientation=[0, 0, 0.707106781186548, 0.707106781186547])
        floor = p.loadURDF(r"URDF Models\wall.urdf",basePosition=[1.0, -0.2, 2.0], baseOrientation=[0, 0.707106781186548, 0, 0.707106781186547])
        self.kuka_robot = p.loadURDF("kuka_iiwa\model_vr_limits.urdf", 1.400000, -0.200000, 0.600000, 0.000000, 0.000000, 0.000000, 1.000000)
        self.kuka_gripper = p.loadSDF("gripper\wsg50_one_motor_gripper_new_free_base.sdf")[0]
        self.kuka_end_effector_idx = 6
        table = p.loadURDF(r"table\table.urdf", basePosition=[1.0, -0.2, 0.0], baseOrientation=[0, 0, 0.7071, 0.7071])
        self.bowl = p.loadURDF(r"URDF Models\grey_plate\model.urdf", basePosition=[0.7, -0.2, 0.7], globalScaling=2.5)
        
        # Joining the gripper to the robot
        kuka_cid = p.createConstraint(self.kuka_robot, 6, self.kuka_gripper, 0, p.JOINT_FIXED, [0, 0, 0], [0, 0, 0.05], [0, 0, 0])
        kuka_cid2 = p.createConstraint(self.kuka_gripper, 4, self.kuka_gripper, 6, jointType=p.JOINT_GEAR, jointAxis=[1,1,1], parentFramePosition=[0,0,0], childFramePosition=[0,0,0])
        p.changeConstraint(kuka_cid2, gearRatio=-1, erp=0.5, relativePositionTarget=0, maxForce=100)
        jointPositions = [-0.000000, -0.000000, 0.000000, 1.570793, 0.000000, -1.036725, 0.000001]
        for jointIndex in range(p.getNumJoints(self.kuka_robot)):
            p.resetJointState(self.kuka_robot, jointIndex, jointPositions[jointIndex])
            p.setJointMotorControl2(self.kuka_robot, jointIndex, p.POSITION_CONTROL, jointPositions[jointIndex], 0)
        p.resetBasePositionAndOrientation(self.kuka_gripper, [0.923103, -0.200000, 1.250036], [-0.000000, 0.964531, -0.000002, -0.263970])
        jointPositions = [0.000000, -0.011130, -0.206421, 0.205143, -0.009999, 0.000000, -0.010055, 0.000000]
        for jointIndex in range(p.getNumJoints(self.kuka_gripper)):
            p.resetJointState(self.kuka_gripper, jointIndex, jointPositions[jointIndex])
            p.setJointMotorControl2(self.kuka_gripper, jointIndex, p.POSITION_CONTROL, jointPositions[jointIndex], 0)
        
        # Building the objects
        self.obj_dict = objects_in_env.obj_dict
        for i in self.obj_dict:
            new_id = p.loadURDF(self.obj_dict[i]["path"], basePosition=self.obj_dict[i]["baseposition"], baseOrientation=self.obj_dict[i]["baseorientation"], globalScaling=self.obj_dict[i]["globalscaling"])
            self.obj_dict[i]["object_id_bullet"] = new_id

    def step(self):
        p.stepSimulation()
        time.sleep(1./150)

    def robot_home_pose(self):
        jointPositions = [-0.000000, -0.000000, 0.000000, 1.570793, 0.000000, -1.036725, 0.000001]
        for jointIndex in range(p.getNumJoints(self.kuka_robot)):
            p.setJointMotorControl2(self.kuka_robot, jointIndex, p.POSITION_CONTROL, jointPositions[jointIndex], 0)
        for _ in range(100):
            p.stepSimulation()
            time.sleep(1./250)

        
        # reset gripper
        p.resetBasePositionAndOrientation(self.kuka_gripper, [0.923103, -0.200000, 1.250036], [-0.000000, 0.964531, -0.000002, -0.263970])
        jointPositions = [0.000000, -0.011130, -0.206421, 0.205143, -0.009999, 0.000000, -0.010055, 0.000000]
        for jointIndex in range(p.getNumJoints(self.kuka_gripper)):
            p.setJointMotorControl2(self.kuka_gripper, jointIndex, p.POSITION_CONTROL, jointPositions[jointIndex], 0)
        for _ in range(100):
            p.stepSimulation()
            time.sleep(1./250)
            

    def inverse_kinematics(self, target_pose, target_orientation=[0,math.pi,0]):
        current_pose = list(p.getLinkState(self.kuka_robot,6)[0])
        target_orn = p.getQuaternionFromEuler(target_orientation)
        num_steps = 100

        diff_x = target_pose[0] - current_pose[0]
        diff_y = target_pose[1] - current_pose[1]
        diff_z = target_pose[2] - current_pose[2]

        inc_x = diff_x / num_steps
        inc_y = diff_y / num_steps
        inc_z = diff_z / num_steps

        for i in range(num_steps):
            step_pose = [current_pose[0] + inc_x * i, current_pose[1] + inc_y * i, current_pose[2] + inc_z * i]
            # print(step_pose)
            joint_poses = p.calculateInverseKinematics(self.kuka_robot, 6, step_pose, target_orn)
            for j in range (7):
                p.setJointMotorControl2(bodyIndex=self.kuka_robot, jointIndex=j, controlMode=p.POSITION_CONTROL, targetPosition=joint_poses[j])

            for _ in range(5):
                self.step()
            
    def control_gripper(self, action):
        if(action == "close"):
            p.setJointMotorControl2(self.kuka_gripper, 4, p.POSITION_CONTROL, targetPosition = 0.1, force=50)
            p.setJointMotorControl2(self.kuka_gripper, 6, p.POSITION_CONTROL, targetPosition = 0.1, force=50)
        
        elif(action == "open"):
            p.setJointMotorControl2(self.kuka_gripper, 4, p.POSITION_CONTROL, targetPosition = 0, force=1000)
            p.setJointMotorControl2(self.kuka_gripper, 6, p.POSITION_CONTROL, targetPosition = 0, force=1000)

        else:
            print("invalid action request")
    
    def pick_which_object(self, object_index):
        object_id = self.obj_dict[object_index]["object_id_bullet"]
        target_position, _ = p.getBasePositionAndOrientation(object_id)
        target_position = list(target_position)
        target_position[2] += 0.32

        if(object_index==3):
            target_position[2]+= 0.02
        self.inverse_kinematics(target_position)
        self.control_gripper("close")

        for _ in range(50):
            self.step()

        self.inverse_kinematics([0.7, -0.2, 1.5])
        release_position = [0.7, -0.23, 1.13]
        self.inverse_kinematics(release_position)
        self.control_gripper("open")

        for _ in range(50):
            self.step()
            
        self.robot_home_pose()

    def reset_pose(self):
        for i in self.obj_dict:
            new_object_id = self.obj_dict[i]["object_id_bullet"]
            new_position = self.obj_dict[i]["baseposition"]
            new_orientation = self.obj_dict[i]["baseorientation"]
            p.resetBasePositionAndOrientation(new_object_id, new_position, new_orientation)
        p.resetBasePositionAndOrientation(self.bowl,[0.7, -0.2, 0.7],[0,0,0,1])

if __name__ == "__main__":
    sim = pybullet()
    cube_home_pose = [0.85,-0.2,0.97]

    while True:
        sim.step()
        repeat = int(input("start?"))
        if(repeat == 0):
            sim.step()
            for i in range(1,10):
                sim.pick_which_object(i)
            