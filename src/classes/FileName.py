import time, re
from classes.Url import Url


class FileName:
    #pass in a url and be handed back a string suitable for filename use
    def convert_url_to_filename(self, url, ext='', random=False):
        if not isinstance(ext, str):
            raise ValueError('ext needs to be of TYPE str')

        if isinstance(url, Url):
            if random:
                uniqueStr = str(time.time())
                uniqueStr = uniqueStr.split('.')

                u = self.__clean(url.get_url())
                return u + '_' + uniqueStr[0] + '.' + ext
        else:
            raise ValueError('Incorrect TYPE passed, Url expected.')

    def __clean(self,string):
        string = re.sub('(http)(s)?(://)','',string)
        string = re.sub('[\.]','_',string)
        return string