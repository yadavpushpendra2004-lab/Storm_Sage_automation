# 🚀 Storm Sage: The Multimodal AI Content Engine
**An Autonomous, High-Speed YouTube Pipeline for the AI-Augmented Era.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Inference-Groq%20LPU-orange)](https://groq.com/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📖 The Vision & Genesis
Traditional programming is evolving into **Human-AI Symbiosis**. *Storm Sage* was born from the necessity to prove that with the right AI orchestration, a developer can build production-ready systems at 10x velocity. 

**The Sprint:** This project moved from a "Zero Knowledge" state (no prior experience with APIs or Git) to a fully cloud-deployed autonomous system within a **72-hour development window**.

---

## 🛠 Project Evolution: From Script to SaaS

### Phase 1: The Backend Engine (v1.0 - v3.0)
Initially conceived as a CLI-based Python script, the core focused on the **YouTube Data API v3** and **OAuth 2.0** authentication. 
* **Challenge:** Implementing secure credential handling and token refreshment.
* **Solution:** Developed a modular backend to handle recursive folder scanning for batch uploads.

### Phase 2: High-Speed Inference (v4.0)
To reduce latency, the system migrated from standard LLM providers to **Groq LPU (Language Processing Unit)**.
* **Tech:** Integrated **Llama 3.3** for real-time viral metadata (titles/tags) generation.
* **Optimization:** Achieved a 10x reduction in text synthesis time.

### Phase 3: The Multimodal Control Panel (v5.0 - Current)
Transformed the backend tool into a professional end-product using **Streamlit**.
* **Visual Studio:** Integrated **Stable Diffusion** (via Hugging Face Inference API) to allow on-demand thumbnail generation within the dashboard.
* **Architecture:** A full-stack solution connecting a Python backend to a responsive web frontend.

---

## 🧠 Engineering Challenges & Error Handling
Development is 10% coding and 90% troubleshooting. Major hurdles overcome during this journey:

1.  **Unicode & Character Encoding:** Handled `UnicodeDecodeError` (cp1252 vs UTF-8) to support global metadata including emojis.
2.  **API Handshaking:** Managed **Hugging Face "Cold Starts"** by implementing custom **Retry/Polling Logic** to handle 503 Service Unavailable errors.
3.  **SDK Migrations:** Successfully navigated a mid-project migration when models were decommissioned, moving from `google-generativeai` to the latest **Groq SDK** without system downtime.
4.  **Security Protocols:** Implemented strict API key management to prevent credential leaks.

---

## 🚀 Key Features
* **Autonomous Scheduling:** Leverages **GitHub Actions** for 24/7 serverless execution.
* **Multimodal Generation:** AI-driven text (Llama 3.3) and image (Stable Diffusion) synthesis.
* **Production Queue:** A visual dashboard to track, edit, and trigger uploads in real-time.
* **Zero-Cost Architecture:** Built entirely using free-tier high-performance APIs and open-source libraries.

---

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **AI Engines:** Groq (Llama 3.3), Hugging Face (Stable Diffusion)
* **Frontend:** Streamlit
* **APIs:** YouTube Data API v3, Google OAuth 2.0
* **DevOps:** Git, GitHub Actions, Environment Variables (.env)

---

## 📂 Installation & Usage
1. **Clone the Repo:** `git clone https://github.com/yadavpushpendra2004-lab/Storm_Sage_automation.git`
2. **Install Dependencies:** `pip install -r requirements.txt`
3. **Set Keys:** Create a `.env` file with your `GROQ_API_KEY` and `HF_TOKEN`.
4. **Launch:** `streamlit run app.py`

---

## 👤 About the Developer
**Pushpendra Yadav** *First-year MCA Student at IIIT Bhopal* I am a **High-Velocity Learner** and **AI-Augmented Engineer** dedicated to building the future of autonomous software. I believe that in the upcoming years, the ability to orchestrate AI agents will be the primary differentiator for elite developers.

---