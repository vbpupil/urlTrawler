from classes.Url import Url
from classes.Html import Html
from classes.FileName import FileName
from classes.FileIO import FileIO
from classes.HtmlParse import HtmlParse
import traceback, time
from urllib.parse import urlparse

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
                b = urlparse(url.get_url())
                print(b)
            except ValueError as e:
                print(e)

            #lets get the html from the page
            html = Html(url)

            #pass into a the htmlparser
            parser = HtmlParse(html.get())

            #search for
            tags = {}
            tags['a'] = parser.findAll('a', 'href')
            tags['img'] = parser.findAll('img', 'src')
            # tags['audio'] = parser.findAll('audio', 'src')
            # tags['embed'] = parser.findAll('embed', 'src')
            # tags['form'] = parser.findAll('form', 'action')
            # tags['iframe'] = parser.findAll('iframe', 'src')
            # tags['object'] = parser.findAll('object', 'src')
            # tags['param'] = parser.findAll('param', 'src')
            # tags['script'] = parser.findAll('script', 'src')
            # tags['source'] = parser.findAll('source', 'src')
            # tags['video'] = parser.findAll('video', 'src')

            # print(tags)

            #write tags to file
            file = FileIO(log_path + f_name)

            file.write('**A TAGS**\n', 'a')

            for tag in tags['a']:
                file.write(tag+'\n', 'a')

            file.write('\n\n**IMG TAGS**\n', 'a')

            for tag in tags['img']:
                file.write(tag+'\n', 'a')

            #increase site count
            site_count += 1

    print(str(site_count) + " sites read in", (time.time() - start_time), " seconds")
except Exception as e:
    print(traceback.format_exc())