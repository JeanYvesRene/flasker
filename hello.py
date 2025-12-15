from flask import Flask, render_template
# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
def index():
    first_name = "Jean-Yves"
    stuff = "This is <strong>Bold</strong> Text"
    favorite_pizza = ["Pepperoni", "Chesse", "Mushrooms", 41]
    return render_template ('index.html', 
                            first_name=first_name,
                            stuff=stuff, 
                            favorite_pizza=favorite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template ('user.html', name=name)

#Ceate Custome error Pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)

