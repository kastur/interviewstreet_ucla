import re
import random
def tsplit(string, *delimiters):
  pattern = '|'.join(map(re.escape, delimiters))
  return re.split(pattern, string)

def trim_quote(quote):
  f = open('prepositions.txt')
  preps = {}
  for prep in f.readlines():
    preps[prep] = True

  quotes = []
  sentences = tsplit(quote, '.',';','!',',')
  for sentence in sentences:
    words = sentence.split(' ')
    quote = ""
    flag = False

    for word in words:
      if preps.has_key(word+'\n'):
        if not flag:
          flag = True
          quote = word + ' '
        else:
          break
      else:
        quote = quote + word + ' '
    quote = quote.lstrip().rstrip()

    if len(quote) > 3:
        quotes.append(quote.lstrip().rstrip())

  return random.choice(quotes)

if __name__ == '__main__':
  print trim_quote('If you pick up a starving dog and make him prosperous, he will not bite you. This is the principal difference between a dog and a man.')
