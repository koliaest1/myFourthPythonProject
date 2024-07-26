# the list with words from string
# please, do not modify it
some_iterable = input().split()
dictionary = {}
for i in some_iterable:
    dictionary[i.upper()] = i.lower()
print(dictionary)
