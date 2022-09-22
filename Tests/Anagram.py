emplist = ['cat','act','dog','orrange','rangeor','god']

dict = {}
# keysdfs = ''.join(sorted(emplist))
# print(keysdfs)


for item in emplist:
    key = ''.join(sorted(item))
    key1 = sorted(emplist)
    # print(key1)
    if key in dict:
        dict[key].append(item)
    else:
        dict[key] = []
        dict[key].append(item)

# print(dict)
result = ""
for key,value in dict.items():
    result += ' '.join(value) + ' '
print(result)

#
# print(dict)