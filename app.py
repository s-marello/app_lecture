from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf

app = Flask(__name__)

def get_prediction(user_input):
    model = tf.keras.models.load_model('model') 
    user_result = model.predict(user_input)
    ppr_target = user_result.tolist()[0][0]
    mupr_target = user_result.tolist()[0][1]
    return (f"Прочность при растяжении, МПа: {ppr_target} /nМодуль упругости при растяжении, ГПа: {mupr_target}")

@app.route('/', methods=['POST', 'GET'])

@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    message = ''
    if request.method == 'GET':
        return render_template('main.html')
    if request.method == 'POST':  
        smn = float(request.form.get('smn'))
        pl = float(request.form.get('pl'))
        mu = float(request.form.get('mu'))
        ko = float(request.form.get('ko'))
        seg = float(request.form.get('seg'))
        tv = float(request.form.get('tv'))
        pp = float(request.form.get('pp'))
        ps = float(request.form.get('ps'))
        un = float(request.form.get('un'))
        shn = float(request.form.get('shn'))
        pn = float(request.form.get('pn'))
        user_input_list = [[smn, pl, mu, ko, seg, tv, pp, ps, un, shn, pn]]
        list_array = np.array(user_input_list)
        message = get_prediction(list_array)
        return render_template('main.html', message=message)
    
if __name__ == '__main__':
    app.run()
