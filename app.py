from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # allows index.html (opened in browser) to talk to this server


def get_db():
    conn = sqlite3.connect('instance/school.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Create the users table if it doesn't exist yet,
    and add one test user so you can try logging in right away.
    """
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Add a test user only if the table is empty
    existing = conn.execute('SELECT * FROM users').fetchall()
    if len(existing) == 0:
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                     ('admin', '1234'))
        print("Test user created -> username: admin, password: 1234")                     

    conn.commit()
    conn.close()


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    conn = get_db()
    user = conn.execute(
        'SELECT * FROM users WHERE username = ? AND password = ?',
        (username, password)
    ).fetchone()
    conn.close()

    if user:
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        return jsonify({'success': False, 'message': 'Invalid username or password'})


if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)