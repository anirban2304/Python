import requests
from bs4 import BeautifulSoup

r = requests.get("http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers = {'User-agent':'Morzilla/5.0(X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

c = r.content
soup = BeautifulSoup(c, "html.parser")
properties = soup.find_all("div", {"class":"propertyRow"})
for property in properties:
    price = property.find("h4", {"class":"propPrice"}).text.replace("\n", "").replace(" ", "")
    print(price)