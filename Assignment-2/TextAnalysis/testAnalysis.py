'''
'''

# Takes teh inputs
fileName= input("Enter the file name: ")
inputFile= open(fileName,'r')
text = inputFile.read()

#count the sentences
sentences = text.count('.') + text.count('?') + text.count(':') + text.count(';')+text.count('!')

#count the words
words = len(text.split())

#count the syllables
syllables = 0
vowels = 'aeiouAEIOU'
for word in text.split():
    for vowel in vowels:
        syllables += word.count(vowel)
    for ending in ['es','ed','e']:
        if word.endswith(ending):
            syllables -=1
    if word.endswith('le'):
        syllables +=1


#compute teh Flesch Index and Grade Level
index = 206.835 - 1.015 * (words/sentences) - 84.6 * (syllables/words)
level = round(0.39 * (words/sentences)+11.8*(syllables/words)-15.59)

#output the results
print('The Flesch Index is',index)
print("The Grade level equivalent is ",level)
print(sentences, 'sentences')
print(words,'words')
print(syllables,'syllables')