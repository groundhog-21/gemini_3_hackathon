# 💡 Lighthouse 3: Strategic Intelligence Advisor

**Lighthouse 3** is a high-reasoning autonomous research agent designed to provide C-Suite executives with high-signal, "noise-filtered" market intelligence. Built for the **Gemini 3 Hackathon**, it leverages deep synthesis to turn raw global news into actionable strategic briefings.

## 🚀 Key Features
* **High-Reasoning Synthesis:** Uses `gemini-3-pro-preview` with `thinking_level=HIGH` to identify "Hidden Connections" across global markets.
* **Grounded Research:** Integrated with Google Search Grounding to ensure all briefings are anchored in real-time data.
* **Thought Signature:** Every report includes a transparent log of the AI's internal logic, building executive trust through auditability.
* **ROI-First Lens:** Filters out general hype to focus on capital allocation, revenue drivers, and infrastructure shifts.

## 🛠️ Tech Stack
* **Core Model:** Gemini 3 Pro Preview
* **Grounding:** Google Search Tool
* **Infrastructure:** Python 3.10+, `google-genai` SDK
* **Deployment:** (Planned) Google Cloud Run

## 📥 Installation & Usage
1. **Clone Repo:** `git clone https://github.com/your-repo/lighthouse-3`
2. **Install Deps:** `pip install -r requirements.txt`
3. **Set Keys:** Add `GEMINI_API_KEY` to your `.env` file.
4. **Run Hunt:** `python researcher.py`