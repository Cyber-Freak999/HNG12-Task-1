# Number Classification API (HNG 12 Task 1)

## Overview
This is a RESTful API that takes a number as input and returns interesting mathematical properties about it, along with a fun fact retrieved from the Numbers API.

## Features
- Classifies numbers as **Armstrong**, **Odd**, or **Even**.
- Checks if a number is **prime** or **perfect**.
- Computes the **sum of digits** of the number.
- Fetches a **fun fact** from the Numbers API.
- Returns data in **JSON format**.
- Handles invalid inputs gracefully with proper error messages.

## Tech Stack
- **Language:** Python
- **Framework:** FastAPI
- **Web Server:** Uvicorn
- **External API:** Numbers API

## API Endpoint
### **GET /api/classify-number**
#### **Query Parameters:**
| Parameter  | Type   | Description                        |
|------------|--------|------------------------------------|
| number     | int    | The number to classify            |

#### **Example Request:**
```bash
curl -X GET "http://your-domain.com/api/classify-number?number=371"
```

#### **Example Response (200 OK):**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### **Error Response (400 Bad Request):**
```json
{
    "number": "abc",
    "error": true
}
```

## Installation & Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Cyber-Freak999/HNG12-Task-1.git
   cd HNG12-Task-1
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the API:**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

5. **Test the API:**
   Open a browser or use `curl` to test:
   ```bash
   curl -X GET "http://127.0.0.1:8000/api/classify-number?number=371"
   ```

## License
This project is licensed under the MIT License.


