from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Python Webpage</h1><p>This is a sample index page.</p>"

if __name__ == "__main__":
    app.run(debug=True)
