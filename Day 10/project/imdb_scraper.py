import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

def get_movies_ids(num=10, page=1):
    links_data = pd.read_csv("links.csv")
    movies_ids = list(links_data.imdbId)
    start_index = (page-1)*num
    end_index = start_index + num
    return movies_ids[start_index:end_index]

def get_movie_data(movie_id):
    url = f"https://www.imdb.com/title/tt{str(movie_id).zfill(7)}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    info = soup.find("script", attrs={"type":"application/ld+json"}).string
    json_info = json.loads(str(info))
    return json_info

def collect_movie_info(movie_id):
    info = get_movie_data(movie_id)
    movie = {
        "name" : info["name"],
        "genre" : info["genre"],
        "image" : info["image"],
        "description" : info["description"]
    }
    return movie


def get_movie_info(page=1):
    ids = get_movies_ids(page=page)
    lis = []
    for id in ids:
        data = collect_movie_info(id)
        lis.append(data)
    return lis


if __name__ == "__main__":
    ids = get_movies_ids(page=2)
    for id in ids:
        data = collect_movie_info(id)
        print(data)



