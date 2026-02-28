# marketabra-qa-automation
UI &amp; API test automation for MarketAbra platform

### Stack:
Python, Pytest, Playwright, Requests
### Project Structure
```text
├── allure_reports
├── api/
│   ├── clients/
│   │   ├── abra_client.py
│   │   └── postgres_client.py
│   ├── models/
│   │   ├── abra_model.py
│   │   ├── error_model.py
│   │   └── postgres_model.py
│   ├── test_data/
│   └── tests/
│       ├── conftest.py
│       └── sign_in_test.py
├── ui/
│   ├── data/
│   ├── pages/
│   └── tests/
├── utils/
│   ├── allure_helper.py
│   ├── common_checker.py
│   ├── generator.py
│   └── http_client.py
├── results/
├── .env
├── .gitignore
├── config.py
├── pytest.ini
├── README.md
└── requirements.txt          
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
### Execution and Reporting
Follow these steps to run tests and view results via the Terminal:
##### 1. Launch tests
Use this command to execute tests and collect reporting data. It automatically cleans the results folder before the launch.

`pytest {path_to_test_file} -v --alluredir results --clean-alluredir`

for examle:
`pytest api/tests/sign_in_test.py -v --alluredir results --clean-alluredir`

##### 2. Open the report
After the tests are finished, generate and open the visual HTML report in your default browser.

`allure serve results`



