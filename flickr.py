import urllib
import json

def get_pic(url):
  if url[-1] == '/': url = url[:-1]
  photo_id = url.split('/')[-1]
  print photo_id
  fp = urllib.urlopen(
    "http://api.flickr.com/services/rest/" +
    "?method=flickr.photos.getSizes" +
    "&api_key=72b8c51a1f09f08bc9332fcf5ee65f03" +
    "&photo_id=" + photo_id +
    "&format=json" +
    "&nojsoncallback=1");
  repl_str = fp.read()
  repl_json = json.loads(repl_str)

  largest_image = repl_json['sizes']['size'][-1]['source']

  repl_json['sizes']['size'][-1]['source']


  fp = urllib.urlopen(largest_image);
  
  image_data = fp.read()

  return image_data

if __name__ == '__main__':
  get_pic('http://www.flickr.com/photos/weedobooty/7031679837/')

