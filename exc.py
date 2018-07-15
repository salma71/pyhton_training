# problem_1
s = 'django'

# use indexing to print out 
# 'd'
# 'o'
# 'djan'
# 'jan' 
# 'go' 

print(s[:1])
print(s[5:])
print(s[:4])
print(s[1:4])
print(s[4:])
print(s[::-1])

# problem 2
l = [3,7,[1,4,'hello']]
# reassign "hello" to be 'goodbye'
l[2][2] = "goodbye"
print(l)

# problem 3

d1 = {'simple_key': 'hello'}

d2 = {'k1':{'k2': 'hello'}}

d3 = {'k1':[{'nest_key':['this is deep', ['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1])