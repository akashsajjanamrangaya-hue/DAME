# Behavior-Based Cyber Deception System (Flask)

This is a simple academic project that demonstrates **rule-based** detection of normal vs abnormal behavior and redirects users to real or fake websites accordingly. No AI/ML is used.

## ✅ Features
- Rule-based detection using a JSON dataset
- Redirects to real websites for normal behavior
- Fake (decoy) pages for abnormal behavior with local-only search
- Sticky abnormal session (once abnormal, always fake in that session)
- Logs abnormal activities with timestamps

## 📂 Project Structure
```
.
├── app.py
├── dataset.json
├── logs.txt
├── README.md
├── static/
│   ├── index.css
│   ├── fake_google.css
│   ├── fake_youtube.css
│   ├── fake_amazon.css
│   ├── fake_generic.css
│   └── fake_search.js
└── templates/
    ├── index.html
    ├── fake_youtube.html
    ├── fake_google.html
    ├── fake_amazon.html
    └── fake_generic.html
```

## ▶️ How to Run (Step-by-Step)
1. **Install Python 3** if not already installed.
2. **Install Flask**:
   ```bash
   pip install flask
   ```
3. **Run the application**:
   ```bash
   python app.py
   ```
4. **Open your browser** and go to:
   ```
   http://127.0.0.1:5000
   ```
5. **Try normal keywords** like `google`, `youtube`, or `amazon`.
6. **Try suspicious keywords** like `hack` or `phish` to see fake pages.
7. Use `/reset` to clear the session for testing.

## 🗂️ File Explanation
- **app.py**: Main Flask application with rule-based logic and session handling.
- **dataset.json**: Contains allowed keywords, suspicious keywords, and behavior rules.
- **templates/**: HTML pages (index and fake pages with local search).
- **static/index.css**: Modern UI theme for the main index page.
- **static/fake_google.css**: Fake search page theme.
- **static/fake_youtube.css**: Fake video page theme.
- **static/fake_amazon.css**: Fake store page theme.
- **static/fake_generic.css**: Fake gateway theme for suspicious activity.
- **static/fake_search.js**: Local-only search behavior for fake pages (no external redirects).
- **logs.txt**: Stores abnormal activity logs (keyword, timestamp, redirection type).

## ⚠️ Notes
- This is a **rule-based** system (no AI/ML).
- Fake pages are for demonstration only.
- The session keeps a user in fake pages once abnormal behavior is detected.

---
Made for academic demonstration purposes.
