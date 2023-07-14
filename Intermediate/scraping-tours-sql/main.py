import os
import time
import requests
import selectorlib
import smtplib, ssl



URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("Intermediate/scraping-tours-sql/extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "corporancarriers@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "corporan.manuel@yahoo.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

 
    
def store(extracted):
    with open("Intermediate/scraping-tours-sql/data.txt", "a") as file:
        file.write(extracted + "\n")
        

def read(extracted):
    with open("Intermediate/scraping-tours-sql/data.txt", "r") as file:
        return file.read()
    
       
if __name__ == "__main__":
   scraped = scrape(URL)
   extracted = extract(scraped)
   print(extracted)
   
   content = read(extracted)
   if extracted != "No upcoming tours":
       if extracted not in "Intermediate/scraping-tours-sql/data.txt":
        store(extracted)
        send_email(message="Hey, new event was found!")
        
    