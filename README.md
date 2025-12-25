🎬 Video Intelligence AIVideo Intelligence AI is a modern web application designed to analyze video content, extract transcripts, and generate AI-powered insights instantly. Leverages DeepSeek LLM to provide comprehensive summaries, topic clustering, and key highlights from YouTube videos or uploaded transcript files.This project was developed as a Graduation Project to demonstrate the integration of Large Language Models (LLMs) with video data processing.🚀 Key Features📺 YouTube Integration: Automatically extracts metadata and time-stamped transcripts from YouTube URLs without downloading the video file.📂 File Support: Supports manual upload of .txt transcript files for offline analysis.🧠 AI-Powered Analysis (DeepSeek):Executive Summary: A concise overview of the video content.Topic Clustering: Categorizes main talking points.Key Highlights: Extracts the most impactful sentences and quotes.🎨 Modern UI: A sleek, user-friendly interface built with Streamlit (Dark Mode supported).⬇️ Data Export: Allows users to download processed transcripts as .txt files.🛠️ Tech StackThis project is built using the following technologies and libraries:TechnologyDescriptionPythonCore backend logic and data processing.StreamlitFrontend framework for rapid web app development.yt-dlpRobust command-line audio/video downloader for data extraction.OpenAI SDKClient used to interact with the DeepSeek API.DeepSeek V3The Large Language Model (LLM) used for text analysis.RegexText pattern matching and HTML formatting.📸 Screenshots(Add your project screenshots here. For example: assets/home_screen.png)Main InterfaceAI Analysis Result⚙️ Installation & SetupFollow these steps to set up the project locally.1. Clone the RepositoryBashgit clone https://github.com/YOUR_USERNAME/video-intelligence-ai.git
cd video-intelligence-ai
2. Create a Virtual Environment (Recommended)Bash# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install DependenciesBashpip install -r requirements.txt
4. Run the ApplicationBashstreamlit run app.py
🔑 ConfigurationTo use the AI Analysis features, you need a valid DeepSeek API Key.Run the application.Open the Sidebar (left menu) in the web interface.Enter your API Key in the settings box.Note: Your API key is not stored permanently; it is only used for the current session.📂 Project StructurePlaintextvideo-intelligence-ai/
├── app.py                # Main application entry point (Frontend)
├── youtube_helper.py     # Module for YouTube transcript extraction (Backend)
├── ai_helper.py          # Module for DeepSeek API integration (AI)
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
