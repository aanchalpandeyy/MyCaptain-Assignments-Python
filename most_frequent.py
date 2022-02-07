test_str = "Mississippi"
res = {}
for keys in test_str:
	res[keys] = res.get(keys, 0) + 1
print ("Count of all characters in Mississippi is : \n" + str(res))