#!/usr/bin/env python3

from flask import Flask, jsonify, render_template
import wakeonlan
import dotenv
import os

app = Flask(__name__)
app.config['']

dotenv.load_dotenv()
MAC_ADDRESS = os.getenv('MAC_ADDRESS')
PORT = os.getenv('PORT')

# API endpoint to send wake-on-LAN packet to hardcoded host
@app.route('/api/wol', methods=['GET'])
def wake_on_lan():
    try:
        # Send wake-on-LAN packet to host
        wakeonlan.send_magic_packet(MAC_ADDRESS)
        print("Sending WOL to " + MAC_ADDRESS)
        return jsonify({'message': 'Wake-on-LAN packet sent successfully.'})
    except Exception as e:
        return jsonify({f'message': 'Failed to send wake-on-LAN packet: {e}'}), 500

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')