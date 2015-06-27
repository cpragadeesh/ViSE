import urllib2,cookielib

def searchURL(url):
    site= "https://www.google.co.in/searchbyimage?hl=en&biw=1438&bih=736&site=webhp&image_url={0}&sa=X&ei=j6SOVYjgIdaiugSPtZgQ&ved=0CBkQ9Q8oAA".format(url)
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    
    req = urllib2.Request(site, headers=hdr)
    page = urllib2.urlopen(req)
    content = page.read()
    return content
