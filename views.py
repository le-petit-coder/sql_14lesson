from flask import Flask, jsonify
from utils import get_movie_by_title, get_movie_by_years, get_movies_by_genre, get_movies_by_rating

app = Flask(__name__)


@app.route("/movie/<title>")
def movie_page(title):
    json_movie = get_movie_by_title(title)
    return jsonify(json_movie)


@app.route("/movie/<year1>/to/<year2>")
def movie_by_years(year1, year2):
    json_movie = get_movie_by_years(year1, year2)
    return jsonify(json_movie)


@app.route("/genre/<genre>")
def movies_by_genre(genre):
    json_movies = get_movies_by_genre(genre)
    return jsonify(json_movies)


@app.route("/rating/children")
def movies_children():
    rating = 'G'
    json_movies = get_movies_by_rating(rating)
    return jsonify(json_movies)


@app.route("/rating/family")
def movies_family():
    rating = ['PG', 'PG-13']
    json_movies = get_movies_by_rating(rating)
    return jsonify(json_movies)


@app.route("/rating/adult")
def movies_adults():
    rating = ['R', 'NC-17']
    json_movies = get_movies_by_rating(rating)
    return jsonify(json_movies)


if __name__ == '__main__':
    app.run()
