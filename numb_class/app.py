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
    n_abs = abs(n)  # Handle negative numbers
    digits = [int(d) for d in str(n_abs)]
    length = len(digits)
    return sum(d**length for d in digits) == n_abs

def get_fun_fact(n):
    url = f"http://numbersapi.com/{n}/math"
    response = requests.get(url)
    return response.text if response.status_code == 200 else "No fun fact available."

# API Endpoint
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    
    # Validate input
    try:
        # Convert input to float (handles both integers and floating-point numbers)
        number = float(number)
    except (ValueError, TypeError):
        # Return 400 for invalid inputs (e.g., non-numeric values)
        return jsonify({"number": number, "error": True}), 400

    # Determine properties
    properties = []
    if is_armstrong(int(number)):  # Check Armstrong for integers only
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    response = {
        "number": number,
        "is_prime": is_prime(int(number)),
        "is_perfect": is_perfect(int(number)),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(abs(int(number)))),
        "fun_fact": get_fun_fact(int(number))
    }
    return jsonify(response), 200

# Run the App
if __name__ == '__main__':
    app.run(debug=True)
