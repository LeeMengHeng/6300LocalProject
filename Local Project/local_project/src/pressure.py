from flask import Flask, request, jsonify

app = Flask(__name)
counter = 0

@app.route('/update-indicator', methods=['POST'])
def update_indicator():
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
    app.run(host='0.0.0.0', port=5000)