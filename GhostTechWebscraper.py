from bs4 import BeautifulSoup
import requests as req
website = req.get('https://www.ghosttechsolutions.com/about-us/')
S = BeautifulSoup(website.content,'html5lib')
title = S.title
text = (S.find('p'))
with open('ghosttechparsedwebsiteinfo.html','w') as f:
    f.write(str(title.string))
    f.write(str(S.find('cite')))
    f.write(str(text))
    f.close()
filename ='file:///Users/18325/Documents/AdvancedBusinessProgramming/' + 'ghosttechparsedwebsiteinfo.html'