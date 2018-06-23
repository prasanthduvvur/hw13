import time
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime


# Initialize browser
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "c:/users/owner/downloads/chromedriver_win32/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


# Function to scrape mars nasa website
def scrape_mars():

    # Initialize browser
    browser = init_browser()

    # Visit the mars nasa site
    url = "https://mars.nasa.gov/news"
    browser.visit(url)

    # Scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # mars headlines
    news_title = soup.find("div",class_="content_title").get_text()
    news_desc = soup.find("div",class_="rollover_description_inner").get_text()

    # Store in dictionary
    mars = {
        "newstitle": news_title,
        "newsdesc": news_desc,
    }

    # Return results
    return mars


# Function to scrape JPL Mars Space Images - Featured Image
def scrape_mars_image():

    # Initialize browser
    browser = init_browser()

    # Visit the mars nasa site
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    # Scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # mars image
    featured_image_url = soup.find('a',class_="button fancybox")
    url = featured_image_url.get('data-fancybox-href')

    # Store in dictionary
    marsimage = {
        "image_url": "https://www.jpl.nasa.gov"+url
    }

    # Return results
    return marsimage

# Function to Visit the Mars Weather twitter account and scrape the latest Mars weather tweet from the page. 
# Save the tweet text for the weather report as a variable called mars_weather.
def scrape_mars_twitter():

    # Initialize browser
    browser = init_browser()

    # Visit the mars nasa site
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)

    # Scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # mars weather report
    results = soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    for result in results:
    # Error handling
        try:
        # Identify and return tweet
            mars_tweet = result.text
            if "Sol" in mars_tweet: 
                marsweather_tweet = mars_tweet
                break
        except AttributeError as e:
            print(e)
    # Store in dictionary
    marsweather = {
        "marsweatherreport": marsweather_tweet
    }

    # Return results
    return marsweather


#function to scrape Mars Hemisperes
#Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
#You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

def scrape_mars_hemi():

    # Initialize browser
    browser = init_browser()

    #Visit the mars nasa cerebrus hemisphere site
    url_cerebrus = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(url_cerebrus)

    #Scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Cerebrus image
    url = soup.find("a",target="_blank")
    cerebrus_scrape_image_url = url.get("href")
    print("the url is: "+cerebrus_scrape_image_url)

    # Visit the mars nasa Schiaparelli hemisphere site

    # Initialize browser
    browser = init_browser()

    url_schiaparelli = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(url_schiaparelli)

    # # # Scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # # # Schiaparelli  image
    url = soup.find("a",target="_blank")
    schiaparelli_scrape_image_url = url.get("href")

    # # Initialize browser
    browser = init_browser()

    # # # # Visit the mars nasa Syrtis Major hemisphere site
    url_syrtis_major = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(url_syrtis_major)

    # # # # Scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # # # # Syrtis Major  image
    url = soup.find("a",target="_blank")
    syrtis_major_scrape_image_url = url.get('href')

    # # Initialize browser
    browser = init_browser()

    # # # Visit the mars nasa Valles Marineris hemisphere site
    url_valles_marineris = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(url_valles_marineris)

    # # # Scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # # # Valles Marineris  image
    url = soup.find("a",target="_blank")
    valles_marineris_scrape_image_url = url.get("href")

    # Store in dictionary
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": valles_marineris_scrape_image_url},
        {"title": "Cerberus Hemisphere", "img_url": cerebrus_scrape_image_url},
        {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_scrape_image_url},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_major_scrape_image_url}
    ]

    # Return results
    return hemisphere_image_urls