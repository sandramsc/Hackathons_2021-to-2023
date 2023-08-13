from flask import *
import pandas as pd
from werkzeug.utils import secure_filename
import os
import business

app = Flask(__name__)

UPLOAD_PATH = 'static/'

FILE_NAME = 'user-feedback.csv'

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/count')
def count():

    df_positive = pd.read_csv('static/positive.csv')

    df_neutral = pd.read_csv('static/neutral.csv')

    df_negative = pd.read_csv('static/negative.csv')

    data = {

        "pos": len(df_positive),
        "neg": len(df_negative),
        "neu": len(df_neutral),

    }

    return render_template('count.html', data = data)


@app.route('/top/<state>')
def top(state):

    if state == 'positive':

        df_positive = pd.read_csv('static/positive.csv')

        df_positive = df_positive[:10]

        return render_template('table.html',tables=[df_positive.to_html(classes='female')],
                titles = ['positive reviews'])

    if state == 'negative':

        df_negative = pd.read_csv('static/negative.csv')

        df_negative = df_negative[:10]

        return render_template('table.html',tables=[df_negative.to_html(classes='male')],
                titles = ['negative reviews'])

    return 'specify state', 501

@app.route('/download')
def download():

    return send_file('results.csv', as_attachment=True)

if __name__ == '__main__':

    business.process()
    
    app.run(host='0.0.0.0', debug=True)
