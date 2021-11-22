                    ############
#####################  STRING  #########################
                    ############

string1 = "89"
string2 = "hellO"
#String methods
print(string1.zfill(5)) #zfill() add zeroes at the beginning of the string
string1.startswith("8") #returns True, startswith("")
string1.find("8") #returns 0, find() 
string2.lower(), string2.upper(), string2.capitalize() #lower(), upper(), capitalize()
string2.replace("l", "L", 1) #replace()
string2.splitlines() #splitlines()


                    ##########
#####################  LIST  #########################
                    ##########
#create list
nums = list(range(10,20,2)) # [10, 12, 14, 16, 18]

#Slicing #lst[start:stop:step]
print(nums[1::2]) #double colon to specify steps

#Splicing - updates items in a list
nums[0:1] = [33,55,77]

#List methods
nums_copy = nums.copy() #copy()
nums.count(14) #count()
nums_copy.extend(nums) #extend()
nums.insert(0, "two") #insert(where, what)
nums.pop(0) #pop(index) or pop() - without argument removes last element
nums.reverse()
nums.sort()

#List comprehensions 
                #syntax !!!!! [do_this if something else do this for thing in things]
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
double = [n * 2 for n in nums2]
evens = [num for num in nums2 if num % 2 == 0]


                    ##########
#####################  DICT  #########################
                    ##########
#Create dictionary
dict([["Name", "Alex"], ["Age", 30]]) #{'Name': 'Alex', 'Age': 30}

#Looping over Dictionaries
ages = {"Whiskey": 6, "Fluffy": 3, "Ezra": 7}

for name in ages.keys():
    print(name)

for age in ages.values():
    print(age)

for k,v in ages.items():
    result = f'{k} = {v}'
  
result1 = '\n'.join(f'{k} = {v}' for k, v in ages.items()) #Single line expression

#Dictionary methods
ages.get("Ezra")
ages.get("Alex", 9) #default value if key doesn't exist


                    ##########
#####################  SETS  #########################
                    ##########
lemon = {'sour', 'yellow', 'fruit', 'bumpy'}
banana = {'fruit', 'smooth', 'sweet', 'yellow'}      

#Set operators
lemon | banana | {'fruit', 'sad'} # or banana.union(lemon) - a list can be used as an argument #union  - {'bumpy', 'yellow', 'fruit', 'sour', 'sweet', 'smooth'} 
lemon & banana #intersection - returns similar items from the sets - {'fruit', 'yellow'}
lemon - banana #difference 
lemon ^ banana #symmetric_difference - returns unique items from the sets - {'bumpy', 'sweet', 'smooth', 'sour'}
