# Outing Recommender

A FastAPI-based recommendation service that helps users discover nearby places based on location and category preferences using Google Maps data through Apify.

## Features

- Search for nearby places using latitude and longitude
- Filter by place category (restaurants, cafes, parks, etc.)
- FastAPI backend
- Streamlit frontend
- Google Maps data powered by Apify

---

## Project Structure

```text
src/
│
├── main.py
│
├── frontend/
│   └── app.py
│
├── helpers/
│   ├── config.py
│   └── dependencies.py
│
├── routes/
│   ├── base.py
│   ├── data.py
│   └── schemas/
│
└── services/
    └── searchgooglemaps.py
```

---

## Requirements

- Python 3.10+
- Apify Account
- Apify API Token

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

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

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
http://localhost:5000/docs
```

---

## Run Frontend

```bash
streamlit run frontend/app.py
```

---

## API Example

### Search Places

**POST**

```http
/api/search
```

Request Body:

```json
{
  "latitude": 31.2001,
  "longitude": 29.9187,
  "search_type": "restaurant"
}
```

Example Response:

```json
[
  {
    "name": "Restaurant A",
    "rating": 4.5,
    "address": "Alexandria, Egypt"
  }
]
```

---

## Technologies Used

- FastAPI
- Streamlit
- Apify
- Pydantic

---

## Future Improvements

- Authentication & Authorization
- Recommendation Engine
- Caching Layer (Redis)
- Rate Limiting
- Unit Testing
- Docker Support
- CI/CD Pipeline

---

## License

This project is licensed under the MIT License.
