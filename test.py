from BeautifulSoup import  BeautifulSoup
source_code = '"""<span class="UserName"><a href="#">Martin Elias</a></span>"""'
soup = BeautifulSoup(source_code)
print(soup.find('span',{'class':'UserName'}).text)