from flask import Flask, render_template, request, redirect, url_for, render_template_string
app = Flask(__name__)

@app.route("/")
def home():
    name = "Kumon"
    info = {
        "age":18,
        "gender": "M"
    }
    return render_template("index.html", title="Home page", name=name, 
                           info = info) 

@app.route("/about")
def about():
    descriptions = {
        "hobbies": ["soccer", "gaming", "gooning"],
        "courses": ["Math", "Chemistry"]
    }
    return render_template("about.html", title="About page", descriptions=descriptions)

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logged_in", methods= ['POST'])
def logged_in():
    username = request.form.get("username")
    password = request.form.get("password")
    return render_template("logged_in.html", username= username,
                            password = password)


@app.route("/file_upload", methods=['POST'])
def file_upload():
    return render_template_string("""
    {% extends "base.html" %}
    {% block content %}
        <h1>Thank you for uploading a file</h1>
    {% endblock %}
    """)

if __name__ == "__main__":
    app.run(debug=True)