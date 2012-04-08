import re
import random
import nltk
import textwrap

def tsplit(string, *delimiters):
  pattern = '|'.join(map(re.escape, delimiters))
  return re.split(pattern, string)

def parse_grammar(tags, grammar, title_candidates):
  cp = nltk.RegexpParser(grammar)
  result = cp.parse(tags)
  for node in result:
    if type(node) is nltk.tree.Tree and node.node == 'NP':
      title_candidates.append(zip(*node.flatten())[0])

def trim_quote(quote):
  title_candidates = []
  tokens  = nltk.word_tokenize(quote)

  tags = nltk.pos_tag(tokens)
  print tags

  parse_grammar(tags, "NP: {<DT>?<JJ>+<NN>+}", title_candidates)
  parse_grammar(tags, "NP: {<JJ><NN>+}", title_candidates)
  parse_grammar(tags, "NP: {<VBP><NN>+}", title_candidates)
  parse_grammar(tags, "NP: {<IN><.*>+?<NN>+}", title_candidates)
  parse_grammar(tags, "NP: {<WP><.*>+?<JJ>+}", title_candidates)
  parse_grammar(tags, "NP: {<WP><.*>+?<IN>}", title_candidates)
  parse_grammar(tags, "NP: {<RB.*><.*>+?<JJ>+}", title_candidates)

  if len(title_candidates) == 0:
    parse_grammar(tags, "NP: {<NN.*>+}", title_candidates)
  #cp = nltk.RegexpParser(grammar)
  #result = cp.parse(tags)

  #for node in result:
  #  if type(node) is nltk.tree.Tree and node.node == 'NP':
  #    title_candidates.append(zip(*node.flatten())[0])

  str_quote = ' '.join(random.choice(title_candidates))
  return '\n'.join(textwrap.wrap(str_quote, 20))


def trim_quote_old(quote):
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
  print trim_quote('dog')
  print trim_quote('If you pick up a starving dog and make him prosperous, he will not bite you. This is the principal difference between a dog and a man.')
  print trim_quote('A fact is a simple statement that everyone believes. It is innocent, unless found guilty. A hypothesis is a novel suggestion that no one wants to believe. It is guilty, until found effective.')
  print trim_quote('If you want to be free, there is but one way; it is to guarantee an equally full measure of liberty to all your neighbors. There is no other.')
  print trim_quote('I know not with what weapons World War III will be fought, but World War IV will be fought with sticks and stones.')
  print trim_quote('Be entirely tolerant or not at all; follow the good path or the evil one. To stand at the crossroads requires more strength than you possess.')
  print trim_quote('For most folks, no news is good news; for the press, good news is not news.')
  print trim_quote('A man cannot be too careful in the choice of his enemies.')
  print trim_quote('Anyone who works is a fool. I don\'t work - I merely inflict myself upon the public.')
  print trim_quote("It's not that I'm afraid to die, I just don\'t want to be there when it happens.")
  print trim_quote('If you want change, you have to make it. If we want progress we have to drive it.')
  print trim_quote("Any ordinary favor we do for someone or any compassionate reaching out may seem to be going nowhere at first, but may be planting a seed we can't see right now. Sometimes we need to just do the best we can and then trust in an unfolding we can't design or ordain.")

