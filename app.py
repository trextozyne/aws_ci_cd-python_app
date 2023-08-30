from flask import Flask, Response
import os

app = Flask(__name__)

@app.route("/")
def hello():
    # ... (Your existing route code)
    return content

@app.route("/healthz")
def health_check():
    return Response("OK", status=200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 80)))
