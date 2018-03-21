from classes.Url import Url
from classes.Html import Html
from classes.FileName import FileName
from classes.FileIO import FileIO
from classes.HtmlParse import HtmlParse
import traceback, time

start_time = time.time()

log_path = 'logs/'
src_path = 'srcfile/'
site_count = 0

# read srcfile dir to gather up URLS
try:
    src_file = FileIO(src_path + 'src_urls.txt')
    src = src_file.return_list()

    if isinstance(src, list):
        for url in src:
            try:
                url = Url(url)
                f_name = (FileName()).convert_url_to_filename(url, 'txt', True)
            except ValueError as e:
                print(e)

            #lets get the html from the page
            html = Html(url)

            #pass into a the htmlparser
            parser = HtmlParse(html.get())

            print(parser.findAll('a', 'href'))


            file = FileIO(log_path + f_name)
            file.write(html.get())

            site_count += 1

    print(str(site_count) + " sites read in", (time.time() - start_time), " seconds")
except Exception as e:
    print(traceback.format_exc())

