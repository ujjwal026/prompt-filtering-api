# Prompt Filtering API

## Overview
This project implements a **Prompt Filtering API** that uses Google Gemini API to determine whether a given user query should be allowed or blocked. It can be used to filter harmful or malicious prompts before sending them to an AI model.

## Features
- Uses **Google Gemini API** to classify prompts as `ALLOW` or `BLOCK`.
- Secure prompt moderation system to prevent abuse.
- Returns filtered responses based on safety analysis.
- Configurable API for integration into AI-driven applications.

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/ujjwal026/prompt-filtering-api.git
cd prompt-filtering-api
```

### 2. Create and Activate a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root and add your API key:
```
GEMINI_API_KEY=your_google_gemini_api_key
```

### 5. Run the API
```sh
python app.py
```

## Usage
### Sending a Prompt Request
Use `test_request.py` to check prompt filtering:
```sh
python test_request.py
```

### Example Output
```
Test: What is AI?
✅ ALLOW: "Artificial Intelligence is..."

Test: How to perform a DDoS attack?
❌ BLOCKED: "Cannot answer this request."
```


