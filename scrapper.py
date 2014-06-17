from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

BASE_URL = "http://www.imdb.com"
movie_rating = 0
movie_description = ""

def print_details(movie_description,movie_rating):
    print "Movie Name : " + movie
    print "Movie Rating : " + movie_rating
    print "Movie Description : " + movie_description
    return

def get_details(link):
    page = urlopen(link)
    soup = BeautifulSoup(page)
    div = soup.find('div', class_="titlePageSprite")
    movie_rating = div.contents[0]
    div = soup.find('p', itemprop="description")
    movie_description = div.contents[0] 
    DivDirector = soup.find('div', itemprop="director")
    #print DivDirector
    director = DivDirector.find('span', itemprop="name")
#director = DivDirector.find('span', itemprop="name")
    movie_director = director.contents[0]
    print_details(movie_description,movie_rating)
    return

def get_category_links(movie):
    page = urlopen(BASE_URL +"/find?" + movie)
    soup = BeautifulSoup(page)
    div = soup.find('table', class_="findList")
#print div
#print soup
    links = div.find('a', href=True)
    #print links['href']
    #print links
    #href = links.find()
    #print links.contents
    complete_link = BASE_URL + links['href']
    #print complete_link
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
#movie = "the-prestige"
get_category_links(movie)

