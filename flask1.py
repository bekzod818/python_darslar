from flask import Flask
app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return "<center><h1>Asosiy sahifa</h1></center>"

@app.route('/user/<username>')
def show_user_profile(username):
    return '<h1>User %s</h1>' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return '<h1>Post %d</h1>' % post_id

@app.route('/projects/')
def projects():
    return '<h1>The project page</h1>'

@app.route('/about')
def about():
    return "<center><h1>Sayt haqida</h1></center>"

if __name__ == '__main__':
    app.run(debug=True)































# from flask import Flask, render_template
# app = Flask(__name__)
#
# @app.route("/index")
# @app.route("/")
# def index():
#     return render_template("BMI.html")
#
# @app.route("/about")
# def about():
#     return "<center><h1>Sayt haqida</h1></center>"
#
# if __name__ == "__main__":
#     app.run(debug=True)