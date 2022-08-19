import sqlite3


def get_movie_by_title(title):
    """Функция возвращает информацию о фильме по ключевому слову"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                SELECT title, country, release_year, listed_in, description 
                FROM netflix  
                WHERE title LIKE '%{title}%'
                ORDER BY release_year DESC
                """

        cursor.execute(query)
        result = cursor.fetchall()

        movie = {
            'title': result[0][0],
            'country': result[0][1],
            'release_year': result[0][2],
            'listed_in': result[0][3],
            'description': result[0][4]
        }

        return movie


def get_movie_by_years(year1, year2):
    """Функция возвращает все фильмы6 выпущенные в заданном периоде"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                SELECT title, release_year
                FROM netflix
                WHERE release_year BETWEEN {year1} AND {year2}
                ORDER BY release_year DESC
                LIMIT 100
                """

        cursor.execute(query)
        result = cursor.fetchall()

        list_movies = []
        for i in range(len(result)):
            movies = {
                'title': result[i][0],
                'release_year': result[i][1],
            }
            list_movies.append(movies)
        return list_movies


def get_movies_by_rating(ratings: str):
    """Функция возвращает фильмы по рейтингу"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        rating = ", ".join([f'"{rating}"' for rating in ratings])
        query = f"""
                SELECT title, rating, description
                FROM netflix
                WHERE rating IN ({rating})
                LIMIT 100
                """

        cursor.execute(query)
        result = cursor.fetchall()
        list_movies = []
        for line in result:
            movies = {
                "title": line[0],
                "rating": line[1],
                "description": line[2]
             }
            list_movies.append(movies)
        return list_movies


def get_movies_by_genre(genre):
    """Функция возвращает фильмы по заданному жанру"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                SELECT title, description 
                FROM netflix  
                WHERE listed_in LIKE '%{genre}%'
                ORDER BY release_year DESC
                LIMIT 10
                """

        cursor.execute(query)
        result = cursor.fetchall()
        list_movies = []

        for i in range(len(result)):
            movies = {
                'title': result[i][0],
                'description': result[i][1],
            }
            list_movies.append(movies)

        return list_movies


def get_movies_by_cast(cast1, cast2):
    """Фнукция возаращает название/ названия фильмов, где заданные актеры играли вместе"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"SELECT title FROM netflix " \
                f"WHERE \"cast\" LIKE '%{cast1}%' AND \"cast\" LIKE '%{cast2}%'"

        cursor.execute(query)
        result = cursor.fetchall()

        return result


def get_movies_by_parameters(type, release_year, listed_in):
    """Функция возвращает названия и информацию о фильме по заданным параметрам"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                SELECT title, description 
                FROM netflix  
                WHERE type LIKE '%{type}%'
                AND release_year == {release_year}
                AND listed_in LIKE '%{listed_in}%'
                LIMIT 10
                """

        cursor.execute(query)
        result = cursor.fetchall()
        list_movies = []

        for i in range(len(result)):
            movies = {
                'title': result[i][0],
                'description': result[i][1],
            }
            list_movies.append(movies)
        return list_movies




