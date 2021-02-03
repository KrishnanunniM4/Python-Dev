

a = 5
b = 2
if a > b:
    print("a is grater than b")
else:
    print("a is less than b")

x = "Hello"
print(type(x))

fruits = ["apple", "orange", "grapes"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("python is " + x)

import random
print(random.randrange(1,10))

for x in "krishnanunni":
    print(x)

x = "Hello World"
y = "sup"
if y in x:
    print("Present")
else:
    print("Not Present")

x = "Hello,World"
#print(x.upper())
#x.lower
#x.strip
#x.replace
#print(x.split(","))

quantity = 36
itemno = 458
price = 25
txt = "I want to pay {2} for {0} quantity of item {1}"
print(txt.format(quantity,itemno,price))

x = "My Name is Dev"
y = x.split(" ")
z = "-".join(y)
print(z)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
thislist.insert(2, "peach")
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist.append("orange")
print(thislist)

list_one = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list_two = ["blackcurrant", "watermelon"]
list_one.extend(list_two)
print(list_one)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
#thislist.remove("kiwi")
#thislist.pop(2)
#del thislist[3]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
#for x in thislist:
#    print(x)
#for i in range(len(thislist)):
#    print(thislist[i])
i = 0
while i < len(thislist):
    print(thislist[i])
    i+=1

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
#newlist = []
#for x in thislist:
#    if "a" in x:
#        newlist.append(x)
#print(newlist)
#newlist = [x for x in thislist if "a" in x]
#newlist = [x if x != "banana" else "watermelon" for x in thislist]
newlist = [x.upper() for x in thislist]
print(newlist)

thislist = ["apple", "Banana", "cherry", "Orange", "kiwi", "mango"]
#thislist.sort()
#thislist.sort(reverse = True)
thislist.sort(key = str.lower)
print(thislist)

thislist = ["apple", "Banana", "cherry", "Orange", "kiwi", "mango"]
newlist = thislist.copy()
print(newlist)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(x, y, *z) = fruits
print(x)
print(y)
print(z)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

thisset = {"apple", "banana", "cherry"}
#thisset.remove("banana")
thisset.discard("banana")
print(thisset)

set_one = {"apple", "mango", "orange"}
set_two = {"google", "facebook", "apple"}
#set_one.update(set_two)
#set_three = set_one.union(set_two)
#set_three = set_one.intersection(set_two)
#set_three = set_one.difference(set_two)
set_three = set_one.symmetric_difference(set_two)
print(set_three)

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1984
}
#x = thisdict["model"]
x = thisdict.get("model")
#txt = "the model is {}"
#print(txt.format(x))
x = thisdict.keys()
#thisdict["color"] = "Red"
#print(x)
y = thisdict.values()
thisdict["color"] = "Yellow"
#print(y)
z = thisdict.items()
#print(z)
thisdict.update({"year" : 2004})
#print(thisdict)
thisdict.pop("year")
#print(thisdict)
#thisdict.clear()
#for x, y in thisdict.items():
    #print(x, y)
mydict = thisdict.copy()
#print(mydict)

def recursion(k):
    if(k > 0):
        result = k + recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("Results\n")
recursion(6)
