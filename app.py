# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_info

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app)


# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # store collection in a list
    marsdb_list = list((mongo.db.mars.find()))

    print(marsdb_list)

    # return template and data
    return render_template("index.html", marsdb_list=marsdb_list)

# # Set route
# @app.route('/')
# def index():
#     # Store the entire team collection in a list
#     teams = list(db.team.find())
#     print(teams)

#     # Return the template with the teams list passed in
#     return render_template('index.html', teams=teams)

# Route that will trigger scrape functions
@app.route("/scrape")
def scrape():

    # Run scraped functions
    mars = scrape_info.scrape_mars()
    marsimage = scrape_info.scrape_mars_image()
    marsweather = scrape_info.scrape_mars_twitter()
    marshemiurls = scrape_info.scrape_mars_hemi()

    # Drops collection if available to remove duplicates
    mongo.db.mars.drop()

    # Store results into a dictionary
    marsdict = {
        "headline": mars["newstitle"],
        "newspara": mars["newsdesc"],
        "marsimageurl": marsimage["image_url"],
        "marsweather": marsweather["marsweatherreport"],
        "marshemiurls": marshemiurls
    }

    # Insert mars info into database
    mongo.db.mars.insert_one(marsdict)

    # Redirect back to home page
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
