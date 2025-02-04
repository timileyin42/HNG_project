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

def get_fun_fact(n):
    url = f"http://numbersapi.com/{n}/math"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        pass
    return "No fun fact available."

# API Endpoint
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    # Ensure number is valid
    if number is None:
        return jsonify({
            "error": True,
            "message": "Number parameter is required",
            "number": None
        }), 400  

    try:
        number = float(number)  # Convert input to float
        int_part = int(number)  # Extract integer part
    except (ValueError, TypeError):
        return jsonify({
            "error": True,
            "message": "Invalid number format",
            "number": number  # Include the invalid input
        }), 400  # Return 400 only for invalid input

    # Determine properties
    properties = ["even" if int_part % 2 == 0 else "odd"]
    if int_part < 0:
        properties.append("negative")

    response = {
        "number": number,  # Show the original float number
        "integer_part": int_part,  # Show the extracted integer part
        "is_prime": bool(is_prime(int_part)),  # Ensure boolean output
        "is_perfect": bool(is_perfect(int_part)),  # Ensure boolean output
        "properties": properties,  # Ensure properties is an array
        "digit_sum": sum(int(d) for d in str(abs(int_part))),  # Ensure numeric output
        "fun_fact": str(get_fun_fact(int_part))  # Ensure string output
    }

    return jsonify(response), 200  # Always return 200 for valid input

# Run the App
if __name__ == '__main__':
    app.run(debug=True)

