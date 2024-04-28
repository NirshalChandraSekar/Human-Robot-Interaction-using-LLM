<p align="center">
  <h2 align="center">HUMAN ROBOT INTERACTION USING LLM</h2>
</p>

<img src="https://github.com/NirshalNiru/Human-Robot-Interaction-using-LLM/blob/9efc2ba087d3556df6e64c36b67a8a66ce521d45/image.png">

### About the project
The advancement of technology has enhanced daily comfort, yet there remains a gap in emotional support. Initially, robots were perceived as rigid and unapproachable, which made it challenging for users to rely on them for effective communication. To improve human-robot interaction, it is crucial for robots to understand human sentiments and empathize accordingly. With this objective in mind, our goal is to develop a social robot that users can depend on for companionship, guidance, and emotional support. The primary aim of this social robot is to generate empathetic responses based on the user's speech and provide objects that may be needed in a virtual environment.

### Demo
Watch the full video here: https://drive.google.com/file/d/1xd6yHDAU-aS1a9mcW1AZJ8jg_G-mB6Li/view?usp=sharing

### Methodology
Upon receiving user speech, the system performs speech-to-text conversion, converting the audio into text format which is then processed by a Large Language Model (LLM) to understand the user's semantic intent and sentiment. Based on this, the LLM generates an empathetic response in text format, which is then converted back to speech output to the user. Simultaneously, in a virtual environment, a KUKA robot offers an object aimed at improving the user's sentiment, with the LLM suggesting appropriate virtual objects from the simulated environment. The LLM continuously tracks and adapts to the user's changing sentiment levels throughout the interaction. The system is integrated within Python 3.11, utilizing speech recognition libraries, the GPT-3.5 Turbo LLM, and the PyBullet simulation tool for controlling/animating the KUKA robot.

### Usage
*The pipeline is tested in Python 3.11 version*
##### Required Libraries/Tools
1) Speech Recognition Module - To recognize the input audio from the user and convert it to text
   ```
   pip install SpeechRecognition
   ```
2) pyttsx3 Module - To convert the output text into speech to the user
   ```
   pip install pyttsx3
   ```
3) PyBullet - Physics simulation package
   ```
   pip install pybullet
   ```
4) Guidance - For controlling langiage models
   ```
   pip install guidance
   ```
--> Clone this repo on your local directory, and install all the above mentioned packages. 

--> Navigate to the "llm.py" file and set your OpenAI API key in line 8.

--> Run the main.py file on your terminal. Input '0' to start your conversation with the robot, and when you want to stop the conversation just say "STOP" out loud, and the simulation will rest and wait for you to input 0 again to continue your next conversation.

### Evaluation
For evaluations, we enabled the LLM to track and store the user's sentiment on a scale of 0 to 10 for each prompt, with 0 being extremely negative and 10 being extremely positive. When the user stops the conversation, we return this tracked sentiments ovre the conversation as a list and plot them to see how the user's sentiment is being changed over the period of the conversation. The goal is to try and flip the sentiment from a negative state to a positve state if the user is initially in a negative mood, and if the person is initially in a positive mood, then the llm should try and maintain this positivity of the user during the conversation.

Sample plots of sentiment over different conversations:
<img src="https://github.com/NirshalNiru/Human-Robot-Interaction-using-LLM/blob/b8673fd4ec24afbbebf980239f22380117c6f870/plots.png">

