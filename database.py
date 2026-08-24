import sqlite3

DATABASE = "database/resume_analyzer.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def init_db():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            score INTEGER NOT NULL,
            matched_skills TEXT,
            missing_skills TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_analysis(
    filename,
    score,
    matched_skills,
    missing_skills
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO analyses
        (filename, score, matched_skills, missing_skills)
        VALUES (?, ?, ?, ?)
    """, (
        filename,
        score,
        ", ".join(matched_skills),
        ", ".join(missing_skills)
    ))

    connection.commit()
    connection.close()


def get_history():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, filename, score,
               matched_skills,
               missing_skills,
               created_at
        FROM analyses
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    connection.close()

    return records