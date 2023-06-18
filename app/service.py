from flask import Flask
import socket
import datetime
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# static information as metric
metrics.info('app_info', 'Application info', version='1.0')

@app.route('/', methods=['GET'])
def get_details():
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Get the hostname
    hostname = socket.gethostname()
    # Create the response string
    response = f"Timestamp: {timestamp} \nHostname: {hostname}" 
    # Return the response
    return response

if __name__ == '__main__':
    app.run()