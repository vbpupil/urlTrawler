import urllib, re

class Url():
    #sets the URL
    def setUrl(self, url):
        if self.urlCheck(url):
            self.url=url

    #returns the set URL
    def getUrl(self):
        return self.url

    #verifies if url is present and also that its a valid url
    def urlCheck(self,url):
        if url:
            if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url):
                return True
            else:
                raise ValueError('Not a valid URL.')
        else:
            raise ValueError('No URL set.')