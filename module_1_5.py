from idlelib.pyshell import ModifiedInterpreter

immutable_var = 1, "apple", True,
print(immutable_var)
print(type(immutable_var))
#immutable_var.remove("apple") 'tuple' object has no attribute 'remove'
#print(immutable_var)
a = 3
b = 4
c = 5
x = 6
y = 7
z = 8
Modifiedlist = 'tuple_'
mutable_list = 1, 2, "mango",False, [a,b,c], Modifiedlist
mutable_list[4][0] = x
mutable_list[4][1] = y
mutable_list[4][2] = z
print(mutable_list)
