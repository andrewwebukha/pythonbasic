#concatenation using a plus operator, using .format
first_name = "Andrew"
last_name = "Webukha"
#full_name ="{} {}".format(first_name,last_name)
#print(full_name)
print("The tallest person in the family of {} is named after {}".format(last_name,first_name))
#full_name= first_name+" "+last_name
#print(full_name)

name= "John Juma"
name2= "kevin kirimi"
name3= "FABIAN KEN"
print (name.capitalize())
print(name2.title())

sen= "man is to error because man did not create man"
print(sen.count("man"))
print(sen.count(" "))
print(sen.count("e"))
#python is case sensitive
#string slicing
#in slicing left of the colon signifies the starting element. right of the colon signifies the ending position but the end element is excluded
print(sen[0])
print(sen[-1])
print(sen[0:2])
print (sen.__len__())
jina= "muyani"
print(jina[1:2])
print(jina[::-1])
#print(jina[5:3:-1])
#split
print(sen.split())