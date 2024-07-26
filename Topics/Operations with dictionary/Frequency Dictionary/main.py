# put your python code here
word = input().lower()
list_of_words = word.split()
dict_result = dict.fromkeys(list_of_words, 0)
for i in list_of_words:
    if i in dict_result.keys():
        dict_result[i] += 1
for key, value in dict_result.items():
    print(key, value)
