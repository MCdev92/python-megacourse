import requests
from send_email import send_email

api_key = "25c6584d66ee45598295501ada567930"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-06-08&sortBy=publishedAt&apiKey=25c6584d66ee45598295501ada567930"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
    
