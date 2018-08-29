from urllib.parse import urlparse


#this class will compare a site url and a tag - eg a tag, img tag
#and determine if they are from the same url, and if they are https secure

class LinkAnalyzer:
    is_local = True
    site_is_https = False
    tag_is_https = False
    tag_is_insecure_content = False
    siteUrl = ''
    tagUrl = ''


    def __init__(self, siteUrl, aTag):
        self.tagUrl = urlparse(aTag.get_url())
        self.tag_is_https = self.isHttps(self.tagUrl)

        self.siteUrl = urlparse(siteUrl.get_url())
        self.site_is_https = self.isHttps(self.siteUrl)

        #confirm if tag is secure
        if(self.tag_is_https == False):
            self.tag_is_insecure_content = True

        #check if both are http/https match
        if(self.tagUrl.scheme != self.siteUrl.scheme):
            self.is_local = False

        #check if both are http/https match
        if(self.tagUrl.netloc != self.siteUrl.netloc):
            self.is_local = False


    def isHttps(self, u):
        return bool(u.scheme == 'https')