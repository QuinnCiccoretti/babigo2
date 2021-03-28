def newPhrase():
  return { 'start_time': '', 'end_time': '', 'text' : "" }

def getEnglishPhrases( ts ):
  items = ts['results']['items']
  #print( items )
  
  #set up some variables for the first pass
  phrase =  newPhrase()
  phrases = []
  nPhrase = True
  x = 0
  c = 0
  words_per_phrase = 5
  if(len(items) < 5):
    words_per_phrase = 2

  for item in items:

    # if it is a new phrase, then get the start_time of the first item
    if nPhrase == True:
      if item["type"] == "pronunciation":
        phrase["start_time"] = float(item["start_time"])
        nPhrase = False
      c+= 1
    else: 
      # get the end_time if the item is a pronuciation and store it
      # We need to determine if this pronunciation or puncuation here
      # Punctuation doesn't contain timing information, so we'll want
      # to set the end_time to whatever the last word in the phrase is.
      if item["type"] == "pronunciation":
        phrase["end_time"] = float(item["end_time"])
        
    # in either case, append the word to the phrase...
    phrase["text"] += (item['alternatives'][0]["content"]) + " "
    x += 1
    
    # now add the phrase to the phrases, generate a new phrase, etc.
    if x == words_per_phrase:
      #print c, phrase
      # phrase.text = phrase['text'].trim()
      phrases.append(phrase)
      phrase = newPhrase()
      nPhrase = True
      x = 0
      
  return phrases
