from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

BASE_URL = "http://www.imdb.com"
movie_rating = 0
movie_description = ""

#
#   Print the details of the found movie
#

def print_details(movie_description,movie_rating):
    print "Movie Name : " + movie
    print "Movie Rating : " + movie_rating
    print "Movie Description : " + movie_description
    return

#
#   Get the details of the found movie. Scrape throu' for director and rating.
#   More details to be added.
#

def get_details(link):
    page = urlopen(link)
    soup = BeautifulSoup(page)
    div = soup.find('div', class_="titlePageSprite")
    movie_rating = div.contents[0]
    div = soup.find('p', itemprop="description")
    movie_description = div.contents[0] 
    DivDirector = soup.find('div', itemprop="director")
    director = DivDirector.find('span', itemprop="name")
    movie_director = director.contents[0]
    print_details(movie_description,movie_rating)
    return

#
#   Find the movie, using imdb/find? tag. Get the first matched movie.
#

def get_category_links(movie):
    page = urlopen(BASE_URL +"/find?" + movie)
    soup = BeautifulSoup(page)
    div = soup.find('table', class_="findList")
    links = div.find('a', href=True)

    complete_link = BASE_URL + links['href']
    get_details(complete_link)
    return
def format_movie():
    movie.replace(" ","-")
    return
movie = raw_input("Enter movie name : ")
#format_movie()
#movieCapital = capitalize(movie)
movie = movie.replace(" ","-")
#print movie
get_category_links(movie)

