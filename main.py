from flask import Flask, request, render_template, url_for

app=Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def index():
  CSS_MAIN = url_for('static', filename='style.css')
  return render_template('index.html', style=CSS_MAIN)

app.run()