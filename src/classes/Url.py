import re
from urllib.parse import urlparse


class Url():
    def __init__(self, url):
        self.set_url(url)

    #sets the URL
    def set_url(self, url):
        if self.url_check(url):
            parsed=urlparse(url)
            self.url = parsed.scheme + '://' + parsed.netloc
            self.scheme = parsed.scheme
            self.query = parsed.query
            self.path = parsed.path
            self.params = parsed.params
            self.netloc = parsed.netloc

    #returns the set URL
    def get_url(self):
        return self.url

    #verifies if url is present and also that its a valid url
    def url_check(self,url):
        if url:
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url):
                return True
            else:
                raise ValueError('Not a valid URL.')
        else:
            raise ValueError('No URL set.')