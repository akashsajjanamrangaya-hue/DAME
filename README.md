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
│   └── fake_google.css
└── templates/
    ├── index.html
    ├── fake_google.html
    └── fake_google_results.html
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
- **static/fake_google.css**: Full styling for the gateway, fake Google home, and results pages.
- **logs.txt**: Stores abnormal activity logs (keyword, timestamp, redirection type).

## ✅ How Normal vs Abnormal Is Detected
- **Normal**: The keyword is exactly one of the allowed values in `dataset.json` (google, amazon, youtube).
- **Abnormal**: Any of the following triggers abnormal behavior:
  - Forbidden patterns like `/`, `?`, or `..`
  - Sensitive keywords like `admin` or `config`
  - Any keyword not in the allowed list

## ✅ How Fake Site Cloning Works
- The backend checks the keyword and, if abnormal, loads the Google-like clone:
  - `fake_google.html` for the home page
  - `fake_google_results.html` for search results
- All search results are generated locally with JavaScript and stay inside the fake environment.

## ⚠️ Notes
- This is a **rule-based** system (no AI/ML).
- Fake pages are for demonstration only.
- The session keeps a user in fake pages once abnormal behavior is detected.

---
Made for academic demonstration purposes.
