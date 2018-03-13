import urllib, re

class Url():
    #sets the URL
    def set_url(self, url):
        if self.url_check(url):
            self.url=url

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