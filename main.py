from flask import Flask

app = Flask(__name__)

FLAG = "CYBERUS{First_Flag!!!}"

@app.route("/")
def index():
    return f"<h1>Hello Challenger!</h1><p>Your flag is: {FLAG}</p>"

# simple health endpoint used by some platforms (IGNORE)
@app.route("/health")
def health():
    return "OK", 200
