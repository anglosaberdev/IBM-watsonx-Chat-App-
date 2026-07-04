# IBM watsonx Chat App 🤖

A Flask-based Generative AI web application powered by **IBM watsonx.ai** that allows users to select from multiple Large Language Models (LLMs) and interact with them through a simple chat interface.

This project was developed as part of the **IBM Develop Generative AI Applications** course on Coursera.

---

## 🚀 Features

* Chat with multiple AI models
* Select your preferred model before asking a question
* Supports:

  * Llama
  * Granite
  * Mistral
* Built using IBM ChatWatsonx
* Simple and responsive Flask web interface
* Prompt engineering using LangChain Prompt Templates

---

## 🛠️ Technologies Used

* Python
* Flask
* IBM watsonx.ai
* ChatWatsonx
* LangChain
* HTML
* CSS
* JavaScript

---

## 📂 Project Structure

```text
ibm-watsonx-chat-app/
│
├── app.py                  # Flask application
├── model.py                # AI model initialization and response generation
├── config.py               # IBM credentials and model configuration
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/ibm-watsonx-chat-app.git
```

Move into the project directory:

```bash
cd ibm-watsonx-chat-app
```

Create a virtual environment:

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

Create a `config.py` file (or use environment variables) and add your IBM watsonx.ai credentials:

```python
API_KEY = "YOUR_API_KEY"
PROJECT_ID = "YOUR_PROJECT_ID"
URL = "YOUR_WATSONX_URL"
```

Configure the available models:

```python
LLAMA_MODEL_ID = "..."
GRANITE_MODEL_ID = "..."
MISTRAL_MODEL_ID = "..."
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 💡 How It Works

1. Select an AI model.
2. Enter your question.
3. The application sends the prompt to IBM ChatWatsonx.
4. The selected model generates a response.
5. The answer is displayed instantly in the chat interface.

---

## 📸 Demo

Add screenshots or a GIF of your application here.

Example:

```
screenshots/home.png
screenshots/chat.png
```

---

## 🎓 Learning Outcomes

Through this project, I learned how to:

* Build AI-powered web applications with Flask
* Integrate IBM watsonx.ai with Python
* Work with multiple LLMs
* Use LangChain Prompt Templates
* Design a simple interactive chat interface
* Handle API responses and model selection

---

## 📚 Course

This project was created while completing the **Develop Generative AI Applications: Get Started** course offered by IBM on Coursera.

---

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome. Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is intended for educational purposes.

MIT License.
