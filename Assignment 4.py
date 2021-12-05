#!/usr/bin/env python
# coding: utf-8

# In[3]:


#For Mutiplication
def multiply(num1, num2):
    return num1 * num2
#For Division
def division(num1,num2):
    return num1/num2
#For Addition
def add(num1,num2):
    return num1+num2
#For Subtraction
def subtract(num1,num2):
    num1-num2
value1 = int(input("Enter 1st number: "))
value2 = int(input("Enter 2nd number: "))
print("Select Operation 1 for Mutiply 2 For Divison 3 For Addition and 4 for Subtraction")
operation = int(input("Enter Your Choice"))
if(operation == 1):
    print(value1, "*", value2, "=", multiply(value1, value2))
elif(operation == 2):
    print(value1, "/", value2, "=", division(value1, value2))
elif(operation == 3):
    print(value1, "+", value2, "=", add(value1, value2))
elif(operation == 4):
     print(value1, "-", value2, "=", subtract(value1, value2))
else:
    print("Please Enter Correct Choice")

    

   

    
    


# In[4]:


#Adding a key to the Dictionary
squares = {1: 1, 2: 4, 3: 9}
squares[4] = 16
print(squares)



# In[5]:


d = {'key1': 1,'key2': 14,'key3': 47}
sum1 = sum(d[item] for item in d)
print(sum1)


# In[7]:


def checkIfDuplicates_2(listOfElems):
    ''' Check if given list contains any duplicates '''    
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)         
    return False

list = ['1', '2', '3', '1', '2', '4', '7', '1', '3']
result = checkIfDuplicates_2(list)
if result:
    print('Yes, list contains duplicates')
else:
    print('No duplicates found in list')
    
    


# In[ ]:


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

