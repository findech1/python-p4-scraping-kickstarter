# file: kickstarter_scraper.py
from bs4 import BeautifulSoup
import ipdb

def create_project_dict():
    html = ''
    with open('./fixtures/kickstarter.html') as file:
        html = file.read()
    
    kickstarter = BeautifulSoup(html, 'html.parser')
    projects = {}

    # Iterate through the projects
    for project in kickstarter.select("li.project.grid_4"):
        title = project.select("h2.bbcard_name strong a")[0].text
        image_link = project.select("div.project-thumbnail a img")[0]['src']
        description = project.select("p.bbcard_blurb")[0].text
        location = project.select("ul.project-meta span.location-name")[0].text
        percent_funded = project.select("ul.project-stats li.first.funded strong")[0].text.replace("%", "")

        # Store project details in the dictionary
        projects[title] = {
            'image_link': image_link,
            'description': description,
            'location': location,
            'percent_funded': percent_funded
        }

    # Return the projects dictionary
    return projects

# Uncomment the line below if you want to start debugging with ipdb
ipdb.set_trace()

# Call the function and print the result
result = create_project_dict()
print(result)
