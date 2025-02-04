from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Helper Functions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n):
    digits = [int(d) for d in str(abs(n))]
    length = len(digits)
    return sum(d**length for d in digits) == abs(n)

def get_fun_fact(n):
    url = f"http://numbersapi.com/{n}/math"
    response = requests.get(url)
    return response.text if response.status_code == 200 else "No fun fact available."

# API Endpoint
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    try:
        number = float(number)  # Convert input to float
    except (ValueError, TypeError):
        return jsonify({"error": True, "message": "Invalid number format", "number": number}), 200  # Always return 200

    int_part = int(number)  # Extract integer part (e.g., 3.14 → 3, -7.89 → -7)

    # Determine properties
    properties = ["even" if int_part % 2 == 0 else "odd"]

    response = {
        "number": number,  # Show the original float number
        "integer_part": int_part,  # Show the extracted integer part
        "is_prime": is_prime(int_part),
        "is_perfect": is_perfect(int_part),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(abs(int_part))),
        "fun_fact": get_fun_fact(int_part)
    }
    
    return jsonify(response), 200  # Always return 200

# Run the App
if __name__ == '__main__':
    app.run(debug=True)

