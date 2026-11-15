from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run(debug=True)