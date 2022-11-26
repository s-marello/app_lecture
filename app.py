from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')

def get_prediction(user_input):
    model = tf.keras.models.load_model("model") 
    user_result = model.predict(user_input)
    
    return f"Ответ {user_result}"

@app.route('/predict/', methods=['post', 'get'])
def processing():
    message = ''
    if request.method == 'POST':  
        message = get_prediction(np.array([[request.form.get('smn'), 
                                            request.form.get('pl'),
                                            request.form.get('mu'),
                                            request.form.get('ko'),
                                            request.form.get('seg'),
                                            request.form.get('pp'),
                                            request.form.get('ps'),
                                            request.form.get('un'),
                                            request.form.get('shn'),
                                            request.form.get('pn')]]))
    return render_template('login.html', message=message)


if __name__ == '__main__':
    app.run()
