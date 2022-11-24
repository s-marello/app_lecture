from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf


app = Flask(__name__)


def get_prediction(person):
    model = tf.keras.models.load_model(r"models\titanic_mlp")
    y_pred = model.predict(person)

    return f"Человек выжил с вероятностью {y_pred}"


@app.route('/')
def index():
    return "main"


@app.route('/predict/', methods=['post', 'get'])
def processing():
    message = ''
    if request.method == 'POST':
        person = request.form.get('username')

        person_parameters = person.split(" ")
        person = [float(param) for param in person_parameters]
        person = np.array([person])

        message = get_prediction(person)

    return render_template('login.html', message=message)


if __name__ == '__main__':
    app.run()
