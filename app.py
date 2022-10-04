from flask import Flask, render_template, redirect, send_from_directory

app = Flask(__name__)

@app.route('/About.html')
def About():
  return render_template('About.html')

@app.route('/All-Aboard.html')
def AllAboard():
  return render_template('All-Aboard.html')

@app.route('/Bethanys-Talishop.html')
def BethanysTalishop():
  return render_template('Bethanys-Talishop.html')

@app.route('/Character-Design.html')
def CharacterDesign():
  return render_template('Character-Design.html')

@app.route('/Neo-Zion.html')
def NeoZion():
  return render_template('Neo-Zion.html')

@app.route('/View-All.html')
def ViewAll():
  return render_template('View-All.html')

@app.route('/Gallery.html')
def Gallery():
  return render_template('Gallery.html')

@app.route('/')
def Home():
  return redirect('Gallery.html')

@app.errorhandler(404)
def page_not_found(e):
    return redirect('Gallery.html')

if __name__ == "__main__":

  app.run(host='0.0.0.0',debug=True)