# app.py
from flask import Flask, render_template, request, jsonify
import os
import shutil
import re
import requests
from datetime import datetime

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create folders if not exist
os.makedirs(os.path.join(BASE_DIR, "uploads"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "results"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "jpg_destination"), exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run-task", methods=["POST"])
def run_task():
    task = request.json.get("task")
    result = {"success": False, "message": "", "output": ""}

    try:
        if task == "move_jpg":
            source = os.path.join(BASE_DIR, "uploads")
            dest = os.path.join(BASE_DIR, "jpg_destination")
            moved = 0
            for file in os.listdir(source):
                if file.lower().endswith((".jpg", ".jpeg")):
                    shutil.move(os.path.join(source, file), os.path.join(dest, file))
                    moved += 1
            result = {
                "success": True,
                "message": f"Moved {moved} JPG files successfully!",
                "output": f"Check 'jpg_destination' folder"
            }

        elif task == "extract_emails":
            txt_path = os.path.join(BASE_DIR, "uploads", "emails.txt")
            output_path = os.path.join(BASE_DIR, "results", "extracted_emails.txt")
            
            if not os.path.exists(txt_path):
                result["message"] = "Please add 'emails.txt' in 'uploads' folder"
            else:
                with open(txt_path, "r", encoding="utf-8") as f:
                    text = f.read()
                emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
                with open(output_path, "w", encoding="utf-8") as f:
                    for email in emails:
                        f.write(email + "\n")
                result = {
                    "success": True,
                    "message": f"Found {len(emails)} emails!",
                    "output": "\n".join(emails) if emails else "No emails found."
                }

        elif task == "scrape_title":
            url = "https://httpbin.org/html"
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Good practice
            title_match = re.search(r"<title>(.*?)</title>", response.text, re.I)
            page_title = title_match.group(1) if title_match else "No title found"
            result = {
                "success": True,
                "message": "Title scraped successfully!",
                "output": page_title
            }

    except Exception as e:
        result["message"] = f"Error: {str(e)}"
        result["output"] = "Something went wrong. Check console."

    return jsonify(result)

# FIXED THIS LINE → Was "_main_" before!
if __name__ == "__main__":
    app.run(debug=True)