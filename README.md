# marketabra-qa-automation
UI &amp; API test automation for MarketAbra platform

### Stack:
Python, Pytest, Playwright, Requests
### Project Structure
```text
├── api/                        
│   ├── data/                   
│   │   └── settings.py          
│   ├── services/              
│   │   └── auth_api.py        
│   ├── tests/                 
│   │   └── test_auth.py       
│   └── conftest.py             
├── ui/                        
│   ├── data/                 
│   ├── pages/                
│   ├── tests/                 
│   └── conftest.py             
├── .gitignore                  
├── LICENSE                    
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

