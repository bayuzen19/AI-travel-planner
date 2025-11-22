# AI Travel Itinerary Planner

AI Travel Itinerary Planner builds AI-generated, personalized day-trip plans from a simple city name and a short list of interests. The app exposes a Streamlit UI that talks to a small planner layer which uses a Groq LLM (via `langchain_groq`) to generate friendly human-readable itineraries.

---

## Quick highlights

- Enter a city and comma-separated interests (e.g. `coffee, art museum, street food`) and get a concise, bullet-style day itinerary.
- Single-page Streamlit UI (`app.py`) for fast local testing and demoing.
- Small, maintainable code structure: planner core, prompt/chain logic, and configuration.

---

## Architecture (end-to-end)

1. The user fills the form in the Streamlit app (`app.py`).
2. `app.py` builds a `TravelPlanner` instance from `src/core/planner.py` and sets the `city` and `interests`.
3. `TravelPlanner.create_itineary()` calls `generate_itineary` in `src/chains/itinerary_chain.py`.
4. `itinerary_chain` formats a prompt and invokes a Groq chat model via `langchain_groq.ChatGroq` using the `GROQ_API_KEY` env var.
5. The returned text is shown back to the user in the Streamlit UI.

This flow is intentionally small and synchronous for clarity — you can later swap the LLM, add caching, or move generation into a background worker.

---

## Files & folders

- `app.py` — Streamlit app entrypoint and UI layout.
- `requirements.txt` — Python dependencies.
- `dockerfile`, `k8s-deployment.yaml` — container & deployment scaffolding.
- `src/` — core application code:
	- `src/core/planner.py` — `TravelPlanner` class that prepares messages and calls the chain.
	- `src/chains/itinerary_chain.py` — LLM wrapper, prompt template, and `generate_itineary` function.
	- `src/config/config.py` — environment config (loads `GROQ_API_KEY`).
	- `src/utils/` — helpers including `logger.py` and `custom_exception.py`.

---

## Requirements

The main dependencies are in `requirements.txt`. Key packages used:

- `streamlit` — UI
- `langchain`, `langchain_core`, `langchain_groq`, `langchain_community` — LLM + prompt tooling
- `python-dotenv` — load `.env` configuration

Install them with:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## Environment variables

Create a `.env` file at the project root with at least the Groq API key used by the Groq LLM client in `src/chains/itinerary_chain.py`:

```
GROQ_API_KEY=your_groq_api_key_here
```

If the key is missing the app will fail when the chain tries to call the model.

---

## Run locally (development)

1. Activate your virtual environment and install requirements (see above).
2. Add `.env` with `GROQ_API_KEY`.
3. Run Streamlit:

```powershell
streamlit run app.py
```

Open the URL printed by Streamlit (usually `http://localhost:8501`) and try the UI.

Example inputs:

- City: `Paris`
- Interests: `history, coffee, hidden gems`

---

## Docker / Deployment

There is a `dockerfile` and `k8s-deployment.yaml` included for containerized deployment. Basic steps (example):

```powershell
docker build -t ai-travel-planner:latest .
docker run -e GROQ_API_KEY="your_key" -p 8501:8501 ai-travel-planner:latest
```

For Kubernetes, update `k8s-deployment.yaml` with your container image and secrets (do NOT store API keys in plain YAML — prefer secrets or a secret manager).

---

## Logging & error handling

- `src/utils/logger.py` provides the logger used across the app.
- `src/utils/custom_exception.py` wraps and surfaces errors from the planner.

If generation fails, the app surfaces a friendly warning in the UI and logs the error locally.

---

## Troubleshooting

- Missing `GROQ_API_KEY`: create `.env` or set `GROQ_API_KEY` in your environment.
- Model invocation errors: check network access and API key quota.
- If Streamlit page doesn't update, restart the app after making code changes.

---

## Next steps / improvements

- Add unit tests for the planner and chain functions.
- Add caching for repeated requests or a simple rate limiter.
- Add CI to run linting and tests on push.
- Add more configurable prompts and temperature control in `itinerary_chain`.

---

## Contributing

1. Fork the repo and create a branch.
2. Add tests and make changes.
3. Open a PR and describe your changes.

---

## Author

Bayuzen Ahmad

---

## License

This project does not include a license file. Add one (e.g., MIT) if you plan to publish it.
