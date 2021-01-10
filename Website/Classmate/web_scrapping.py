import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.edureka.co/all-courses')
soup = BeautifulSoup(page.content, 'html.parser')
coursed = soup.find(id='add-master-courses')
items = coursed.find_all(class_='card giTrackElement giTrackElementHover')
# print(items[0].find('h3').get_text())
# print(items[0].find(class_='highlights hidden-xs').get_text())
# print(items[0].find('ul').get_text())
course_names = [item.find('h3').get_text() for item in items]
course_desc = [item.find('ul').get_text() for item in items]
# print(course_names)
# print(course_desc)

course_stuff = pd.DataFrame(
    {'course_names': course_names, 'course_desc': course_desc, }
)
print(course_stuff)
course_stuff.to_csv('coursess.csv')

