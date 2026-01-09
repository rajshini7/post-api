# API Automation Framework – Pytest + Newman

## OVERVIEW
This project is a **robust API automation testing framework** built using **Python (Pytest)** and **Postman/Newman**, designed to validate RESTful APIs end-to-end.

It supports:
- CRUD API validation (POST, GET, PUT, PATCH, DELETE)
- Header and authentication validation
- Data-driven testing
- HTML reporting
- CI/CD execution with GitHub Actions
- Parallel and scalable execution

The framework is currently integrated with **JSONPlaceholder** as a mock API and is **production-ready** for real backend services.

---

## WHY THIS PROJECT
Modern backend systems rely heavily on APIs. This project demonstrates:

- How to design **clean, maintainable API automation**
- Separation of concerns (client, payloads, tests)
- Real-world CI/CD readiness
- Industry-standard tooling (Pytest, Newman, GitHub Actions)

This framework is suitable for:
- Backend API testing
- Regression testing
- CI validation before deployments
- Interview demonstrations for QA / SDET / Backend roles

---

## CORE CONCEPTS
- **API Client Abstraction** – Centralized HTTP handling
- **Reusable Payload Builders** – No hardcoded data
- **Pytest Fixtures** – Shared setup & teardown
- **Assertions at API Contract Level**
- **HTML Reporting** – Pytest + Newman
- **CI/CD Execution** – Automated on every push

---

## TECH STACK
### Programming & Testing
- Python 3.11+ / 3.14 compatible
- Pytest
- Requests

### Reporting
- pytest-html
- Newman HTML Extra Reporter

### API Tooling
- Postman Collection
- Newman (CLI runner)

### CI/CD
- GitHub Actions (Ubuntu runner)
- Node.js 18 (for Newman)

---

## FOLDER STRUCTURE
post-api/
│
├── client/
│ └── api_client.py # Central API request handler
│
├── data/
│ └── payloads.py # Request payload builders
│
├── tests/
│ └── test_posts_crud.py # CRUD API test cases
│
├── postman/
│ ├── CRUD_VAL.postman_collection.json
│ └── JSONplaceholder.postman_environment.json
│
├── reports/
│ └── pytest-report.html # Pytest HTML report
│
├── newman-report/
│ └── newman.html # Newman HTML report
│
├── .github/workflows/
│ └── api-tests.yml # CI pipeline
│
├── conftest.py # Pytest fixtures
├── pytest.ini # Pytest configuration
├── requirements.txt # Python dependencies
├── package.json # Node dependencies (Newman)
├── .gitignore
└── README.md


---

## HOW TO EXECUTE (LOCAL)
post-api/
│
├── client/
│ └── api_client.py # Central API request handler
│
├── data/
│ └── payloads.py # Request payload builders
│
├── tests/
│ └── test_posts_crud.py # CRUD API test cases
│
├── postman/
│ ├── CRUD_VAL.postman_collection.json
│ └── JSONplaceholder.postman_environment.json
│
├── reports/
│ └── pytest-report.html # Pytest HTML report
│
├── newman-report/
│ └── newman.html # Newman HTML report
│
├── .github/workflows/
│ └── api-tests.yml # CI pipeline
│
├── conftest.py # Pytest fixtures
├── pytest.ini # Pytest configuration
├── requirements.txt # Python dependencies
├── package.json # Node dependencies (Newman)
├── .gitignore
└── README.md


---

## HOW TO EXECUTE (LOCAL)

post-api/
│
├── client/
│ └── api_client.py # Central API request handler
│
├── data/
│ └── payloads.py # Request payload builders
│
├── tests/
│ └── test_posts_crud.py # CRUD API test cases
│
├── postman/
│ ├── CRUD_VAL.postman_collection.json
│ └── JSONplaceholder.postman_environment.json
│
├── reports/
│ └── pytest-report.html # Pytest HTML report
│
├── newman-report/
│ └── newman.html # Newman HTML report
│
├── .github/workflows/
│ └── api-tests.yml # CI pipeline
│
├── conftest.py # Pytest fixtures
├── pytest.ini # Pytest configuration
├── requirements.txt # Python dependencies
├── package.json # Node dependencies (Newman)
├── .gitignore
└── README.md

### 1. Clone the Repository
```bash
git clone https://github.com/rajshini7/pytest-postman-api-testing.git
cd post-api

### 2. Create Virtual Environment
python -m venv .venv
.\.venv\Scripts\activate   # Windows

### 3. Install Python Dependencies
pip install -r requirements.txt

### 4. Run Pytest API Tests
pytest -v -s \
--html=reports/pytest-report.html \
--self-contained-html

### 5. Install Newman & Reporter
npm install -g newman newman-reporter-htmlextra

6. Run Postman Collection via Newman
newman run postman/CRUD_VAL.postman_collection.json ^
-e postman/JSONplaceholder.postman_environment.json ^
--reporters cli,htmlextra ^
--reporter-htmlextra-export newman-report/newman.html

###CI/CD READY

This project is fully CI/CD enabled using GitHub Actions.

Pipeline Features

Triggered on push & PR to development

Installs Python & Node dependencies

Runs Pytest API tests

Runs Newman collection

Uploads reports as artifacts

CI Artifacts

pytest-report.html

newman.html

You can download these directly from the GitHub Actions → Artifacts section.

###EXPECTED OUTPUT

✅ All CRUD API tests passing

📄 Pytest HTML Report (detailed assertions)

📄 Newman HTML Report (Postman execution summary)

🚀 CI pipeline green on GitHub

### BRANCHING STRATEGY
main
 ├── staging
 └── development


development → Active development & testing

staging → Pre-release validation

main → Production-ready code only

Direct pushes to main are intentionally restricted.

###CREATED BY

Rajeev S
API Automation & Python Enthusiast
Bengaluru, India

