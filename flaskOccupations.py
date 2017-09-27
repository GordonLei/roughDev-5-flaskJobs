from flask import Flask, render_template
from occupation import randomJob, createDict, returnReader
#import occupation, csv, random

app = Flask(__name__)

@app.route("/")
def root():
        return "root"

@app.route("/occupations")
def occupation(): 
        return render_template("ace.html", dictJob = createDict(), randJob = randomJob(createDict()))

if __name__ == "__main__":
        app.debug = True
        app.run()
