# 🎬 Vista – Video Intelligence AI

**Vista** is a modern web application designed to analyze video content, extract transcripts, and generate **AI-powered insights instantly**.
The application leverages **DeepSeek LLM** to produce comprehensive summaries, topic clustering, and key highlights from **YouTube videos** or **uploaded transcript files**.

This project was developed as a **Graduation Project**, aiming to demonstrate the practical integration of **Large Language Models (LLMs)** with **video data processing** and **natural language understanding**.

---

## 🚀 Key Features

### 📺 YouTube Integration

* Extracts **metadata** and **time-stamped transcripts** directly from YouTube URLs
* No need to download the video file

### 📂 File Support

* Supports manual upload of `.txt` transcript files
* Enables **offline analysis**

### 🧠 AI-Powered Analysis (DeepSeek)

* **Executive Summary** – Concise overview of video content
* **Topic Clustering** – Groups and categorizes main discussion topics
* **Key Highlights** – Extracts the most impactful sentences and quotes

### 🎨 Modern User Interface

* Built with **Streamlit**
* Clean, responsive design with **Dark Mode** support

### ⬇️ Data Export

* Download processed transcripts and AI outputs as `.txt` files

---

## 🛠️ Tech Stack

| Technology      | Description                                       |
| --------------- | ------------------------------------------------- |
| **Python**      | Core backend logic and data processing            |
| **Streamlit**   | Frontend framework for rapid web app development  |
| **yt-dlp**      | Extracts YouTube metadata and transcripts         |
| **OpenAI SDK**  | Client for interacting with the DeepSeek API      |
| **DeepSeek V3** | Large Language Model (LLM) used for text analysis |
| **Regex**       | Text pattern matching and HTML formatting         |

---

## ⚙️ Installation & Setup

Follow the steps below to run the project locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/vista-video-intelligence-ai.git
cd vista-video-intelligence-ai
```

---

### 2️⃣ Create a Virtual Environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 🔑 Configuration (DeepSeek API Key)

To enable AI-powered analysis, a valid **DeepSeek API Key** is required.

1. Run the application
2. Open the **Sidebar** (left panel)
3. Enter your **DeepSeek API Key** in the settings box

> ⚠️ **Note:**
> The API key is **not stored permanently** and is only used for the current session.

---

## 📂 Project Structure

```
vista-video-intelligence-ai/
├── app.py                # Main application entry point (Frontend)
├── youtube_helper.py     # YouTube transcript extraction module
├── ai_helper.py          # DeepSeek API integration (AI logic)
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## 🎓 Academic Context

This project was developed as a **Graduation Project**, focusing on:

* Real-world usage of **Large Language Models**
* Video transcript processing
* AI-based content summarization and analysis
* Practical deployment of an interactive AI web application

---

## 📌 License

*Add license information here (e.g., MIT License).*
