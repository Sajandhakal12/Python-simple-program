'''

'''

import random

# takes filename as argument and returns tuple with list of vocabulary
def getWords(fileName):
    with open(fileName) as f:
        texts =[]
        texts = f.read().splitlines()
        return tuple(texts)

#assignment
articles=getWords('articles.txt')
nouns=getWords('nouns.txt')
prepositions=getWords('prepositions.txt')
verbs=getWords('verbs.txt')


#form a sentence
def sentence():
    return nounPhrase()+' '+verbPhrase()

#form a nounphrase    
def nounPhrase():
    return random.choice(articles)+ " " +random.choice(nouns)

#form a verb phrase       
def verbPhrase():
    return random.choice(verbs)+" "+nounPhrase()+" "+prepositionalPhrase()

#form a prepositional phrase
def prepositionalPhrase():
    return random.choice(prepositions)+ " "+nounPhrase()
    
def main():
    number=int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
        
main()