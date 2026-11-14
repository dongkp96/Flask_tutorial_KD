from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    name ="Kevin"
    id = 5
    course ="Mohit's Flask tutorial"
    return render_template('index.html', title='Home page', 
                           name=name,
                           id = id,
                           course = course)

@app.route("/about")
def about():
    logged_in = False
    items = ["Apple", "Orange", "Banana"]
    students = {
        "Enya": "Math",
        "Kevin": "English :("
    }
    return render_template("about.html", title="About page", logged_in =logged_in, items = items, students=students)

if __name__ == "__main__":
    app.run(debug=True)