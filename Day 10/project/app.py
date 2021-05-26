import imdb_scraper
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    lis = imdb_scraper.get_movie_info(page=1)
    return render_template('home.html', data = lis)

if __name__ == '__main__':
    app.run(debug=True)