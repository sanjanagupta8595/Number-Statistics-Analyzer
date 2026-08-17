topic = "PROJECT ON NUMBER STATISTIC CALCULATOR"
print(topic.center(50))

n = int(input("HOW MANY NUMBERS DO YOU WANT TO ENTER : "))
total =0
average = 0
even_num = 0
odd_num = 0
for i in range(1,n+1):
        val = int(input("Enter NUMBER : "))
        total = total+val
        average = total/n
        if i==1:
             maximum = val
             minimum = val
        else:
            if val>maximum :
                maximum = val
            if val < minimum:
                minimum = val


        if val%2==0:
                  even_num+=1
        else:
             odd_num+=1
     
print ("total : ",total)
print("average : ",average)
print("maximum number : ",maximum)
print("minimum number : ",minimum)
print("Even Number : ", even_num)
print("Odd Number : ",odd_num)


print("SUCCESSFULL!!!")
       