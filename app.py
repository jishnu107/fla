from flask import Flask, jsonify, request

app = Flask(__name__)

def add_numbers(a, b):
    """Helper function to add two numbers, raising TypeError if not numeric."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    return a + b

@app.route('/')
def home():
    return jsonify({"status": "healthy", "message": "Python Flask App is running!"})

@app.route('/add', methods=['GET'])
def add():
    try:
        a_str = request.args.get('a')
        b_str = request.args.get('b')
        
        if a_str is None or b_str is None:
            return jsonify({"error": "Missing parameters 'a' and 'b'"}), 400
            
        a = float(a_str)
        b = float(b_str)
        result = add_numbers(a, b)
        return jsonify({"a": a, "b": b, "result": result})
    except ValueError:
        return jsonify({"error": "Parameters must be numeric values"}), 400
    except TypeError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
