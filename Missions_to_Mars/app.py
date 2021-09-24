# ## Step 2 - MongoDB and Flask Application

# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

# * Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

# * Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

#   * Store the return value in Mongo as a Python dictionary.

# * Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.


from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

@app.route("/")
def index():
    scraped_info = mongo.db.scraped_info.find_one()
    return render_template("index.html", scraped_info=scraped_info)

@app.route("/scrape")
def scrape():
    # Run scrape function
    scraped = scrape_mars.mars_scrape()

    mongo.db.scraped_info.update({}, scraped, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
