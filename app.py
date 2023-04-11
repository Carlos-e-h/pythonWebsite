from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



@app.route('/')

def hello():

    return render_template('homepage.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':

    app.run(debug=True,port=2000)

