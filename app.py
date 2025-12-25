import streamlit as st
import re
from youtube_helper import get_transcript_with_timestamps
from ai_helper import analyze_transcript_with_deepseek

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Video Intelligence AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded" 
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .stTextInput > div > div > input { background-color: #1f2937; color: white; border-radius: 10px; border: 1px solid #4b5563; }
    .stButton > button { background: linear-gradient(to right, #6366f1, #a855f7, #ec4899); color: white; border: none; border-radius: 20px; height: 50px; width: 100%; font-weight: bold; transition: all 0.3s ease; }
    .stButton > button:hover { opacity: 0.8; transform: scale(1.02); }
    .transcript-box { background-color: #111827; padding: 15px; border-radius: 10px; border: 1px solid #374151; height: 400px; overflow-y: scroll; font-family: monospace; font-size: 14px; line-height: 1.6; white-space: pre-wrap; }
    h1, h2, h3 { color: #e5e7eb; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR (API KEY GİRİŞİ) ---
with st.sidebar:
    st.header("⚙️ Ayarlar")
    api_key = st.text_input("DeepSeek API Key", type="password", placeholder="sk-...")
    st.info("API anahtarınız sadece bu oturumda kullanılır ve kaydedilmez.")
    st.markdown("---")
    st.write("Developed for Graduation Project")

# --- YARDIMCI FONKSİYONLAR ---
def format_transcript_for_display(plain_text):
    html_text = re.sub(r'(\[\d{2}:\d{2}\])', r'<span style="color:#a855f7">\1</span>', plain_text)
    html_text = html_text.replace('\n', '<br>')
    return html_text

# --- MAIN INTERFACE ---
st.title("🎬 Video Intelligence AI")
st.markdown("Analyze videos, extract insights, and generate summaries instantly.")

tab1, tab2 = st.tabs(["📺 YouTube URL", "📂 Upload Transcript File (.txt)"])

# --- SESSION STATE ---
if 'yt_data' not in st.session_state:
    st.session_state['yt_data'] = {'raw': None, 'display': None, 'url': None, 'summary': None}
if 'file_data' not in st.session_state:
    st.session_state['file_data'] = {'raw': None, 'display': None, 'summary': None}

# ==========================================
# TAB 1: YOUTUBE BÖLÜMÜ
# ==========================================
with tab1:
    col_input, col_lang, col_btn = st.columns([3, 1, 1])
    with col_input:
        url_input = st.text_input("Enter YouTube URL", placeholder="https://www.youtube.com/watch?v=...")
    with col_lang:
        lang_input = st.text_input("Dil (Opsiyonel)", placeholder="tr, en...")
    with col_btn:
        st.write("") 
        st.write("") 
        if st.button("Get Transcript", key="btn_yt"):
            if url_input:
                with st.spinner("Processing video data..."):
                    st.session_state['file_data'] = {'raw': None, 'display': None, 'summary': None}
                    content, lang = get_transcript_with_timestamps(url_input, lang_input if lang_input else None)
                    
                    if content:
                        st.session_state['yt_data']['raw'] = content
                        st.session_state['yt_data']['display'] = format_transcript_for_display(content)
                        st.session_state['yt_data']['url'] = url_input
                        st.session_state['yt_data']['summary'] = None # Yeni video gelince özeti sıfırla
                        st.success(f"Transcript loaded! (Language: {lang})")
                    else:
                        st.error(lang)
            else:
                st.error("Lütfen bir URL girin.")

    st.divider()

    if st.session_state['yt_data']['raw']:
        col_video, col_trans = st.columns([1, 1])
        with col_video:
            st.subheader("Video Player")
            st.video(st.session_state['yt_data']['url'])
            st.markdown("### Get the transcript:")
            st.download_button(
                label="⬇️ Download .txt",
                data=st.session_state['yt_data']['raw'],
                file_name="youtube_transcript.txt",
                mime="text/plain",
                use_container_width=True 
            )
        with col_trans:
            st.subheader("Transcript")
            st.markdown(f"""<div class="transcript-box">{st.session_state['yt_data']['display']}</div>""", unsafe_allow_html=True)
            
        # --- AI ANALİZİ (YOUTUBE) ---
        st.divider()
        st.header("🧠 AI Analysis (YouTube)")
        
        if st.button("✨ Generate AI Summary & Analysis", key="ai_btn_yt"):
            if not api_key:
                st.warning("Lütfen sol menüden DeepSeek API Anahtarınızı girin.")
            else:
                with st.spinner("Wait a while..."):
                    # AI Helper fonksiyonunu çağırıyoruz
                    analysis_result = analyze_transcript_with_deepseek(api_key, st.session_state['yt_data']['raw'])
                    st.session_state['yt_data']['summary'] = analysis_result
        
        # Sonuç varsa göster
        if st.session_state['yt_data']['summary']:
            st.markdown(st.session_state['yt_data']['summary'])

# ==========================================
# TAB 2: DOSYA YÜKLEME BÖLÜMÜ
# ==========================================
with tab2:
    uploaded_file = st.file_uploader("Upload a transcript file", type=["txt"])
    if uploaded_file is not None:
        if st.button("Process File", key="btn_file"):
            st.session_state['yt_data'] = {'raw': None, 'display': None, 'url': None, 'summary': None}
            stringio = uploaded_file.getvalue().decode("utf-8")
            st.session_state['file_data']['raw'] = stringio
            st.session_state['file_data']['display'] = format_transcript_for_display(stringio)
            st.session_state['file_data']['summary'] = None
            st.success("File processed!")

    st.divider()

    if st.session_state['file_data']['raw']:
        st.subheader("Uploaded Transcript Content")
        st.markdown(f"""<div class="transcript-box" style="height: 500px;">{st.session_state['file_data']['display']}</div>""", unsafe_allow_html=True)
             
        # --- AI ANALİZİ (DOSYA) ---
        st.divider()
        st.header("🧠 AI Analysis (File)")
        
        if st.button("✨ Generate AI Summary & Analysis", key="ai_btn_file"):
            if not api_key:
                st.warning("Lütfen sol menüden DeepSeek API Anahtarınızı girin.")
            else:
                with st.spinner("DeepSeek is analyzing the file..."):
                    analysis_result = analyze_transcript_with_deepseek(api_key, st.session_state['file_data']['raw'])
                    st.session_state['file_data']['summary'] = analysis_result

        if st.session_state['file_data']['summary']:
            st.markdown(st.session_state['file_data']['summary'])