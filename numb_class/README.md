# Number Classification API

This is a **Number Classification API** built using Python and Flask. It takes a number as input and returns interesting mathematical properties about the number, along with a fun fact fetched from the [Numbers API](http://numbersapi.com/).

---

## Features
- **Mathematical Properties**:
  - Checks if the number is **prime**.
  - Checks if the number is a **perfect number**.
  - Checks if the number is an **Armstrong number**.
  - Determines if the number is **odd** or **even**.
  - Calculates the **sum of its digits**.
- **Fun Fact**:
  - Fetches a fun fact about the number from the Numbers API.
- **Error Handling**:
  - Handles invalid inputs (e.g., non-numeric values) and returns appropriate error messages.

---

## API Endpoint

### Request

GET /api/classify-number?number=<number>

`
### Parameters
- `number` (required): The number to classify. Must be a valid integer.

### Example Request

GET /api/classify-number?number=371


### Example Response (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is a narcissistic number, since 3^3 + 7^3 + 1^3 = 371."
}

## Example Response (400 Bad Request)
{
    "number": "abc",
    "error": true
}

## Setup and Installation

### Prerequisites

Python 3.8 or higher

pip (Python package manager)

### steps

git clone git@github.com:timileyin42/HNG_project.git
cd numb_class

### Set Up a Virtual Environment:

python -m venv myenv
source myvenv/bin/activate

### Install Dependencies:

pip install -r requirements.txt

### Run the API:

python app.py

# Testing

### Run Unit Tests

To ensure the API works as expected, run the included unit tests:

python -m unittest test_app.py


# Deployment

### Deploy to Render
Create a render.yaml file:

services:
  - type: web
    name: number-classification-api
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: python app.py

## Technologies Used

Python: Programming language.

Flask: Web framework for building the API.

Requests: Library for making HTTP requests to the Numbers API.

unittest: Framework for writing and running unit tests.

## Acknowledgments

- [Numbers API](http://numbersapi.com) for providing fun facts about numbers.
- Flask and Python communities for their excellent documentation and resources.

