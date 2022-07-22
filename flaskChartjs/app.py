from flask import Flask
from flask import render_template, json,request
import datetime
import main

app = Flask(__name__)
"""
@app.route("/data", methods=["GET", "POST"])
def get_data():
	if request.method == "POST":
		date = request.form["date"]
        print(date)
"""
@app.route("/")
def chart():

    legend = 'COVID Cases'
    values,labels = main.confirmed_cases(3)
    values_rec,label_rec =main.Recovered_cases(3)
    values_det,label_det = main.death_cases(3)
    return render_template('index.html', values=values, labels=labels, legend=legend,values_rec=values_rec,label_rec=label_rec,values_det=values_det,label_det=label_det)

if __name__ == "__main__":
    app.run(debug=True)