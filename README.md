# 🗼 Lighthouse 3: Strategic Intelligence Advisor

**Lighthouse 3** is a high-reasoning autonomous research agent designed to provide C-Suite executives with high-signal, "noise-filtered" market intelligence. Developed for the **Gemini 3 Hackathon**, it leverages deep synthesis to transform raw global data into boardroom-ready strategic briefings.

## 🚀 Live Portal
The agent's output is rendered through a minimalist, executive-facing web portal:
**[View Live Strategic Briefing](https://lighthouse-portal-91439230830.us-central1.run.app)**

## 🧠 Intelligence Engine
* **High-Reasoning Synthesis:** Leverages `gemini-3-pro-preview` with `thinking_level=HIGH` to identify "Hidden Connections" and secondary effects across global markets.
* **Grounded Research:** Integrated with **Google Search Grounding** to ensure every briefing is anchored in real-time, verified data.
* **Auditability:** Every report includes a **"Thought Signature"**, a transparent log of the AI's internal reasoning process to build executive trust.
* **ROI-First Lens:** Engineered to bypass "hype cycles," focusing instead on capital allocation, revenue drivers, and infrastructure shifts.

## 🛠️ Tech Stack
* **LLM:** Gemini 3 Pro Preview (Google GenAI SDK)
* **Search:** Google Search Tool (Grounding)
* **Backend:** Python 3.10 / Flask
* **Deployment:** Google Cloud Run (Containerized via Docker)
* **Orchestration:** Gunicorn (Production-grade WSGI server)

## 📥 Local Development
1. **Clone Repo:** `git clone https://github.com/agbro/lighthouse-3`
2. **Install Dependencies:** `pip install -r requirements.txt`
3. **Configure Environment:** Create a `.env` file with your `GEMINI_API_KEY`.
4. **Execute Research Agent:** `python researcher.py` (Generates the `.md` briefing)
5. **Launch Local Portal:** `python app.py` (Serves the briefing at localhost:8080)

## 🏗️ Deployment
This project is optimized for **Google Cloud Run**. It utilizes a tailored `.gcloudignore` configuration to ensure lean container builds by excluding virtual environments and documentation while prioritizing mission-critical report assets.