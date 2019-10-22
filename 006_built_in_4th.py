print('\n\n')
print('===================================================================')
print('|  Built-in Function #4                                           |')
print('|  1.sort, reverse                                                |')
print('|  2.sort object                                                  |')
print("===================================================================\n\n")

# sorted, reversed()
print('1. sort, reverse & sorted()')
num = [1,4,3,6,3,5,2]
print("   num is", num)
print("   The result of sorted(num) :", sorted(num))
print("   The result of sorted(num,reverse=True) :", sorted(num,reverse=True))
num.sort()
print("The result of num.sort() is", num)
num.sort(reverse=True)
print("The result of num.sort(reverse=True) is", num)
print('\n')

# Sorting Object
print("\nSorting Object")
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __str__(self):
        return "{}:{}".format(self.name, self.score)

Students = [Student("Mike", 50), Student("Jhon", 20), Student("Toby", 40)]

def print_student():
    for i in Students:
        print(i, end= " ")
    print("")

print_student()
sorted(Students, key= lambda stu: stu.score)
print("Return Sort by Function")
print_student()
Students.sort(key= lambda stu: stu.score)
print_student()
Students.sort(key= lambda stu: stu.score, reverse=True)
print_student()
