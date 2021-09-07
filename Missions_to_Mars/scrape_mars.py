# dependencies
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
import pandas as pd

# Function to scrape several Mars websites
def scrape_mars():

    # Scrapping News Title & News Paragraph
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Access webpage for data scrapping
    browser.visit('https://redplanetscience.com/')
    time.sleep(3)

    # Convert browser html to html string
    news_html = browser.html

    # Create BeautifulSoup Object and parse with HTML
    news_soup = BeautifulSoup(news_html, 'html.parser')

    # Retrieve latest news title and news paragraph
    news_title = news_soup.find('div', class_='content_title').text
    news_p = news_soup.find('div', class_='article_teaser_body').text
    print(news_title)
    print(news_p)

    # Scrapping Featured Image Url
    # Access webpage for data scrapping
    space_image_url = 'https://spaceimages-mars.com/'
    browser.visit(space_image_url)
    time.sleep(3)

    # Using splinter to click on Full Image Button
    browser.links.find_by_partial_text('FULL IMAGE').click()

    # Convert browser html to html string
    image_html = browser.html

    # Create BeautifulSoup Object and parse with HTML
    image_soup = BeautifulSoup(image_html, 'html.parser')

    # Retrieve Featured Image's Url
    featured_image = image_soup.find('img', class_='fancybox-image')['src']
    featured_image_url = space_image_url + featured_image
    print(featured_image_url)

    # Scrapping Mars Comparison Facts Table
    # Using Pandas to read HTML and storing tables in a list
    table = pd.read_html('https://galaxyfacts-mars.com/')

    # Renaming columns in the dataframe and setting the index
    comparison_df = table[0]
    mars_df = comparison_df.rename(columns={0:"Description", 1:"Mars", 2:"Earth"}).set_index("Description")
    
    # Convert dataframe to html
    mars_fact = mars_df.to_html(classes=["table", "table-striped", "table-bordered"], justify="left")

    # Scrapping Mars Hemispheres images
    # Access webpage for data scrapping
    hemisphere_url = 'https://marshemispheres.com/'
    browser.visit(hemisphere_url)
    time.sleep(3)

    # Convert browser html to html string
    hemisphere_html = browser.html

    # Create BeautifulSoup Object and parse with HTML
    hemisphere_soup = BeautifulSoup(hemisphere_html, 'html.parser')

    # Retrieve all h3 tags to get the names of hemispheres
    hemisphere_link = hemisphere_soup.find_all('h3')[0:-1]

    # Declare a list to store hemisphere image url and title as dictionary
    hemisphere_image_urls = []

    # For loop to iterate through the hemisphere name and retrieve title and image url using splinter
    for names in hemisphere_link:
        
        # Retrieve name of the hemisphere and use splinter to access each image page
        sphere = names.text 
        browser.links.find_by_partial_text(sphere).click()
        
        enhanced_html = browser.html
        enhanced_soup = BeautifulSoup(enhanced_html, 'html.parser')
        
        hemisphere_title = enhanced_soup.find('h2', class_="title").text.rsplit(' ',1)[0]
        hemisphere_image = hemisphere_url + enhanced_soup.find('img', class_='wide-image')['src']
        
        hemisphere_image_urls.append({"title":hemisphere_title, "img_url": hemisphere_image})
        
        # Click on "Back" to return to homepage to run the loop again
        browser.links.find_by_partial_text('Back').click()

    print(hemisphere_image_urls)

    # Store Data in dictionary
    mars_scrape_data = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image_url": featured_image_url,
        "mars_facts": mars_fact,
        "mars_hemispheres_urls": hemisphere_image_urls
        }
    browser.quit()

    return mars_scrape_data
