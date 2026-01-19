# API Automation Framework – Pytest + Newman

## OVERVIEW
This project is a **robust API automation testing framework** built using **Python (Pytest)** and **Postman/Newman**, designed to validate RESTful APIs end-to-end.

It supports:
- CRUD API validation (POST, GET, PUT, PATCH, DELETE)
- Centralized API client abstraction
- Reusable payload builders (no hardcoding)
- HTML reporting (Pytest & Newman)
- CI/CD execution using GitHub Actions

The framework currently uses **JSONPlaceholder** as a mock API and is **production-ready** for real backend services.

---

## WHY THIS PROJECT
Modern applications rely heavily on APIs. This project demonstrates:
- Clean API automation architecture
- Separation of concerns (client, payloads, tests)
- CI/CD-ready test execution
- Industry-standard tools used

Suitable for:
- API regression testing
- Backend validation
- CI quality gates
- Interview and portfolio demonstration

---

## CORE CONCEPTS
- **API Client Abstraction**
- **Reusable Payload Builders**
- **Pytest Fixtures**
- **Contract-level Assertions**
- **HTML Reporting**
- **Automated CI Execution**

---

## TECH STACK
### Programming & Testing
- Python 3.11+ (compatible up to 3.14)
- Pytest
- Requests

### Reporting
- pytest-html
- Newman HTML Extra Reporter

### API Tooling
- Postman
- Newman

### CI/CD
- GitHub Actions
- Node.js 18

---

## FOLDER STRUCTURE
```text
post-api/
├── client/
│   └── api_client.py
├── data/
│   └── payloads.py
├── tests/
│   └── test_posts_crud.py
├── postman/
│   ├── CRUD_VAL.postman_collection.json
│   └── JSONplaceholder.postman_environment.json
├── reports/
│   └── pytest-report.html
├── newman-report/
│   └── newman.html
├── .github/
│   └── workflows/
│       └── api-tests.yml
├── conftest.py
├── pytest.ini
├── requirements.txt
├── package.json
├── .gitignore
└── README.md
```

---

## HOW TO EXECUTE (LOCAL)

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
pytest -v -s --html=reports/pytest-report.html --self-contained-html
```

---

## POSTMAN / NEWMAN EXECUTION

```bash
npm install -g newman newman-reporter-htmlextra
newman run postman/CRUD_VAL.postman_collection.json \
  -e postman/JSONplaceholder.postman_environment.json \
  --reporters "cli,htmlextra" \
  --reporter-htmlextra-export "newman-report/newman.html"
```

---

## CI/CD READY
- Runs on every push & PR to `development`
- Executes Pytest and Newman
- Uploads HTML reports as CI artifacts

---

## EXPECTED OUTPUT
- Passing CRUD API tests
- Pytest HTML report
- Newman HTML report
- Green CI pipeline

---

## BRANCHING STRATEGY
```text
main
├── staging
└── development
```

---

## CREATED BY
**Rajeev S**  
API Automation & Python Enthusiast  
Bengaluru, India
