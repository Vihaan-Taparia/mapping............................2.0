#ACTIVITY 1
#HANDS ON MAP
#add two lists using map and lambdas
numbers1=[1,2,3]
numbers2=[4,5,6]
result=map(lambda x,y:x+y,numbers1,numbers2)
print("Addition of two lists")
print(list(result))

#using map
nums=[1,2,3,4,5]
def sq(n):
    return n*n
square=list(map(sq,nums))
print("Square number in list")
print(square)

#ACTIVITY 2
#ZIP IT
#zip the element of two lists
s1={2,3,1}
s2={'b','a','c'}
s3=list(zip(s1,s2))
print(s3,"\n")


#Zip the elements
list1=[10,20,30,40]
list2=[100,200,300,400]

for x,y in zip(list1,list2[::-1]):
    print(x,y)
#zip into dictionary

stocks=['reliance','infosys','tcs']
prices=[2175,1127,2750]

new_dict={stocks:prices for stocks,prices in zip(stocks,prices)}
print('\n{}'.format(new_dict))

#ACTIVITY 3
#EXIT FUNCTION

for i in range(10):
    #if value of i becomes 5 then program is forced to exit
    if i == 5:
        print(exit)
        exit()
    print(i)