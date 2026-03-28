import streamlit as st
import os
import requests
import io
import time
from PIL import Image
from dotenv import load_dotenv
from groq import Groq
# Backend function import (ensure uploader.py is in the same folder)
from uploader import schedule_short_folder 

# --- 1. LOAD ENVIRONMENT VARIABLES ---
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

# --- 2. INITIALIZE CLIENTS ---
# Groq Client
if GROQ_API_KEY:
    groq_client = Groq(api_key=GROQ_API_KEY)
else:
    st.error("GROQ_API_KEY missing in .env file!")

# Hugging Face Config
HF_API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# --- 3. UI CONFIGURATION ---
st.set_page_config(page_title="Storm Sage Control Panel", page_icon="🚀", layout="wide")

st.title("🚀 Storm Sage: The Multimodal AI Engine")
st.markdown(f"**Developer:** Pushpendra Yadav (IIIT Bhopal) | **Status:** Production v5.0")
st.divider()

# --- 4. SIDEBAR: SYSTEM MONITOR ---
st.sidebar.header("📊 System Monitor")
queue_dir = "Shorts_Queue"
if os.path.exists(queue_dir):
    folders = [f for f in os.listdir(queue_dir) if os.path.isdir(os.path.join(queue_dir, f))]
    st.sidebar.metric("Pending Shorts", len(folders))
else:
    folders = []
    st.sidebar.error("Queue Folder Missing!")

# --- 5. SECTION 1: GROQ METADATA GENERATOR ---
st.header("🪄 1. AI Metadata Generator (Groq)")
col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_input("Enter Video Topic", placeholder="e.g., The Life Cycle of a Massive Star")
    if st.button("Generate Script & Tags"):
        if topic and GROQ_API_KEY:
            with st.spinner("Groq is synthesizing viral content..."):
                try:
                    chat_completion = groq_client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": "You are a YouTube SEO expert. Generate a viral title and description with hashtags."},
                            {"role": "user", "content": f"Generate metadata for: {topic}"}
                        ],
                        model="llama-3.3-70b-versatile",
                    )
                    st.session_state['ai_result'] = chat_completion.choices[0].message.content
                    st.success("Metadata Generated!")
                except Exception as e:
                    st.error(f"Groq Error: {e}")
        else:
            st.warning("Input topic and ensure API Key is set.")

if 'ai_result' in st.session_state:
    with col1:
        suggested_text = st.text_area("Suggested Content", st.session_state['ai_result'], height=200)

# --- 6. SECTION 2: AI VISUAL STUDIO (Hugging Face) ---
st.divider()
st.header("🎨 2. AI Visual Studio")

visual_prompt = st.text_input("Thumbnail Description", placeholder="cinematic view of a dying star, 8k, nebula")

def query_hf(payload, max_retries=3):
    for i in range(max_retries):
        response = requests.post(HF_API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            return response.content
        elif response.status_code == 503:
            st.info(f"Model loading... Attempt {i+1}/{max_retries}")
            time.sleep(20)
    return None

if st.button("Generate Visual"):
    if visual_prompt and HF_TOKEN:
        with st.spinner("Synthesizing Visual..."):
            img_bytes = query_hf({"inputs": visual_prompt})
            if img_bytes:
                try:
                    image = Image.open(io.BytesIO(img_bytes))
                    st.image(image, caption="AI Generated Thumbnail", use_container_width=True)
                    st.session_state['last_img_data'] = img_bytes
                except Exception as e:
                    st.error(f"Image Decode Error: {e}")
            else:
                st.error("HF Model failed to respond. Try again in 1 min.")
    else:
        st.warning("Check your prompt and HF Token.")

# --- 7. SECTION 3: FINAL PRODUCTION & UPLOAD ---
st.divider()
st.header("🚀 3. Final Production & Upload")

if folders:
    selected_folder = st.selectbox("Select Project Folder", folders)
    c1, c2 = st.columns(2)
    
    with c1:
        if st.button("💾 Save All to Folder"):
            folder_path = os.path.join(queue_dir, selected_folder)
            
            # Save Metadata
            if 'ai_result' in st.session_state:
                with open(os.path.join(folder_path, "metadata.txt"), "w", encoding="utf-8") as f:
                    f.write(st.session_state['ai_result'])
            
            # Save Image
            if 'last_img_data' in st.session_state:
                with open(os.path.join(folder_path, "thumbnail.jpg"), "wb") as f:
                    f.write(st.session_state['last_img_data'])
            
            st.success(f"Assets saved to {selected_folder}!")

    with c2:
        if st.button("📢 Trigger YouTube Upload"):
            with st.spinner("Uploading via Backend..."):
                schedule_short_folder(os.path.join(queue_dir, selected_folder))
                st.success("Upload Request Sent!")

st.sidebar.divider()
st.sidebar.caption("Project: Storm Sage | v5.0 Final")