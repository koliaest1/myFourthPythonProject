# The following line creates a dictionary from the input. Do not modify it, please
import operator
test_dict = json.loads(input())
print("min:", min(test_dict.items(), key=operator.itemgetter(1))[0])
print("max:", max(test_dict.items(), key=operator.itemgetter(1))[0])
