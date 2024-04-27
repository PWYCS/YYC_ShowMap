import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.thepalacetheatre.ca/events")

print(r.content)

soup = BeautifulSoup(r.content, "html.parser")

print(soup.prettify())

classes = [value
           for element in soup.find_all(class_=True)
           for value in element["class"]

# event_info_elements = soup.findall(class='')

event_info_dict = {"EventInfo": []}