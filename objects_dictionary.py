import math

class objects_in_env:
    obj_dict = {

        1: {
            "name": "bottle",
            "object_id_bullet": None,
            "path": r"URDF Models\bottle\bottle.urdf", 
            "baseposition": [0.95, 0.29 , 0.65],
            "baseorientation": [1, 0, 0, 1],
            "globalscaling": 0.03
        },


        2: {
            "name": "duck",
            "object_id_bullet": None,
            "path": r"URDF Models\duck\duck_vhacd.urdf", 
            "baseposition": [1.13, 0.05 , 0.622],
            "baseorientation": [1, 0, 0, 1],
            "globalscaling": 0.8
        },


        3: {
            "name": "apple",
            "object_id_bullet": None,
            "path": r"URDF Models\plastic_apple\model.urdf",
            "baseposition": [1.05, -0.6, 0.64],
            "baseorientation": [0, 0, 0, 1],
            "globalscaling": 0.9
        },


        4: {
            "name": "potato chips",
            "object_id_bullet": None,
            "path": r"URDF Models\potato_chip_1\model.urdf",
            "baseposition": [1.1, -0.71, 0.65],
            "baseorientation": [0, 0, 0, 1],
            "globalscaling": 0.8
        },


        5: {
            "name": "chewing gum",
            "object_id_bullet": None,
            "path": r"URDF Models\suger_2\model.urdf",
            "baseposition": [0.92, -0.65, 0.66],
            "baseorientation": [0, 0, 0, 1],
            "globalscaling": 0.65
        },


        6: {
            "name": "mug",
            "object_id_bullet": None,
            "path": r"URDF Models\orange_cup\model.urdf",
            "baseposition": [1.17 , 0.23 , 0.65],
            "baseorientation": [0, 0, -1, 1],
            "globalscaling": 0.9
        },


        7: {
            "name": "poker",
            "object_id_bullet": None,
            "path": r"URDF Models\poker_1\model.urdf",
            "baseposition": [1 , 0.15 , 0.63],
            "baseorientation": [0, 1, 0, 1],
            "globalscaling": 0.66
        },

        8: {
            "name": "jenga",
            "object_id_bullet": None,
            "path": r"URDF Models\jenga\jenga.urdf",
            "baseposition": [1.2, -0.5, 0.65],
            "baseorientation": [0, 1, 0, 1],
            "globalscaling": 0.9
        },

        9: {
            "name": "joypad",
            "object_id_bullet": None,
            "path": r"URDF Models\joypad\joypad.urdf", 
            "baseposition": [1, -0.46, 0.65],
            "baseorientation": [0.5, 0, 0, 1],
            "globalscaling": 0.09
        }
    }