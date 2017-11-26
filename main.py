from flask import Flask, request, render_template, url_for

app=Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def index():
  return render_template('sign-up.html')

@app.route('/', methods=["POST"])
def validation():
  return render_template('sign-up.html')

app.run()