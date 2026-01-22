from flask import Flask, jsonify

# Create Flask app
app = Flask(__name__)

# Health check endpoint (for ECS / ALB)
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "ecs-backend"
    })

# Sample API endpoint
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({
        "message": "Hello from ECS Full Stack CI/CD 🚀"
    })

# Start the server
if __name__ == "__main__":
    print("Starting backend server on port 5000...")
    app.run(host="0.0.0.0", port=5000)
