<div align="center">
  <a href="https://github.com/Jay-Sung-Lim/AI-ChatBot">
    <img src="https://github.com/Jay-Sung-Lim/AI-ChatBot/assets/107202611/097bcb08-7b3f-4643-a28a-df4e3689493e" alt="Logo" width="150" height="150">
  </a>
  
  <h3 align="center">AI Chatbot</h3>

  <p align="center">
    Give a website link to AI and ask questions
    <br />
    <a href="https://github.com/Jay-Sung-Lim/AI-ChatBot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://ai-chatbot-hackville2024.streamlit.app/">View Demo</a>
    ·
    <a href="https://github.com/Jay-Sung-Lim/AI-ChatBot/issues">Report Bug</a>
    ·
    <a href="https://github.com/Jay-Sung-Lim/AI-ChatBot/issues">Request Feature</a>
  </p>
</div>

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#deployment">Deployment</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


# About The Project
![images](https://github.com/Jay-Sung-Lim/AI-ChatBot/assets/107202611/e5094165-70ba-4590-8690-8dc39461edc2)
This project is built using Python and the LangChain framework. Users can input the URL of the desired website and ask questions to the AI.

The project leverages LangChain's Retrieval Augmented Generation (RAG) system to utilize external data sources. Through the processes of loading, transforming, and embedding, the data is stored in a vector store. Refined answers are then retrieved using the LangChain system.

In this project, the main language model employed is OpenAI's GPT-3.5 Turbo. The frontend chatbot interface is implemented using Streamlit, a pure Python UI library.

Follow the instructions in the "Installation" section below to create your own chatbot!


# Built With
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/-LangChain-006600?logo=chainlink&logoColor=white&style=for-the-badge)
![streamlit](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)


# Getting Started

## Prerequisites
* Get API Key at [https://platform.openai.com/](https://platform.openai.com/)

## Installation
1. Clone the repo
   ```
   git clone https://github.com/Jay-Sung-Lim/AI-ChatBot.git
   ```
   
2. Enter your API Key in `.streamlit/.secrets.toml`
   ```
   OPENAI_API_KEY = YOUR_API_KEY_HERE
   ```
   
3. Install Virtual Environment
   ```
   python -m venv env
   ```
   
4. Activate Virtual Environment
   ```
   source env/bin/activate
   ```
5. Install Python Packages
   ```
   pip install -r requirements.txt
   ```
6. Run Home.py with Streamlit
   ```
   streamlit run Home.py
   ```
   
   

# Deployment
The website is deployed and hosted through Streamlit Cloud. You can access the live website at [https://ai-chatbot-hackville2024.streamlit.app/](https://ai-chatbot-hackville2024.streamlit.app/).

# Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

# License
This project is licensed under the MIT License. See the `License.txt` file for details.
