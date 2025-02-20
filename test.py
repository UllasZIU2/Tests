lst = []
cg = 0
coursecount = 0
rc = 0
c= input("course name and cg - ").split(" ")
if c[0] not in lst:
        lst.append(c[0])  
        cg += int(c[1])
        coursecount += 1
else:
        rc += 1
        print("Course already added")

print(lst)
print(cg)
print(coursecount)
print(rc)

