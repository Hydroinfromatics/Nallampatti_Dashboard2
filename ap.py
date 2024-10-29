from flask import Flask, jsonify, render_template_string
from datetime import datetime
from data_process import process_and_store_data, get_todays_data
import os

app = Flask(__name__)

# Configuration
API_URL = os.environ.get('API_URL', 'default_api_url')

# Simple HTML template for the root route
HOME_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Sensor Data API</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .endpoint { background: #f4f4f4; padding: 10px; margin: 10px 0; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>Sensor Data API Endpoints</h1>
    <div class="endpoint">
        <h3>GET /</h3>
        <p>This page - API documentation</p>
    </div>
    <div class="endpoint">
        <h3>GET /health</h3>
        <p>Health check endpoint</p>
    </div>
    <div class="endpoint">
        <h3>GET /update_data</h3>
        <p>Trigger data update from sensors</p>
    </div>
    <div class="endpoint">
        <h3>GET /sensor_data</h3>
        <p>Get today's sensor data</p>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    """Root route - shows available endpoints"""
    return render_template_string(HOME_TEMPLATE)

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/update_data')
def update_data():
    """Update sensor data endpoint"""
    try:
        process_and_store_data(API_URL)
        return jsonify({
            "status": "success",
            "message": "Data updated successfully",
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/sensor_data')
def get_sensor_data():
    """Get sensor data endpoint"""
    try:
        data = get_todays_data()
        if data.empty:
            return jsonify({
                "status": "success",
                "message": "No data available for today",
                "data": []
            })
        
        json_data = data.to_dict(orient='records')
        return jsonify({
            "status": "success",
            "count": len(json_data),
            "data": json_data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return jsonify({
        "status": "error",
        "message": "The requested URL was not found",
        "error_code": 404
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        "status": "error",
        "message": "An internal server error occurred",
        "error_code": 500
    }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)