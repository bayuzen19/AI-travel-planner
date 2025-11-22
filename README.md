# AI Travel Itinerary Planner

Plan a personalized day trip by simply telling the app your destination and interests.

---

## Features

- Input your destination city to plan a trip.
- Specify your interests (comma-separated) to customize your itinerary.
- AI-generated personalized day trip itinerary.
- Simple and elegant UI built with Streamlit.
- Quick tips to help you get the best travel plans.

---

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd ai_travel_agent
```

2. Install dependencies (preferably in a virtual environment):

```bash
pip install -r requirements.txt
```

---

## Usage

To run the app locally with Streamlit:

```bash
streamlit run app.py
```

The app will open in your browser. Enter the destination city and your interests, then submit the form to generate a personalized travel itinerary.

---

## Dependencies

- streamlit
- langchain
- langchain_core
- langchain_groq
- langchain_community
- python-dotenv

All dependencies are listed in `requirements.txt`.

---

## Docker and Kubernetes

This project includes a `dockerfile` and Kubernetes deployment configuration (`k8s-deployment.yaml`) for containerized deployment.

---

## Author

Bayuzen Ahmad

---

## Version

0.0.1
