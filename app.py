#a basic flask application to demo logger
from flask import Flask
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@app.route("/")
def home():
    logging.info("Home page accessed")
    return "Hello, Logging!"

if __name__ == "__main__":
    app.run(debug=True)
