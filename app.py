from flask import Flask,session,flash,redirect,render_template,url_for,request
import pandas as pd 
import numpy as np
from select_col import select_col
from load_data import return_model



app = Flask(__name__)
app.secret_key ="abc"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET','POST'])
def form():
        if request.method == "POST":
            ROAC = request.form.get('ROA(C)')
            ROAA = request.form.get('ROA(A)')
            ROAB = request.form.get('ROA(B)')
            EPS = request.form.get('EPS')
            Share_net_profit = request.form.get('Share Net Profit')
            Debt_ratio = request.form.get('Debt ratio')
            Net_asset = request.form.get('Net Assets')
            net_profit_bt = request.form.get('Net profit before tax')
            Retained_Earnings = request.form.get('Retained Earnings')
            Net_Income = request.form.get('Net Income')
            sample = pd.DataFrame([[ROAC,ROAA,ROAB,EPS,Share_net_profit,
                                   Debt_ratio,Net_asset,net_profit_bt,
                                   Retained_Earnings,Net_Income]],columns = select_col())

            result = return_model().predict(sample)
            session['prediction'] = 'may become bankrupt' if result[0] == 0 else 'no sign of bankrupty'
            return redirect('/result')
        return render_template('form.html')

# def result(sample_data):
#      result = return_model.score(sample_data)
#      return result

@app.route('/result')
def result():
    if 'prediction' in session:
        return render_template('result.html')
    return redirect('/form')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
 