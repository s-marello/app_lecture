from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf


app = Flask(__name__)


def get_prediction(smn, pl, mu, ko, seg, tv, pp, ps, un, shn, pn):
    model = tf.keras.models.load_model(r"model") 
    user_result = model.predict(np.array([[smn, pl, mu, ko, seg, tv, pp, ps, un, shn, pn]]))
    
    return f"Ответ {user_result}"


@app.route('/', methods = ['POST', 'GET'])

@app.route('/predict/', methods=['post', 'get'])
def processing():
    message = ''
    if request.method == 'POST':
        smn = request.form.get('smn')
        pl = request.form.get('pl')
        mu = request.form.get('mu')
        ko = request.form.get('ko')
        seg = request.form.get('seg')
        tv = request.form.get('tv')
        pp = request.form.get('pp')
        ps = request.form.get('ps')
        un = request.form.get('un')
        shn = request.form.get('shn')
        pn = request.form.get('pn')
        

        message = get_prediction(smn, pl, mu, ko, seg, tv, pp, ps, un, shn, pn)

    return render_template('login.html', message=message)


if __name__ == '__main__':
    app.run()
