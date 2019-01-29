from flask import Flask, render_template, request, redirect, json
from scrape import scrape_page_range

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

# Code adapted from:
# https://www.bogotobogo.com/python/Flask/Python_Flask_with_AJAX_JQuery.php
@app.route('/scrape', methods=['POST'])
def scrape():
    if request.method == 'POST':
        page_start = request.form['page_start']
        page_end = request.form['page_end']

        """
        This function would return some html or information as a dictionary
        html_to_display = scrape_page_range(page_start, page_end)

        """

    return json.dumps({'status': 'OK', 'page_start': page_start, 'page_end': page_end})
    # return redirect(url_for('home'))

if __name__== "__main__":
    app.run(debug=True)
