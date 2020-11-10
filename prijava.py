from bs4 import BeautifulSoup
import requests

def uvozi_html(url):
    # Start the session
    session = requests.Session()

    # Create the payload
    payload = {'username':'email', 
            'password':'willchangeit'
            }

    # Post the payload to the site to log in
    s = session.post("https://www.studentski-servis.com/ess/login.php", data=payload)

    # Navigate to the next page and scrape the data
    s = session.get(url)


    soup = BeautifulSoup(s.content, 'html.parser')
    return soup.prettify()
