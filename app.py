from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return 'welcome to VeiwlyTube'

app.run(debug=True)