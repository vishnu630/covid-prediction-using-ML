from flask import Flask
from flask import render_template, json,request,redirect,url_for
from _datetime import datetime
import main

app = Flask(__name__)

@app.route("/")
def chart():

    legend = 'COVID Cases'
    values,labels = main.confirmed_cases(60)
    values_rec,label_rec =main.Recovered_cases(60)
    values_det,label_det = main.death_cases(60)
    return render_template('index.html', values=values, labels=labels, legend=legend,values_rec=values_rec,label_rec=label_rec,values_det=values_det,label_det=label_det)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        year = request.form['year']
        month = request.form['month']
        day = request.form['day']
        by = datetime(int(year),int(month),int(day))
        now = datetime.now()
        by = datetime(by.year, by.month, by.day)
        date= (by - now.today()).days
        legend = 'COVID Cases'
        values, labels = main.confirmed_cases(date)
        values_rec, label_rec = main.Recovered_cases(date)
        values_det, label_det = main.death_cases(date)
        return render_template('index.html', values=values, labels=labels, legend=legend,values_rec=values_rec,label_rec=label_rec,values_det=values_det,label_det=label_det)
    else:
        return render_template('predict.html')
if __name__ == "__main__":
    app.run(debug=True)
