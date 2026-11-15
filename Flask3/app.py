from flask import Flask, render_template, request, redirect, url_for
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

    
if __name__ == "__main__":
    app.run(debug=True)