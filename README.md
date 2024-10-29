# Nallampatti_Dashboard2
# Sensor Data API

A Flask-based REST API for collecting and serving sensor data. This application fetches data from sensors, processes it, and provides endpoints to access the processed data.

## Features

- Real-time sensor data collection
- Data processing and storage
- RESTful API endpoints
- Deployed on Render
- Health monitoring

## Tech Stack

- Python 3.x
- Flask (Web Framework)
- Pandas (Data Processing)
- Gunicorn (WSGI HTTP Server)
- Render (Deployment Platform)

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API documentation and available endpoints |
| `/health` | GET | Health check endpoint |
| `/update_data` | GET | Trigger sensor data update |
| `/sensor_data` | GET | Retrieve today's sensor data |

## Local Setup

1. Clone the repository
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set environment variables
```bash
# On Unix/macOS:
export API_URL='your-sensor-api-url'

# On Windows:
set API_URL=your-sensor-api-url
```

5. Run the application
```bash
python app.py
```

## Deployment on Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure the service:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Add environment variables:
   - `API_URL`: Your sensor API endpoint

## API Response Examples

### Health Check
```json
{
    "status": "healthy",
    "timestamp": "2024-10-29T10:00:00"
}
```

### Sensor Data
```json
{
    "status": "success",
    "count": 24,
    "data": [
        {
            "timestamp": "2024-10-29T10:00:00",
            "pH": 7.2,
            "TDS": 450,
            "Depth": 12.5,
            "FlowInd": 25.3
        }
    ]
}
```

## File Structure
```
project/
├── app.py               # Main Flask application
├── data_process.py      # Data processing logic
├── get_data.py         # API fetch logic
├── requirements.txt    # Project dependencies
└── README.md          # Documentation
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| API_URL | Sensor API endpoint URL | Yes |
| PORT | Application port (default: 5000) | No |

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Successful request
- 404: Endpoint not found
- 500: Internal server error

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Your License Type] - See LICENSE file for details

## Contact

[Your Contact Information]
