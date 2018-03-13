from classes.Url import Url
from classes.Html import Html
from classes.FileName import FileName

url = Url()
log_path = 'logs/'

try:
    url.set_url('http://www.google.com')
    f_name = (FileName()).convert_url_to_filename(url,'txt',True)
except ValueError as e:
    print(e)

html = Html(url)

try:
    file = open(log_path + f_name, 'w')
    file.write(str(html.get()))
except IOError:
    pass