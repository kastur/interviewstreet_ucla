import urllib
import json

def parse_flickr(photo_id):
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

  fp = urllib.urlopen(largest_image);
  
  image_data = fp.read()
  op = open('image.jpg', 'wb');
  op.write(image_data);
  return image_data

  print largest_image

if __name__ == '__main__':
  parse_flickr('7031679837')

