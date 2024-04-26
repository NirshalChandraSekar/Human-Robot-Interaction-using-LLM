from llm import llm
from speech_processing import speech_processing
from PyBullet_simulation_setup import pybullet
import json
import wandb
import numpy as np

def main():
    gpt = llm()
    process_audio = speech_processing()
    sim = pybullet()
    gpt.init_llm()
    arr = []
    # print("Speak Prompt: ")
    reset = int(input("repeat"))
    while True:
        if(reset == 0):

            prompt = process_audio.speech_to_text()
            if(prompt != "stop"):

                sim.step()
                result = json.loads(gpt.generate_response(prompt)['answer'])
                print(result["object_number"])
                process_audio.text_to_speech(result["text"])
                if result["object_number"] != 0:
                    sim.pick_which_object(result["object_number"])
                arr.append(int(result["score"]))

            else:
                reset = 1
                print(arr)
                sim.reset_pose()
                array = np.array(arr)
                wandb.init(project="sentiment tracking")
                table = wandb.Table(data=np.column_stack((range(len(array)), array)), columns=["x", "y"])
                wandb.log({"line_plot": wandb.plot.line(table, "x", "y", title="Sentiment Plot")})
                wandb.finish()
                arr = []
                reset = int(input("repeat?"))


if __name__ == "__main__":
    main()