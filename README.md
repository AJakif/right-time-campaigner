# Right Time Campaigner

This project is the Software Requirements Specification (SRS) for the Right Time Campaigner system.

## 1.1 Purpose

This system is designed to help marketers and businesses generate personalized, data-driven marketing campaigns across multiple communication channels, by connecting to various data sources and simulating real-time streaming of intelligent campaign recommendations.

The system will output a structured JSON payload representing the right time, right channel, right message, and right audience, suitable for execution across connected marketing platforms.

## Project Structure

right-time-campaigner/
├── backend/
│   ├── main.py
│   └── requirements.txt
├── .gitignore
└── README.md

## Running the Project

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

4. Access the API documentation at `http://localhost:8000/docs`.