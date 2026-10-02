import os

from flask import Flask, redirect, render_template, request, url_for
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "db"),
        port=os.getenv("POSTGRES_PORT", "5432"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        dbname=os.getenv("POSTGRES_DB"),
    )


@app.route("/")
def index():
    with get_db_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "SELECT id, name, email, department, course "
                "FROM students ORDER BY id;"
            )
            students = cur.fetchall()
    return render_template("index.html", students=students)


@app.post("/students")
def add_student():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    department = request.form.get("department", "").strip()
    course = request.form.get("course", "").strip()

    if not name or not email:
        return "Name and email are required.", 400

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO students (name, email, department, course)
                VALUES (%s, %s, %s, %s);
                """,
                (name, email, department, course),
            )
        conn.commit()

    return redirect(url_for("index"))


@app.post("/students/<int:student_id>/delete")
def delete_student(student_id):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM students WHERE id = %s;", (student_id,))
        conn.commit()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
