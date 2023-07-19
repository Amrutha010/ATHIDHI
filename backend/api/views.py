# backend/api/views.py

from flask import Blueprint, jsonify, request
from models import db, Host, Property, Guest, Booking

api_bp = Blueprint('api', __name__)

# Implement CRUD operations for Host, Property, Guest, and Booking here.
# For example, a basic implementation of getting all hosts might look like this:

@api_bp.route('/hosts', methods=['GET'])
def get_hosts():
    hosts = Host.query.all()
    host_data = []
    for host in hosts:
        host_data.append({
            'hostId': host.hostId,
            'HostName': host.HostName,
            'hostStatus': host.hostStatus,
            'Location': host.Location,
            'About': host.About,
            'HostingSince': host.HostingSince.strftime('%Y-%m-%d')
        })
    return jsonify(host_data)
