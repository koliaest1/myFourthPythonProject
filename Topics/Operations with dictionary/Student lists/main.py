import operator
student_list_sorted = dict(sorted(student_list.items(), key=operator.itemgetter(1)))    
print(list(student_list_sorted.keys())[0])
