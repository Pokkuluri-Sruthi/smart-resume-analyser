from flask import Flask, render_template, request, redirect, url_for
import os

from database import init_db, save_analysis, get_history
from resume_parser import analyze_resume

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "docx"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs("database", exist_ok=True)

init_db()


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "resume" not in request.files:
        return redirect(url_for("index"))

    file = request.files["resume"]

    if file.filename == "":
        return redirect(url_for("index"))

    if not allowed_file(file.filename):
        return "Only PDF and DOCX files are allowed."

    job_description = request.form.get("job_description", "")

    filename = file.filename
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    file.save(filepath)

    result = analyze_resume(filepath, job_description)

    save_analysis(
        filename,
        result["score"],
        result["matched_skills"],
        result["missing_skills"]
    )

    return render_template(
        "result.html",
        result=result,
        filename=filename
    )


@app.route("/history")
def history():
    records = get_history()
    return render_template("history.html", records=records)


if __name__ == "__main__":
    app.run(debug=True)