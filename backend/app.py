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


# Define API routes for properties
@app.route('/api/properties', methods=['GET'])
def get_properties():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Property')
    properties = cur.fetchall()
    cur.close()
    return jsonify(properties)

@app.route('/api/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Property WHERE propertyId = %s', (property_id,))
    property_item = cur.fetchone()
    cur.close()

    if property_item:
        return jsonify(property_item)
    return jsonify({"message": "Property not found"}), 404

@app.route('/api/properties', methods=['POST'])
def create_property():
    data = request.get_json()
    host_id = data.get('hostId')
    images = data.get('Images')
    price = data.get('Price')
    location = data.get('Location')
    description = data.get('Description')
    host_details = data.get('HostDetails')

    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO Property (hostId, Images, Price, Location, Description, HostDetails) VALUES (%s, %s, %s, %s, %s, %s)',
                (host_id, images, price, location, description, host_details))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Property created successfully"}), 201

@app.route('/api/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    data = request.get_json()
    host_id = data.get('hostId')
    images = data.get('Images')
    price = data.get('Price')
    location = data.get('Location')
    description = data.get('Description')
    host_details = data.get('HostDetails')

    cur = mysql.connection.cursor()
    cur.execute('UPDATE Property SET hostId = %s, Images = %s, Price = %s, Location = %s, Description = %s, HostDetails = %s WHERE propertyId = %s',
                (host_id, images, price, location, description, host_details, property_id))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Property updated successfully"})

@app.route('/api/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Property WHERE propertyId = %s', (property_id,))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Property deleted successfully"})

@app.route('/api/properties/<int:property_id>/images', methods=['GET'])
def get_property_images(property_id):
    # Implement logic to retrieve images associated with the property by propertyId
    # For example, if images are stored as comma-separated URLs, split the string and return the list.
    # If images are stored in a separate table, perform appropriate database queries.
    # You may return the list of image URLs as JSON in the response.
    return jsonify({"message": "Retrieve property images here"})

@app.route('/api/properties/<int:property_id>/images', methods=['POST'])
def add_property_image(property_id):
    # Implement logic to add a new image to the property by propertyId
    # For example, if images are stored as comma-separated URLs, update the property record in the database.
    # If images are stored in a separate table, insert the new image URL into the table.
    # You may return a success message in the response.
    return jsonify({"message": "Add property image here"})

if __name__ == '__main__':
    app.run(debug=True)
