from classes.Url import Url
from classes.Html import Html
from classes.FileName import FileName
from classes.FileIO import FileIO

log_path = 'logs/'
src_path = 'src/'


# read src dir to gather up URLS
try:
    src_file = FileIO(src_path + 'src_urls.txt')
    src = src_file.return_list()

    print(src)

except:
    pass

# try:
#     url = Url('http://www.google.com')
#     f_name = (FileName()).convert_url_to_filename(url,'txt',True)
# except ValueError as e:
#     print(e)
#
# html = Html(url)
# file = FileIO(log_path + f_name)
# file.write(html.get())