from flask import Flask

app = Flask(__name__)

"""
Static pages below 
"""
@app.route("/")
def home():
    return "Hello world from Flask 2"

@app.route("/about")
def about():
    return "This is the about page"

@app.route("/contact")
def contact():
    return "This is the contact page"

"""
Dynamic pages below
"""
@app.route("/user/<name>")
def user(name):
    return f"This is {name}'s page"

@app.route("/user/<name>/<bio>")
def user_bio(name, bio):
    return f"This is {name}'s {bio}"

"""
URL convert examples blow
"""

@app.route("/student/<int:id")
def student(id):
    return f"Hello student {id}"


@app.route("product/<int:product_id>/<float:price>")
def product(product_id, price):
    return f"This is product {product_id}, which costs {price}"

@app.route("files/<path:file_path>")
def files(file_path):
    return f"This was the file path: {file_path}"

@app.route("developer/<uuid: user_id>")
def developer(uuid):
    return f"This is developer {uuid}"


if __name__ == "__main__":
    app.run(debug=True)