# AI Email Assistant

A Streamlit prototype that classifies a submitted email as important, casual, or spam, then drafts a concise reply with a sequential CrewAI workflow.

## Requirements

- Python
- An API key for the configured OpenAI-compatible model endpoint

## Setup

1. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

2. Set `OPENAI_API_KEY` in your environment. The app defaults to the Groq-compatible API endpoint; set `OPENAI_API_BASE` and `OPENAI_MODEL_NAME` to override the endpoint or model.

3. Start the app:

   ```bash
   streamlit run app.py
   ```

Email text is sent to the configured model provider. Use non-sensitive sample content and review generated classifications and replies before relying on them.
