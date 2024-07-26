from flask import Flask, request, jsonify
import psycopg2

app = Flask(_name_)

# Database connection setup
conn = psycopg2.connect("dbname=weed_db user=postgres password=secret")
cursor = conn.cursor()

@app.route('/update_status', methods=['POST'])
def update_status():
    data = request.json
    robot_id = data['robot_id']
    status = data['status']
    cursor.execute("INSERT INTO status_log (robot_id, status) VALUES (%s, %s)", (robot_id, status))
    conn.commit()
    return jsonify({'message': 'Status updated successfully'}), 200

@app.route('/get_status/<robot_id>', methods=['GET'])
def get_status(robot_id):
    cursor.execute("SELECT * FROM status_log WHERE robot_id = %s", (robot_id,))
    status = cursor.fetchall()
    return jsonify({'status': status}), 200

if _name_ == '_main_':
    app.run(debug=True)
