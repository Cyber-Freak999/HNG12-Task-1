import requests
from app.utils import is_prime, is_perfect, is_armstrong, sum_of_digits


def classify_number(number: int):
    properties = []

    # Check Armstrong
    if is_armstrong(number):
        properties.append("armstrong")

    # Check even/odd
    properties.append("even" if number % 2 == 0 else "odd")

    # Fetch fun fact from Numbers API using "math" type
    fun_fact = fetch_fun_fact(number)

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum_of_digits(number),
        "fun_fact": fun_fact,
    }


def fetch_fun_fact(number: int) -> str:
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math")
        if response.status_code == 200:
            return response.text.strip()
        return "No fun fact available."
    except requests.exceptions.RequestException:
        return "Failed to fetch fun fact."
