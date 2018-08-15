import string 

f = open("wordlist.txt", "r")

words =f.read().splitlines()

# the code below does not work as the empty array is a reference so one array is used by all keys
# d = dict.fromkeys(string.ascii_lowercase, [])
# this is the way to do it
# d = { key : [] for key in keys }

keyed_words = [ 
        {
            'word': word,
            'key': word.lstrip(string.punctuation)[0],
        } for word in words if word.lstrip(string.punctuation) ]

# build keys list from existing keys with a-z as minimum
# keys = set([ word['key'] for word in keyed_words ] + list(string.ascii_lowercase) )

# build keys from a-z plus digits, allows for keys to be deterministic but ...
# is possible for content editor to add a title which starts with a char not in the keys which will throw an error
keys = list(string.ascii_lowercase + string.digits)

d = {}

for key in keys:
    d[key] = sorted([ kw['word'] for kw in keyed_words if kw['key'] == key ])

for key, value in sorted(d.items()):
    print key, value

