from flask import Flask, render_template,request



app = Flask(__name__)







@app.route('/' )
def index():
    weather =request.form.get("weather")
    country =request.form.get("country")
   
    return render_template("index.html")

@app.route('/results')

def results():
    weather =request.form.get("weather")
    country =request.form.get("country")
   
         
    return render_template("results.html",weather=weather)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
