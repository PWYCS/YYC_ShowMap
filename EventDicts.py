# For each event on the Palace Theatre website, scrape the event name, date, time, and description. Store this information in a dictionary, then write it to a csv after each event has been scraped.

from bs4 import BeautifulSoup
import requests
import pickle
import sys
import os.path
import re
import pandas as pd


# Redirect stdout to a file
sys.stdout = open('stdout.md', 'w', encoding='utf-8')

pickle_file = 'c:/Users/trist/Documents/Projects/YYC_ShowMap/_cache/r.pickle'

if os.path.exists(pickle_file):
    with open(pickle_file, 'rb') as f:
        r = pickle.load(f)
else:
    r = requests.get("https://www.thepalacetheatre.ca/events")
    with open(pickle_file, 'wb') as f:
        pickle.dump(r, f)

if r:
    print("Success")
else:
    with open('_cache/scrape.html', 'w', encoding='utf-8') as f:
        f.write(r.content.decode('utf-8'))


soup = BeautifulSoup(r.content, "lxml")

event_info_list = []
eventlist_column_date_divs = soup.find_all("div", class_="eventlist-column-info")
for div in eventlist_column_date_divs:
    children = div.findChildren()
    for child in children:
        if child.name == 'h1' and 'eventlist-title' in child.get('class', []):
            event_name = child.get_text()
            event_logistics = child.find_next_sibling().get_text()
            event_description = child.find_next_sibling().find_next_sibling().get_text()
            event_info_list.append([event_name, event_logistics, event_description])
        if child.name == 'div' and 'sqs-block-button-container' in child.get('class', []):
            ticket_link = child.find('a').get('href')
            event_info_list[-1].append(ticket_link)

event_info_df = pd.DataFrame(event_info_list, columns=['Event Name', 'Logistics', 'Description', 'Ticket Link'])
print(event_info_df.to_html())

            #event_info_dict[event_name]['date'] = child.find_next_sibling().get_text()
            #event_info_dict[event_name]['time'] = child.find_next_sibling().find_next_sibling().get_text()
            #event_info_dict[event_name]['description'] = child.find_next_sibling().find_next_sibling().find_next_sibling().get_text()




# eventlist_column_date_divs = soup.find_all("div", class_="eventlist-column-info")
# for div in eventlist_column_date_divs:
#     children = div.findChildren()
#     for child in children:
#         if child.name == 'h1' and 'eventlist-title' in child.get('class', []):
#             event_name = child.get_text()
#             event_info_dict[event_name] = {}
#             event_info_dict[event_name]['date'] = child.find_next_sibling().get_text()
#             event_info_dict[event_name]['time'] = child.find_next_sibling().find_next_sibling().get_text()
#             event_info_dict[event_name]['description'] = child.find_next_sibling().find_next_sibling().find_next_sibling().get_text()
# print(event_info_dict)

    #print(div.get_text())




# for tag in soup.find_all("eventlist-column-info"):
#     print(tag.name + " " + str(tag.attrs))
# for tag in soup.find_all(True):
#     print(tag.name + " " + str(tag.attrs))
# for tag in soup.find_all(re.compile("event")):
#     print(tag.name)
#print(soup.find_all('div', class_='eventlist-column-info'))
#print(soup.find_all('a', class_='eventlist-title-link'))
#print(soup.find_all('div', class_='sqs-html-content'))
#print(soup.body.children.prettify())
#for child in soup.body.descendants:
#    print(child)

#print(soup.body.descendants)



# Restore stdout
sys.stdout = sys.__stdout__

# APP ABOVE
#############################################################
# BLESS THIS MESS BELOW


# print(soup.get_text())
# for link in soup.find_all('a'):
#     print(link.get('href'))

#print(soup.p['eventlist-column-info'])#['eventlist-column-info'])

#print(soup.prettify())

# classes = [value
#            for element in soup.find_all(class_=True)
#            for value in element["class"] if value ]
# print(classes), print(len(classes))

# event_info_elements = soup.findall(class='')
