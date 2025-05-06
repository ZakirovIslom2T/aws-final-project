from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
    host="rds-islam.ct6ei6agkus4.ap-south-1.rds.amazonaws.com",
    database="db_islam",
    user="postgres",
    password="postgres",
    port="5432"
)

@app.route('/data', methods=['GET'])
def get_data():
    cur = conn.cursor()
    cur.execute("SELECT app_id, app_name, categories FROM tbl_islam_apps_info ORDER BY app_id DESC")
    rows = cur.fetchall()
    cur.close()
    return jsonify(rows)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    app_name = data.get('app_name')
    categories = data.get('categories')
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tbl_islam_apps_info (app_name, categories) VALUES (%s, %s)",
        (app_name, categories)
    )
    conn.commit()
    cur.close()
    return jsonify({'message': 'Row added'})

@app.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()
    app_id = data.get('app_id')
    cur = conn.cursor()
    cur.execute("DELETE FROM tbl_islam_apps_info WHERE app_id = %s", (app_id,))
    conn.commit()
    cur.close()
    return jsonify({'message': 'Row deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
