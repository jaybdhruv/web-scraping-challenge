# Web Scrapping: Mission To Mars

I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## Step 1 - Scraping

I completed initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Splinter.

### NASA Mars News

* I scraped the [Mars News Site](https://redplanetscience.com/) and collected the latest News Title and Paragraph Text. Assigned this to a variable news_title and news_p.

### JPL Mars Space Images - Featured Image

* Visited the url for the Featured Space Image site [here](https://spaceimages-mars.com).

* Used splinter to navigate the site (clicked on "Full Image" to access the high quality image) and found the image url for the current Featured Mars Image and assigned the url string to a variable called `featured_image_url`.

### Mars Facts

* Visited the Mars Facts webpage [here](https://galaxyfacts-mars.com) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. Used Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Visited the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.

* Created a For loop and used Splinter to loop through each click on each hemisphere's full image. Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys `img_url` and `title`.

- - -

## Step 2 - MongoDB and Flask Application

Used MongoDB with Flask template to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Converted my Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that executed all of my scraping code from above and returned one Python dictionary containing all of the scraped data.

* Next, created a route called `/scrape` that imported my `scrape_mars.py` script and called my `scrape` function.

* Created a root route `/` that queried my Mongo database and passed the mars data into an HTML template to display the data.

* Created a template HTML file called `index.html` that took the mars data dictionary and displayed all of the data in the appropriate HTML elements.

## Below are few screenshots of my scraped data and HTML page - 

* MongoDB Data

!['mongodata'](screenshots\mars_mongo_db.jpg)

* HTML Page

!['html_page1'](screenshots\mission_to_mars_html1.jpg)

!['html_page1'](screenshots\mission_to_mars_html2.jpg)