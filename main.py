from flask import Flask, redirect, request, render_template, url_for
import sys
import re

app=Flask(__name__)
app.config['DEBUG']=True

# Validation Method
def validate(field, required=True, min_length=3, max_length=20):
  if field == '' and required:
    return "This field is required."
  elif ' ' in field:
    return "Spaces are not allowed."
  elif len(field)<min_length:
    return "This field must be at least {} characters long.".format(min_length)
  elif len(field)>max_length:
    return "This field must be less than {} characters long.".format(max_length)
  return ''

def match(field, match_field):
  if field != match_field:
    return "Passwords do not match."
  return ''

def validate_email(field):
  if len(field)>0:
    validate_error = validate(field, required=False)
    if validate_error == '':
      regex = r"^\w+\@{1}\w+\.{1}\w+$"
      if re.fullmatch(regex, field):
        return ''
      else:
        return 'Email address is not valid.'
    else:
      return validate_error
  return ''

# Routes
@app.route('/')
def index():
  return render_template('sign-up.html')

@app.route('/', methods=["POST"])
def validation():

  name = request.form['name']
  password = request.form['password']
  confirm_password = request.form['confirm-password']
  email = request.form['email']

  # error vars
  name_error = ''
  password_error = ''
  confirm_password_error = ''
  email_error = ''

  # Do Validation Checks
  name_error = validate(name)
  password_error = validate(password)
  confirm_password_error = match(confirm_password, password)
  email_error = validate_email(email)

  if name_error or password_error or confirm_password_error or email_error:
    return render_template('sign-up.html',
                            name=name,
                            email=email,
                            name_error=name_error,
                            password_error=password_error,
                            confirm_password_error=confirm_password_error,
                            email_error=email_error)
  
  return render_template('welcome.html', name=name)
app.run()