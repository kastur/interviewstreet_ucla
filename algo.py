import shlex
import subprocess
import urlparse
import uuid

import flickr
import wikipedia
import quote


def generate(url):
	get_name = urlparse.parse_qs(urlparse.urlparse(url).query)['name'][0]
	get_image = urlparse.parse_qs(urlparse.urlparse(url).query)['image'][0]
	get_quote = urlparse.parse_qs(urlparse.urlparse(url).query)['quote'][0]
	print get_name
	print get_image
	print get_quote

	print '>> getting image'
	image_data = flickr.get_pic(get_image)

	print '>> getting artist_name'
	artist_name = wikipedia.get_title(get_name)

	print '>> getting quote'
	song_title = quote.get_quote(get_quote)


	print '>> writing image'
	u = uuid.uuid4()
	fp = open('image-%s.jpg' % u, 'wb')
	fp.write(image_data);
	fp.close();

	print '>> visual manip'
	cmd = ['sh', 'fakealbum.sh', str(u), str(artist_name), str(song_title)]
	subprocess.call(cmd)

	print '>> returning image'
	gen_image = open('gen-%s.jpg' % u, 'rb').read();

	cmd = ['rm', 'gen-%s.jpg' % u]
  
	return gen_image;


if __name__ == "__main__":
    generate('www.localhost.com/fakealbum?name=http://en.wikipedia.org/wiki/Jewish_cuisine_(STUFF)&image=http://www.flickr.com/photos/patrick_castelli/7050134201/&quote=http://www.quotationspage.com/quote/1096.html')
