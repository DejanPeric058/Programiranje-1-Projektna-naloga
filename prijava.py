from bs4 import BeautifulSoup
import requests

# Spletna stran je zahtevala prijavo uporabnika. To težavo sem rešil s knjižnico BeautifulSoup 
# in funkcijo uvozi_html. 

def uvozi_html(url):
    '''Vrne html spletne strani, na kateri se je treba prijaviti z uporabniškim imenom in geslom.'''    
    # Start the session
    session = requests.Session()

    # Create the payload
    
    
    
    payload = {'username':'', 
            'password':''
            }



    # Post the payload to the site to log in
    s = session.post("https://www.studentski-servis.com/ess/login.php", data=payload)

    # Navigate to the next page and scrape the data
    s = session.get(url)


    soup = BeautifulSoup(s.content, 'html.parser')
    return soup.prettify()
