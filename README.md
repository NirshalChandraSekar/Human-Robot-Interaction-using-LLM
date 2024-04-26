<p align="center">
  <h2 align="center">HUMAN ROBOT INTERACTION USING LLM</h2>
</p>

### About the project
The advancement of technology has enhanced daily comfort, yet there remains a gap in emotional support. Initially, robots were perceived as rigid and unapproachable, which made it challenging for users to rely on them for effective communication. To improve human-robot interaction, it is crucial for robots to understand human sentiments and empathize accordingly. With this objective in mind, our goal is to develop a social robot that users can depend on for companionship, guidance, and emotional support. The primary aim of this social robot is to generate empathetic responses based on the user's speech and provide objects that may be needed in a virtual environment.

### Demo
Watch the full video here: https://drive.google.com/file/d/1xd6yHDAU-aS1a9mcW1AZJ8jg_G-mB6Li/view?usp=sharing

### Methodology
Upon receiving user speech, the system performs speech-to-text conversion, converting the audio into text format which is then processed by a Large Language Model (LLM) to understand the user's semantic intent and sentiment. Based on this, the LLM generates an empathetic response in text format, which is then converted back to speech output to the user. Simultaneously, in a virtual environment, a KUKA robot offers an object aimed at improving the user's sentiment, with the LLM suggesting appropriate virtual objects from the simulated environment. The LLM continuously tracks and adapts to the user's changing sentiment levels throughout the interaction. The system is integrated within Python 3.11, utilizing speech recognition libraries, the GPT-3.5 Turbo LLM, and the PyBullet simulation tool for controlling/animating the KUKA robot.
