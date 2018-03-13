from classes.url import Url
from classes.html import Html

url = Url()

try:
    url.setUrl('http://www.google.com')
except ValueError as e:
    print(e)

#html = Html(url.getUrl())
html = Html(url)
print(html.get())