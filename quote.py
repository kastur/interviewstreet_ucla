import urllib, urllib2
from BeautifulSoup import BeautifulSoup
from quote_trim import trim_quote

def get_quote(url):
    # get list of subjects
    req = urllib2.Request(url)
    quote_soup = BeautifulSoup(urllib2.urlopen(req))
    quote = quote_soup.findAll('blockquote')[0].findChildren('dt')
    return trim_quote(quote[0].contents[0])

if __name__ == "__main__":
    print get_quote('http://www.quotationspage.com/quote/1474.html');
    print get_quote('http://www.quotationspage.com/quote/1096.html');
