from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/Home.html')
def Home():
  return render_template('Home.html')

@app.route('/About.html')
def About():
  return render_template('About.html')

@app.route('/Contact.html')
def Contact():
  return render_template('Contact.html')

@app.route('/')
def index():
  return redirect('Home.html')

if __name__ == "__main__":

  app.run(host='0.0.0.0',debug=True)