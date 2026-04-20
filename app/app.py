from flask import Flask, render_template, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "appdb"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppassword"),
        port=os.getenv("DB_PORT", "5432"),
    )

@app.route("/")
def game():
    return render_template("index.html")

@app.route("/score", methods=["POST"])
def save_score():
    try:
        data = request.get_json()
        score = data.get("score", 0)

        conn = get_connection()
        cur = conn.cursor()


        cur.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id SERIAL PRIMARY KEY,
                score INT
            )
        """)


        cur.execute("INSERT INTO scores (score) VALUES (%s)", (score,))

        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"status": "ok"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
