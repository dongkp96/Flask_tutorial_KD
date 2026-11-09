from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world from Flask 2"

@app.route("/about")
def about():
    return "This is the about page"

@app.route("/contact")
def contact():
    return "This is the contact page"

@app.route("/user/<name>")
def user(name):
    return f"This is {name}'s page"

@app.route("/user/<name>/<bio>")
def user_bio(name, bio):
    return f"This is {name}'s {bio}"

if __name__ == "__main__":
    app.run(debug=True)