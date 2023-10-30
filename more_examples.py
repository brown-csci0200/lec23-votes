# more ways of looping through a list

the_list = ["a", "b", "c"]

print("For each:")
for itm in the_list:
    print(itm)

print("Using range:")
# similar to for(int i = 0; i < the_list.length; i++)
for i in range(len(the_list)): # could also write: range(0, len(the_list))
    print(the_list[i])

print("Indices and values:")
for i,num in enumerate(the_list):
    print(str(i) + ": " + str(num))

print("Backwards:")
# first input to range is inclusive, next is exclusive
for i in range(len(the_list) - 1, -1, -1):
    print(the_list[i])