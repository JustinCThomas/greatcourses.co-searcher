from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        page_start = request.form['page_start']
        page_end = request.form['page_end']

    return render_template("home.html")

if __name__== "__main__":
    app.run(debug=True)
