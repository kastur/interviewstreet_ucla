import random

FREQ = .25
THRESHOLD = 5

def get_title(name):
    title = name.split('/')[-1]
    title = title.replace('_', ' ')
    title = title.split('(')[0].lstrip().rstrip()

    words = title.split(' ')
    if len(words) < THRESHOLD:
        return title

    new_title = ""
    for word in words:
        if random.random() > FREQ:
            new_title = new_title + " " + word
    
    return new_title

if __name__ == "__main__":
    print get_title('http://en.wikipedia.org/wiki/__Jewish_cuisine_1_2_3_4_5___(STUFF)');
