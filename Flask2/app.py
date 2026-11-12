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
    return "This is the about page"

if __name__ == "__main__":
    app.run(debug=True)