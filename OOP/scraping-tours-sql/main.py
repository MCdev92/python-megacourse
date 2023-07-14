import os
import time
import sqlite3
import requests
import selectorlib
import smtplib, ssl



URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


# Events become a class and the two functions become methods
class Event:
    def scrape(self, url):
        """Scrape the page source from the URL"""
        response = requests.get(url)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("Intermediate/scraping-tours-sql/extract.yaml")
        value = extractor.extract(source)["tours"]
        return value


class Email:
    def send(self, message):
        host = "smtp.gmail.com"
        port = 465

        username = "corporancarriers@gmail.com"
        password = os.getenv("PASSWORD")

        receiver = "corporan.manuel@yahoo.com"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
        print("Email was sent!")
 
class Database:   
   
    def __init__(self, database_path): 
        self.connection = sqlite3.connect("OOP/scraping-tours-sql/data.db")
        
    def store(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
        self.connection.commit()
        
    def read(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band, city, date = row
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
        rows = cursor.fetchall()
        print(rows)
        return rows

      
if __name__ == "__main__":
    while True:
        event = Event() # Event class called
        scraped = event.scrape(URL) # scrape will become an instant
        extracted = event.extract(scraped) # extract will become an instant
        print(extracted)
        
        if extracted != "No upcoming tours":
             database = Database(database_path="OOP/scraping-tours-sql/data.db")
             row = database.read(extracted)
             if not row:
                database.store(extracted)
                email = Email() # Email class called
                email.send(message="Hey, new event was found!")
        time.sleep(2)
        
    