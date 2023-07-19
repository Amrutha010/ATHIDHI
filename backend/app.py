# backend/app.py
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations (replace with your actual database settings)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'amrutha'
app.config['MYSQL_DB'] = 'athidhi'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Define API routes for hosts
@app.route('/api/hosts', methods=['GET'])
def get_hosts():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Host')
    hosts = cur.fetchall()
    cur.close()
    return jsonify(hosts)

@app.route('/api/hosts/<int:host_id>', methods=['GET'])
def get_host(host_id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Host WHERE hostId = %s', (host_id,))
    host = cur.fetchone()
    cur.close()

    if host:
        return jsonify(host)
    return jsonify({"message": "Host not found"}), 404

@app.route('/api/hosts', methods=['POST'])
def create_host():
    data = request.get_json()
    host_name = data.get('HostName')
    host_status = data.get('hostStatus')
    location = data.get('Location')
    about = data.get('About')
    hosting_since = data.get('HostingSince')

    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO Host (HostName, hostStatus, Location, About, HostingSince) VALUES (%s, %s, %s, %s, %s)',
                (host_name, host_status, location, about, hosting_since))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Host created successfully"}), 201

@app.route('/api/hosts/<int:host_id>', methods=['PUT'])
def update_host(host_id):
    data = request.get_json()
    host_name = data.get('HostName')
    host_status = data.get('hostStatus')
    location = data.get('Location')
    about = data.get('About')
    hosting_since = data.get('HostingSince')

    cur = mysql.connection.cursor()
    cur.execute('UPDATE Host SET HostName = %s, hostStatus = %s, Location = %s, About = %s, HostingSince = %s WHERE hostId = %s',
                (host_name, host_status, location, about, hosting_since, host_id))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Host updated successfully"})

@app.route('/api/hosts/<int:host_id>', methods=['DELETE'])
def delete_host(host_id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Host WHERE hostId = %s', (host_id,))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Host deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
