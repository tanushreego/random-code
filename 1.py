dict1={x : x*x for x in range(1,11)}
for key,value in dict1.items():
    dict1.update({key:value+5})
for key,value in dict1.items():
    print(key,value)

    



