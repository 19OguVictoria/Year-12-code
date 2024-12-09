list1 = [34,56,34,26,80,57,98,100,80,64,102,300,35,6,87,88]

count = 0

for i in range 0 to (len.list1 – 1):

    if (list1[i] >=80) AND (list1[i] <=100):

        count = count + 1

print ((“Number of integers in  the range 80-100”) + count)

for i in range 0 to (len.list1 – 1):

      if (list1[i] >=80) and (list1[i] <=100):

        item = list1[i]

        list1.remove(item)


print(list1)