from flask import Flask, render_template #pip install flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("base.html")

if __name__ == '__main__':
    app.debug = True #set to False in production mode
    app.run()
