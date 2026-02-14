# marketabra-qa-automation
UI &amp; API test automation for MarketAbra platform

### Stack:
Python, Pytest, Playwright, Requests
### Project Structure
```text
├── api/                # API Interaction Layer
│   └── auth_api.py     # Auth methods
├── data/               # Test Data
│   └── test_data.py    # BASE_URL, User credentials
├── pages/              # Page Object Model for UI automation(Planned)
├── tests_api/          # API Tests
│   └── test_auth.py    # Authentication tests
├── tests_ui/           # UI Tests (Planned)
├── conftest.py         # Pytest fixtures (Planned)
├── pytest.ini          # Pytest configuration (Planned)
├── README.md           # Project documentation
└── requirements.txt    # List of project dependencies (libraries)
```
### Setup and Installation
1. Clone the repository:
    `git clone https://github.com/mashaosipova-qa/marketabra-qa-automation.git`
2. Create a Virtual Environment:
    ##### Windows
    `python -m venv .venv
    .venv\Scripts\activate`
    ##### macOS/Linux
    `python3 -m venv .venv
    source .venv/bin/activate`
   
3. Install dependencies:
   `pip install --upgrade pip
    pip install -r requirements.txt`

