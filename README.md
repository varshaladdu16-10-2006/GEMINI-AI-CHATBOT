# 🤖 Gemini AI Chatbot

A simple and interactive **AI Chatbot** built using **Python, Streamlit, and Google Gemini API**.

This chatbot allows users to communicate with an AI assistant through a user-friendly web interface and receive AI-generated responses to their questions.

## 🌐 Live Demo

You can try the deployed application here:

[Gemini AI Chatbot – Live Demo](https://gemini-ai-chatbot-5wj8hl4ai8tua3pq4bzalj.streamlit.app/?utm_source=chatgpt.com)

## ✨ Features

* 🤖 AI-powered chatbot
* 💬 Interactive chat interface
* 🧠 Uses Google Gemini for generating responses
* 🌐 Web-based application using Streamlit
* ⚡ Fast and simple user interaction
* 📱 Easy-to-use interface
* 🔄 Supports multiple questions and responses

## 🛠️ Technologies Used

* **Python** – Backend programming
* **Streamlit** – Web application framework
* **Google Gemini API** – AI response generation
* **GitHub** – Source code management
* **Streamlit Cloud** – Application deployment

## 📂 Project Structure

```text
Gemini-AI-Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ How to Run the Project Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Gemini-AI-Chatbot
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API Key

Create a `.streamlit/secrets.toml` file:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

**Do not upload your API key to GitHub.**

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔑 API Key

This project uses the **Google Gemini API** to generate AI responses.

For security, the API key should be stored using Streamlit secrets or environment variables instead of directly writing it inside the source code.

## 🚀 Deployment

The application is deployed using **Streamlit Community Cloud**.

The deployed application can be accessed here:
