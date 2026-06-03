from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Assignment 3 API running"}

@app.route("/health")
def health():
    return {"service": "flask-api", "status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
