import os
import markdown
from flask import Flask, render_template_string

app = Flask(__name__)

# Basic CSS for a "C-Suite" minimalist look
CSS = """
body { font-family: 'Inter', sans-serif; line-height: 1.6; color: #1a1a1a; max-width: 800px; margin: 40px auto; padding: 20px; }
h1 { color: #2c3e50; border-bottom: 2px solid #eee; padding-bottom: 10px; }
h2 { color: #34495e; margin-top: 30px; }
blockquote { background: #f9f9f9; border-left: 5px solid #ccc; padding: 10px 20px; font-style: italic; }
hr { border: 0; border-top: 1px solid #eee; margin: 40px 0; }
"""

@app.route('/')
def index():
    # Force the app to look in its own directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    reports = [f for f in os.listdir(base_dir) if f.startswith('brief_') and f.endswith('.md')]
    
    if not reports:
        # Debugging: show the current path if it fails
        return f"<h1>No briefings available. (Searching in: {base_dir})</h1>"
    
    latest_report = sorted(reports)[-1]
    report_path = os.path.join(base_dir, latest_report)
    
    with open(report_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    # Convert MD to HTML and wrap in basic template
    # 'extra' is a super-set that includes tables, fenced_code, and more.
    html_body = markdown.markdown(md_text, extensions=['extra', 'sane_lists', 'nl2br'])
    
    return render_template_string(f"""
        <!DOCTYPE html>
        <html>
        <head><title>Lighthouse 3 Portal</title><style>{CSS}</style></head>
        <body>{html_body}</body>
        </html>
    """)

if __name__ == "__main__":
    # Cloud Run provides the PORT environment variable
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))