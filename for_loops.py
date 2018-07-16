seq = [1,2,3,4,5,6]

for item in seq:
    print(item)

d = {"sam":1, 
    "Frank":2
}
for jelly in d:
    print(jelly) #print the keys without ordering
    print(d[jelly]) # print the keys only

mypairs = [(1,2), (3,4), (5,6)]
for t1,t2 in mypairs:
    print(t1) # to unpack the tupple

i = 1
while i<5:
    print("i is: {}".format(i))
    i = i+1