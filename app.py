from flask import Flask, render_template

from controllers.breeds_controller import breeds_blueprint



app = Flask(__name__)

app.register_blueprint(breeds_blueprint)



@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)