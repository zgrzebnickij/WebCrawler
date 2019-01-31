import requests
import sys
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def site_map(url):
  """
  key: URL
  * value: dictionary with:
  ** site title (HTML `<title>` tag)
  ** links - set of all target URLs within the domain on the page but without anchor links
  some links may be invalid
  """
  stack = [url]
  visited = [url]
  urlDict = {}
  while stack:
    links = set()
    url = stack.pop()
    try:
      r = requests.get(url)
    except:
      print(f"Wrong url:{url}",file=sys.stderr)
      return 0
    if(r.status_code==200):
      netlocation = urlparse(url).netloc
      soup = BeautifulSoup(r.text, features="html.parser")
      siteurl = url
      for link in soup.find_all('a'):
        url = link.get('href')
        parsed = urlparse(url)
        if parsed.netloc == "":
          path = urljoin(siteurl, parsed.path)
          links.add(path)
          if path not in visited:
            stack.append(path)
            visited.append(path)
        elif parsed.netloc == netlocation:
          path = parsed.geturl()
          links.add(path)
          if path not in visited:
            stack.append(path)
            visited.append(path)
      title = soup.title.string if soup.title else "No title or links"
      urlDict[siteurl]={"title":title, "links":links} 
    else:
      pass
  for keys,values in urlDict.items():
    print(keys)
    print(values)



if __name__ == "__main__":
  a = "http://0.0.0.0:8000/"
  b = "http://127.0.0.1:5000/" ## my site
  site_map(b)