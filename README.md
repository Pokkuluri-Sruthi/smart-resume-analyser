# Smart Resume Analyzer

A full-stack web application that analyzes resumes and evaluates their suitability for a specific job description.

## Live Demo

https://smart-resume-analyser-xczg.onrender.com/

## Features

* Upload PDF or DOCX resumes
* Generate a resume score
* Extract skills and contact information
* Identify key resume sections
* Compare resume skills with job requirements
* Display matched and missing skills
* Provide improvement suggestions
* Store analysis history using SQLite

## Technologies Used

* HTML
* CSS
* JavaScript
* Python
* Flask
* SQLite
* PyPDF2
* python-docx
* Gunicorn

## Project Structure

```text
smart-resume-analyser/
│
├── app.py
├── database.py
├── resume_parser.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── history.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── database/
└── uploads/
```

## How It Works

The application extracts text from an uploaded resume, analyzes its content, calculates a score, and compares detected skills with the provided job description. Results are displayed through the web interface and stored in SQLite.

## Run Locally

```bash
git clone https://github.com/YOUR-USERNAME/smart-resume-analyser.git
cd smart-resume-analyser
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Deployment

The application is deployed using Render with Gunicorn.

## Future Enhancements

* AI-powered resume analysis
* Advanced ATS scoring
* Semantic job matching
* User authentication
* PostgreSQL integration
* Personalized job recommendations

## Purpose

Developed as a portfolio project to demonstrate full-stack development, Python backend development, database integration, document processing, and deployment.
