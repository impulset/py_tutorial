import timeit
#Help
help(list.extend)
#Show attributes of a data type
dir("hello")
dir(["hello"])
#Measure time of execution
timeit.timeit('list(set([1,2,3,1,7,7,2]))', number=10000)
#1 one line code
def list_func():
    desired_day = [1,3]
    day = 3
    if any(x==day for x in desired_day): 
        print("Good")

sum(i for i in range(1, 100) if i%3 == 0 or i%5 == 0)     
print(sum([i for i in range(1, 100) if i%3 == 0 or i%5 == 0]))     
    
    #Ternary
color  = 'teal'
print("Good choice") if color == 'teal' else print('MEH')
#end#1#

#2 Remove comma from tuples
def remove_comma_from_tuples():
    users = [(62662,), (89898,)]
    return [chat_ids for (chat_ids,) in users]    

