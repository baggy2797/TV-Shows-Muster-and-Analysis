from lxml import html
import lxml.etree
from io import StringIO
from requests import get
import json
import sys
import time
from selenium import webdriver
from pymongo import MongoClient
from sshtunnel import SSHTunnelForwarder
from selenium.webdriver.chrome.options import Options

# Chrome browser display options
chrome_options = Options()  
chrome_options.add_argument("--headless")

# Credentions to connect VM
MONGO_HOST = "128.226.28.176"
MONGO_USER = "vbhosal1"
MONGO_PASS = "FKymiLv13"

# Setting up HOST connection
server = SSHTunnelForwarder(
    MONGO_HOST,
    ssh_username=MONGO_USER,
    ssh_password=MONGO_PASS,
    remote_bind_address=('127.0.0.1', 27017)
)

server.start()
# Connecting to MongoDB
client = MongoClient('127.0.0.1', server.local_bind_port)
# Connecting to database 
db = client["IMDB"]

# Opening Chrome browser
driver = webdriver.Chrome("D:\DS_project\chromedriver_win32 (1)\chromedriver.exe",chrome_options = chrome_options)
parser = lxml.etree.HTMLParser()

# Connecting to collection of database
Collection = db["tv_show"] 

# Fetchng and storing list of all Tv shows title
list_of_tv_shows = [line.rstrip('\n') for line in open("List_of_Tv_show.txt")]

# Array list to store Tv shows information
tv_shows_arr = []

counter = 1
# Looping through list of Tv shows title
for tv in list_of_tv_shows:
    # OMDb api call for each Tv show
    url = 'http://www.omdbapi.com/?t='+tv+'&apikey=2272ca8b'
    # Requesting the url link for Tv show
    response = get(url)
    # Converting into json string document
    result = json.loads(response.content)
    # Condition to check if such key present in the json file
    if('imdbID' in result):
        # Fetching imdbID of Tv show
        tv_show_id = result['imdbID']
        # Url parsing with specific Tv show ID to get reviews
        imdb_url = 'https://www.imdb.com/title/'+tv_show_id+'/reviews/'
        driver.get(imdb_url)

        # Looping through website and clicking the LOAD MORE button
        while True:
            try:
                loadMoreButton = driver.find_element_by_xpath("//button[@class ='ipl-load-more__button']")
                time.sleep(1)
                loadMoreButton.click()
                print(counter)
                counter = counter+1
            except Exception as e:
                print(e)
                break
        
        # Converting HTML page to lxml tree
        driver.find_element_by_xpath("//*")
        html = driver.execute_script("return document.documentElement.outerHTML")
        tree = lxml.etree.parse(StringIO(html), parser)

        # Parsing the url to fetch reviews of Tv show
        tv_reviews = tree.xpath('//div[@class="text show-more__control"]/text()')
        # Appending the reviews to OMDb api result  
        result['review'] = tv_reviews
        # Storing all the info of Tv show in list
        tv_shows_arr.append(result)   
    else:
        continue

# Writing the result in json file
with open('imdb_TvShows_data.json', 'w', encoding='utf-8') as f:
    json.dump(tv_shows_arr, f, ensure_ascii=False, indent=4)


with open('imdb_TvShows_data.json','r', encoding='utf-8') as file: 
    file_data = json.load(file) 
      
# Inserting the loaded data in the Collection 
# if JSON contains data more than one entry 
# insert_many is used else inser_one is used 
if isinstance(file_data, list): 
    Collection.insert_many(file_data)   
else: 
    Collection.insert_one(file_data)

server.stop() 
sys.exit()
    

