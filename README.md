# InsightStream Real-Time Sentiment Analysis and Visualization

## Overview
InsightStream is a sophisticated platform designed to perform real-time sentiment analysis and visualization, providing businesses and researchers with actionable insights from textual data. By leveraging FastAPI, InsightStream offers a seamless interface for analyzing sentiment scores from text inputs and visualizing these trends over time. Users can input text data to receive sentiment scores instantly, view historical sentiment trends, and explore data through an intuitive web interface. This tool is particularly beneficial for data analysts, social media managers, and anyone interested in understanding public sentiment dynamics.

## Features
- **Real-Time Sentiment Analysis**: Instantly analyze text inputs and receive sentiment scores categorized as positive, negative, or neutral.
- **Historical Trend Visualization**: Visualize sentiment trends over time, with detailed breakdowns of positive, negative, and neutral counts.
- **Interactive Dashboard**: Engage with a user-friendly dashboard that visually represents sentiment data and trends.
- **Comprehensive API Documentation**: Integrate sentiment analysis capabilities into other applications with ease using detailed API documentation.
- **Responsive Design**: Access the application seamlessly across various devices with a fully responsive interface.
- **Mock Data for Testing**: Explore the features immediately using pre-loaded mock data without any initial setup.

## Tech Stack
| Technology  | Description                          |
|-------------|--------------------------------------|
| Python 3.11+| Programming language                 |
| FastAPI     | Web framework for building APIs      |
| Uvicorn     | ASGI server for running FastAPI apps |
| Jinja2      | Templating engine for HTML           |
| SQLite3     | Lightweight database engine          |
| Pydantic    | Data validation library              |
| Docker      | Containerization platform            |

## Architecture
The InsightStream application is structured to provide a cohesive flow of data from the backend to the frontend. The backend, built with FastAPI, handles API requests, processes sentiment analysis, and interacts with the SQLite database. The frontend, served using Jinja2 templates, provides a dynamic and interactive user interface.

```
+-------------------+
|   Frontend (UI)   |
|-------------------|
| HTML/CSS/JS       |
| Jinja2 Templates  |
+-------------------+
        |
        v
+-------------------+
|   FastAPI Server  |
|-------------------|
| API Endpoints     |
| Sentiment Logic   |
+-------------------+
        |
        v
+-------------------+
|   SQLite Database |
|-------------------|
| SentimentAnalysis |
| TrendData         |
+-------------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)
- Docker (optional for containerization)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/insightstream-real-time-sentiment-analysis-and-vis-auto.git
   cd insightstream-real-time-sentiment-analysis-and-vis-auto
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the FastAPI application:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```
2. Visit `http://localhost:8000` in your web browser to access the application.

## API Endpoints
| Method | Path              | Description                                   |
|--------|-------------------|-----------------------------------------------|
| GET    | `/`               | Returns the home page                         |
| GET    | `/dashboard`      | Returns the dashboard page                    |
| GET    | `/api-docs`       | Returns the API documentation page            |
| GET    | `/about`          | Returns the about page                        |
| GET    | `/contact`        | Returns the contact page                      |
| GET    | `/api/sentiment`  | Retrieves all sentiment analysis records      |
| GET    | `/api/trends`     | Retrieves sentiment trend data                |
| POST   | `/api/analyze`    | Analyzes sentiment for provided text          |

## Project Structure
```
insightstream-real-time-sentiment-analysis-and-vis-auto/
├── app.py                  # Main application file with FastAPI setup
├── Dockerfile              # Docker configuration for containerization
├── requirements.txt        # Project dependencies
├── start.sh                # Shell script for starting the application
├── static/
│   ├── css/
│   │   └── style.css       # Stylesheet for the application
│   └── js/
│       └── main.js         # JavaScript for frontend interactivity
├── templates/
│   ├── about.html          # About page template
│   ├── api_docs.html       # API documentation page template
│   ├── contact.html        # Contact page template
│   ├── dashboard.html      # Dashboard page template
│   └── index.html          # Home page template
└── insightstream.db        # SQLite database file
```

## Screenshots
*Screenshots of the application interface and features will be placed here.*

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t insightstream .
   ```
2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 insightstream
   ```

## Contributing
We welcome contributions from the community! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the existing style and passes all tests.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---
Built with Python and FastAPI.
