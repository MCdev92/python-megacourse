import requests

api_key = "25c6584d66ee45598295501ada567930"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-06-08&sortBy=publishedAt&apiKey=25c6584d66ee45598295501ada567930"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])