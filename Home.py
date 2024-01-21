import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🤖",
)

st.markdown(
"""

# Welcome!
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

# Give It a Try!
[Website Chatbot](/Website_ChatBot)
Click the link or "Website ChatBot" on the sidebar


# How to Install Your Own ChatBot

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

"""
)