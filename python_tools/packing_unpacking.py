                    #####################
##################### Packing/Unpacking #########################
                    #####################

names = ['charlie', 'lucy']
name1, name2 = names 

names_a = ['charlie', 'lucy', 'adam', 'linda']
name2, *name3 = names_a
name3 # ['lucy', 'adam', 'linda']

color_pairs = [['red', 'green'], ['white', 'blue']]
[[pr1,pr2],[sec1, sec2]] = color_pairs
pr1 # 'red'

grades = {'A': 12, 'B': 19, 'C': 30}
for (k, v) in grades.items():
    print(k, v)

