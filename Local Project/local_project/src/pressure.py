from flask import Flask, request, jsonify
import socket

PORT = 8000
app = Flask(__name)
counter = 0



def getAll():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('172.20.10.2', PORT))
    sock.send(b"GET_ALL")

    response = sock.recv(4096)
    sock.close()
    print(response)
    print(response.decode())
    
    return response.decode()

@app.route('/update-indicator', methods=['POST'])
def update_indicator():
    indicator = getAll()
    print(indicator)
    global indicatorCount
    data = request.get_json()
    
    if "sensor_value" in data:
        sensor_value = data["sensor_value"]
        
        if sensor_value > 0:
            indicatorCount = 1
        else:
            indicatorCount = 0  # Reset the count if sensor value is not greater than 0

    return 'OK'

@app.route('/get-indicator-count', methods=['GET'])
def get_indicator_count():
    return jsonify({"indicatorCount": indicatorCount})

if __name__ == '__main__':
    app.run(host='172.20.10.2', port=8000)