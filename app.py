"""
Behavior-Based Cyber Deception System (Flask)
Rule-based detection of normal vs abnormal behavior.
"""
from __future__ import annotations

import json
import os
from datetime import datetime

from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "student-demo-secret-key"  # for session tracking (demo only)

DATASET_PATH = os.path.join(os.path.dirname(__file__), "dataset.json")
LOG_PATH = os.path.join(os.path.dirname(__file__), "logs.txt")


def load_dataset() -> dict:
    """Load the rule-based dataset from JSON."""
    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def is_input_normal(keyword: str, dataset: dict) -> tuple[bool, str]:
    """
    Decide if input is NORMAL or ABNORMAL using simple rules.
    Returns (is_normal, reason).
    """
    rules = dataset.get("behavior_rules", {})
    allowed = dataset.get("allowed_keywords", [])
    suspicious = dataset.get("suspicious_keywords", [])

    cleaned = keyword.strip().lower()

    # Rule 1: length check
    if len(cleaned) < rules.get("min_length", 1):
        return False, "too short"
    if len(cleaned) > rules.get("max_length", 100):
        return False, "too long"

    # Rule 2: block forbidden patterns or characters
    for pattern in rules.get("forbidden_patterns", []):
        if pattern in cleaned:
            return False, f"contains forbidden pattern: {pattern}"

    # Rule 3: only letters, numbers, spaces (basic sanitization)
    if rules.get("allow_only_letters_numbers_spaces", False):
        for char in cleaned:
            if not (char.isalnum() or char.isspace()):
                return False, "invalid characters"

    # Rule 4: suspicious keywords
    if rules.get("block_if_contains_suspicious", False):
        for bad_word in suspicious:
            if bad_word in cleaned:
                return False, f"contains suspicious keyword: {bad_word}"

    # Rule 5: not in allowed list (soft rule)
    if cleaned not in allowed:
        return False, "not in allowed keywords"

    return True, "normal"


def log_abnormal(keyword: str, redirection: str) -> None:
    """Append abnormal activity to logs.txt with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] keyword='{keyword}' redirection='{redirection}'\n"
    with open(LOG_PATH, "a", encoding="utf-8") as file:
        file.write(line)


def decide_fake_template(keyword: str) -> str:
    """Pick which fake page to show based on keyword."""
    cleaned = keyword.strip().lower()
    if "youtube" in cleaned:
        return "fake_youtube.html"
    if "google" in cleaned:
        return "fake_google.html"
    if "amazon" in cleaned:
        return "fake_amazon.html"
    return "fake_google.html"


def real_site_redirect(keyword: str):
    """Redirect to the real site for known keywords."""
    cleaned = keyword.strip().lower()
    url_map = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "amazon": "https://www.amazon.com",
        "wikipedia": "https://www.wikipedia.org",
        "github": "https://github.com",
        "stackoverflow": "https://stackoverflow.com",
    }
    return redirect(url_map.get(cleaned, "https://www.google.com"))


@app.route("/", methods=["GET", "POST"])
def index():
    """Main page: input a keyword and get redirected based on behavior."""
    dataset = load_dataset()
    if request.method == "POST":
        keyword = request.form.get("keyword", "")

        # If the session is already marked abnormal, keep user in fake pages.
        if session.get("abnormal"):
            template = decide_fake_template(keyword)
            log_abnormal(keyword, "FAKE (sticky session)")
            return render_template(template, keyword=keyword)

        is_normal, reason = is_input_normal(keyword, dataset)

        if is_normal:
            session["abnormal"] = False
            return real_site_redirect(keyword)

        # Mark session as abnormal and send to fake page
        session["abnormal"] = True
        template = decide_fake_template(keyword)
        log_abnormal(keyword, "FAKE (abnormal)")
        return render_template(template, keyword=keyword)

    return render_template("index.html")


@app.route("/reset")
def reset():
    """Reset session for demo/testing."""
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
