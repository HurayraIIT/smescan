from cgi import test
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse


URL = 'https://app.smevai.com'
USERNAME = 'wpdabh+year22sa1@gmail.com'
PASSWORD = 'pass1234'


# links = FindLinksFromWebpage(URL)
all_links = []
tested_links = []


# Check If a string is a valid URL
def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


# This function will login to the laravel website
def login(url, username, password):
    s = requests.Session()
    
    # Get the crsf_token first
    front = s.get(url)
    token = re.findall(r'<input type="hidden" name="_token" value="(.*)"', front.text )
    csrf_token = (token[0] if len(token)>0 else '0')
    
    # Get cookies
    cookies = s.cookies
    
    # Create the login payload
    payload = {
        'username': username,
        'password': password,
        '_token': csrf_token
    }
    
    # Send the login POST request
    res = s.post(
        url=url+'/login', 
        data=payload,
        cookies=cookies
    )
    
    # print(res.status_code)
    
    return s


# Find all links from a webpage
def FindLinksFromWebpage(session, url):
    r = session.get(url)
    if r.status_code >= 400:
        print(f'[x] Error: Code {r.status_code} on URL - {url}')
        return []
    html_page = r.text
    soup = BeautifulSoup(html_page, 'html.parser')
    
    links = []
    for link in soup.findAll('a'):
        new_link = link.get('href')
        if is_valid(new_link) and new_link not in links:
            links.append(new_link)
    
    return links


# Recursively Extract all links
def extract_links(session, link):
    
    if link not in all_links:
        all_links.append(link)
    if link in tested_links:
        return
    
    tested_links.append(link)
    # print(f'[+] Tested - {link}')
    
    for l in FindLinksFromWebpage(session, link):
        extract_links(session, l)


# This method will act as the main method here
def RunSmeScan(_URL, _USERNAME, _PASSWORD):
    
    URL = _URL
    USERNAME = _USERNAME
    PASSWORD = _PASSWORD
    result = "Scan Result:<br>"
    
    # Login to the website
    session = login(URL, USERNAME, PASSWORD)
    
    extract_links(session, URL)
    
    # Print The links and their Status Codes
    for index, link in enumerate(sorted(all_links)):
        res = session.get(link)
        
        if index<10:
            result += f'0{index} - <b>{res.status_code}</b> > {link}<br>'
        else:
            result += f'{index} - <b>{res.status_code}</b> > {link}<br>'
    
    return result
    