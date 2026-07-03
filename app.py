from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import mysql.connector

# 🔥 FIX 1: correct __name__
app = Flask(__name__)
CORS(app)

# =========================
# DATABASE CONNECTION
# =========================
def get_db():
        return mysql.connector.connect(
        host="mysql://root:OjQjAuMykudnPWHfhhrSWnnNUvyTJYMu@hayabusa.proxy.rlwy.net:50276/railway",
        user="root",
        password="OjQjAuMykudnPWHfhhrSWnnNUvyTJYMu",
        database="railway",
        port=3306
     )

# =========================
# ROUTES (UNCHANGED)
# =========================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/learn1')
def learn1():
    return render_template('learn1.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/page0')
def page0():
    return render_template('page0.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/page4')
def page4():
    return render_template('page4.html')

@app.route('/page5')
def page5():
    return render_template('page5.html')

@app.route('/result')
def result():
    return render_template('result.html')

# =========================
# SAVE RESULT (FIXED)
# =========================
@app.route('/results', methods=['POST'])
def save():
    try:
        data = request.get_json()
        print("DATA RECEIVED:",data)

        name = data.get('name')
        test_name = data.get('test_name')
        score = data.get('score')

        db = get_db()
        cursor = db.cursor()

        sql = "INSERT INTO results (name, test_name, score) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, test_name, score))

        db.commit()

        cursor.close()
        db.close()

        return jsonify({"message": "Saved successfully"}), 200

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

# =========================
# GET RESULTS
# =========================
@app.route('/save', methods=['GET'])
def results():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT name, test_name, score FROM results")
    rows = cursor.fetchall()

    cursor.close()
    db.close()

    result_list = []

    for r in rows:
        result_list.append({
            "name": r[0],
            "test_name": r[1],
            "score": r[2]
        })

    return jsonify(result_list)

# =========================
# FIX 2: correct main check
# =========================
if __name__ == '__main__':
    app.run(debug=True)
