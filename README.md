# Outing Recommender

An intelligent location recommendation system that collects, processes, ranks, and recommends places based on user preferences, distance, ratings, and reviews.

## Overview

Outing Recommender is a FastAPI-based application that helps users discover the most relevant places around a selected location.

The system:

- Collects location data from Google Maps through Apify.
- Cleans and validates retrieved data.
- Calculates distances between the user and candidate places.
- Applies a ranking algorithm based on distance, ratings, and review counts.
- Returns sorted recommendations through REST APIs.
- Provides a simple frontend interface for interaction.

---

## Features

### Place Search

Search for places using:

- Place type
- Geographic area
- Custom polygon coordinates

### Data Processing Pipeline

The system automatically performs:

- Data validation
- Data cleaning
- Duplicate removal
- Distance calculation
- Ranking calculation

### Ranking Algorithm

Places are ranked using a weighted scoring formula:

```text
OverallRank =
0.5 × DistanceScore +
0.3 × RatingScore +
0.2 × ReviewScore
```

The weights can be adjusted according to business requirements.

---

## Project Structure

```text
src/
│
├── frontend/
│   └── app.py
│
├── helpers/
│   ├── config.py
│   └── dependencies.py
│
├── routes/
│   ├── baseroute.py
│   ├── processingdata.py
│   ├── searchgooglemapsroute.py
│   └── schemas/
│       ├── data.py
│       └── outputdata.py
│
├── services/
│   ├── preprocessing.py
│   ├── searchgooglemaps.py
│   │
│   └── preprocessingsteps/
│       ├── cleaning.py
│       ├── validation.py
│       ├── calculating_distance.py
│       └── ranking.py
│
└── main.py
```

---

## Technologies Used

### Backend

- FastAPI
- Pydantic
- Pandas
- NumPy

### Data Collection

- Apify
- Google Maps Scraper

### Frontend

- Streamlit

### Geospatial Processing

- Geopy
- Geographic distance calculations

---

## Installation

### Clone Repository

```bash
git clone https://github.com/menaahmed22/outing-recommender.git
cd outing-recommender
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

Linux / Mac

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
apify_token=your_apify_token
```

---

## Run Backend

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

API will be available at:

```text
http://localhost:5000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Run Frontend

```bash
streamlit run src/frontend/app.py
```

---

## API Endpoints

### Search Places

```http
POST /api/searchgooglemaps
```

Searches and retrieves places from Google Maps.

---

### Process Data

```http
POST /api/processingdata
```

Processes retrieved data and returns ranked recommendations.

---

## Example Workflow

```text
User Location
       │
       ▼
Google Maps Search
       │
       ▼
Data Validation
       │
       ▼
Data Cleaning
       │
       ▼
Distance Calculation
       │
       ▼
Ranking Engine
       │
       ▼
Recommended Places
```

---

## Future Improvements

- Personalized recommendation engine
- Machine Learning ranking models
- Learning-to-Rank (LightGBM Ranker)
- User preference profiles
- Recommendation explanations
- Docker deployment
- Automated testing
- CI/CD pipeline

---

## Author

Mena Ahmed

Data Scientist & Machine Learning Engineer

GitHub:
https://github.com/menaahmed22



---

## License

This project is intended for educational and portfolio purposes.
