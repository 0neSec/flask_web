from flask import Flask, render_template, url_for
from markupsafe import escape
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
   suasana = "sedih"
   hari = ['senijnjnjnjhhbh', 'selasa', 'rabu', 'kamis', 'jumaat', 'sabtu', 'minggu']
   return render_template("pages/home.html", value="hai ighh saya mohamad khadik", 
                         namaHari= hari, suasana=suasana);



@app.route("/about")
def About():
   return render_template("pages/about.html" );


@app.route("/user/<string:username>")
def user(username):
   return "hallo i'am:{}".format(username);




if __name__ == "__main__":
   app.run(debug=True)
