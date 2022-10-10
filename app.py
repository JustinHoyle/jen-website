from flask import Flask, render_template, redirect, send_from_directory, flash
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm, Form
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, email_validator
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = os.urandom(12).hex()

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config["MAIL_USERNAME"] = 'capartwebsitecontact@gmail.com'
app.config["MAIL_PASSWORD"] = 'mhqeostpatzlkqwu'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

 
mail.init_app(app)

class contactForm(FlaskForm):
    name = StringField(label='Enter your Name', validators=[DataRequired()])
    email = StringField(label='Enter a valid email address', validators=[DataRequired(), Email()])
    message = StringField(label='Enter your message')
    submit = SubmitField(label="Submit")

@app.route("/Contact.html", methods=["GET", "POST"])
def Contact(): 
    if request.method == 'POST':
      msg = Message(request.form.get('name'), sender='contact@example.com', recipients=['capartwebsitecontact@gmail.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (request.form.get('name'), request.form.get('email'), request.form.get('message'))
      mail.send(msg)

      return render_template('Contact.html')
    
    elif request.method == 'GET':
      return render_template('Contact.html')
  
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