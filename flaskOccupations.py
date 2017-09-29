from flask import Flask, render_template
from utils import occupation
#import occupation, csv, random

app = Flask(__name__)

@app.route("/")
def root():
        return "root"

@app.route("/occupations")
def occupations(): 
        return render_template("ace.html", dictJob = occupation.createDict(), randJob = occupation.randomJob(occupation.createDict()))

if __name__ == "__main__":
        app.debug = True
        app.run()
