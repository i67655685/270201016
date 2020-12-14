books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]

book_dict = {}
"""" THE SOLUTİON
for i in range(len(books)):
  key = books[i]
  characters = len(key)
  unique_characters = len(set(key))
  value = (characters, unique_characters)
  book_dict[key] = value

print(book_dict)
"""