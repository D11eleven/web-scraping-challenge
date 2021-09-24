#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os
import pymongo
import requests
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


# In[ ]:


# Set up Splinter
#     executable_path = {'executable_path': ChromeDriverManager().install()}
#     executable_path = {'executable_path': 'chromedriver'}
#     browser = Browser('chrome', **executable_path, headless=False)

  # Scrape page into Soup
#     def scrape():
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False) 


# In[ ]:



conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.commerce_db
collection = db.items


# In[ ]:


# ### NASA Mars News

# * Scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

# ```python
# # Example:
# news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

# news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
# ```


# In[ ]:


time.sleep(1)


# In[ ]:


# def mars_news(): 
        
url = "https://redplanetscience.com/"
browser.visit(url)
        
        
    
    
    
html = browser.html
soup = bs(html, "html.parser")
    
mars_title = soup.find('div', class_ = 'content_title').get_text()
mars_paragraph = soup.find('div', class_ = 'article_teaser_body').get_text()
    
        #     print(f"{mars_title}")
mars_title
mars_paragraph

mars_results = [mars_title, mars_paragraph]
mars_results


# In[ ]:



# ### JPL Mars Space Images - Featured Image

# * Visit the url for the Featured Space Image site [here](https://spaceimages-mars.com).

# * Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

# * Make sure to find the image url to the full size `.jpg` image.

# * Make sure to save a complete url string for this image.

# ```python
# # Example:
# featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'




# grab our new html from surfline      ******   FROM webscrape 3  extra content

#     browser.is_element_present_by_css(".sl-premium-analysis-link", 1)
#     analysis_url = browser.find_link_by_partial_href("premium-analysis").first["href"]
#     browser.visit(analysis_url)
#     browser.is_element_present_by_css(".sl-feed-article", 1)
# ```


# In[ ]:


# def mars_image():
url = "https://spaceimages-mars.com/"
browser.visit(url)
time.sleep(2)

html = browser.html
soup = bs(html, "html.parser")
image = soup.find("img", class_="headerimage fade-in").get("src")
                            
# image 
featured_image_url= "https://spaceimages-mars.com" + image
    
print(f"url: {featured_image_url}")
#     return featured_image_url


# In[ ]:





# In[ ]:


# ### Mars Facts

# * Visit the Mars Facts webpage [here](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

# * Use Pandas to convert the data to a HTML table string.


# In[ ]:


marsfacts_url = "https://galaxyfacts-mars.com"

htm = pd.read_html(marsfacts_url)
mars_tables_df = htm[0]
mars_tables_df


# In[ ]:





# In[ ]:


marsfacts_url = 'https://galaxyfacts-mars.com'

marsfacts= pd.read_html(marsfacts_url)[0]


marsfacts.columns = ['Description', 'Mars', 'Earth']
marsfacts.set_index('Description', inplace=True)
marsfacts_html = marsfacts.to_html()
marsfacts_html


# In[ ]:


clean_html = marsfacts_html.replace('\n', '')
clean_html


# In[ ]:


mars_html = mars_tables_df.to_html('marsfacts_html')
mars_html


# In[ ]:


# ### Mars Hemispheres

# * Visit the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.

# * You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

# * Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

# * Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

# ```python
# # Example:
# hemisphere_image_urls = [
#     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
#     {"title": "Cerberus Hemisphere", "img_url": "..."},
#     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
#     {"title": "# Schiaparelli


url = 'https://marshemispheres.com/'
browser.visit(url)
time.sleep(2)


browser.links.find_by_partial_text('Schiaparelli').click()


html = browser.html
soup = bs(html,"html.parser")



img_link = soup.find('img', class_='wide-image').get('src')


planet_dict = []

url = 'https://marshemispheres.com/'
browser.visit(url)
time.sleep(2)


browser.links.find_by_partial_text('Cerberus').click()


html = browser.html
soup = bs(html,"html.parser")



img_link = soup.find('img', class_='wide-image').get('src')
 
cerberus_title = soup.find('h2', class_='title').text



cerberus_img = url + img_link


browser.back()


cerberus_dict = {'title:' + cerberus_title, 'img_url:' + cerberus_img}
planet_dict.append(cerberus_dict)

cerberus_dict






# In[ ]:







# In[20]:


# Schiaparelli


url = 'https://marshemispheres.com/'
browser.visit(url)
time.sleep(2)


browser.links.find_by_partial_text('Schiaparelli').click()


html = browser.html
soup = bs(html,"html.parser")

img_link = soup.find('img', class_='wide-image').get('src')


schiaparelli_title = soup.find('h2', class_='title').text



schiaparelli_img = url + img_link


browser.back()


schiaparelli_dict = {'title:' + schiaparelli_title, 'img_url:' + schiaparelli_img}
planet_dict.append(schiaparelli_dict)

schiaparelli_dict


# In[21]:


# Syrtis


url = 'https://marshemispheres.com/'
browser.visit(url)
time.sleep(2)


browser.links.find_by_partial_text('Syrtis').click()


html = browser.html
soup = bs(html,"html.parser")



img_link = soup.find('img', class_='wide-image').get('src')


syrtis_title = soup.find('h2', class_='title').text



syrtis_img = url + img_link


browser.back()


syrtis_dict = {'title:' + syrtis_title, 'img_url:' + syrtis_img}
planet_dict.append(syrtis_dict)

syrtis_dict


# In[22]:


# Valles Marineris


url = 'https://marshemispheres.com/'
browser.visit(url)
time.sleep(2)


browser.links.find_by_partial_text('Valles Marineris').click()


html = browser.html
soup = bs(html,"html.parser")



img_link = soup.find('img', class_='wide-image').get('src')


valles_title = soup.find('h2', class_='title').text



valles_img = url + img_link


browser.back()
 

valles_dict = {'title:' + valles_title, 'img_url:' + valles_img}
planet_dict.append(valles_dict)

valles_dict


planet_dict

browser.quit()



# In[ ]:





# In[ ]:


# ## Step 1 - Scraping

# Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

# * Create a Jupyter Notebook file called `mission_to_mars.ipynb` and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.




# ### NASA Mars News

# * Scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

# ```python
# # Example:
# news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

# news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
# ```





# ### JPL Mars Space Images - Featured Image

# * Visit the url for the Featured Space Image site [here](https://spaceimages-mars.com).

# * Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

# * Make sure to find the image url to the full size `.jpg` image.

# * Make sure to save a complete url string for this image.

# ```python
# # Example:
# featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'
# ```





# ### Mars Facts

# * Visit the Mars Facts webpage [here](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

# * Use Pandas to convert the data to a HTML table string.





# ### Mars Hemispheres

# * Visit the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.

# * You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

# * Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

# * Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

# ```python
# # Example:
# hemisphere_image_urls = [
#     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
#     {"title": "Cerberus Hemisphere", "img_url": "..."},
#     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
#     {"title": "Syrtis Major Hemisphere", "img_url": "..."},
# ]
# ```


# In[ ]:




