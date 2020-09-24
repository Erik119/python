ages = [9, 17, 18, 19, 23, 24]

def myfunc(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(myfunc, ages)

for x in adults:
    print(x)

print('+=' * 40)

#now with lambda:

adults = filter(lambda x: x > 17, ages)
for adult in adults:
    print(adult)    


print('+=' * 40)
print('adder')
add = lambda x,y: x+y
print(add(3,4))

print('+=' * 40)
print('sorter')
names=['marja', 'tessa', 'Erik', 'Mika', 'Opa', 'Oma']
tuples = tuple(zip(names, ages))
print(sorted(tuples,key=lambda x: x[1]))
print(sorted(tuples,key=lambda x: x[0]))