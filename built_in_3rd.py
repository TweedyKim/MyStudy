# sorted, reversed()
print("======================[sort & reversed]=======================")
num = [1,4,3,6,3,5,2]
print("num :", num)
print("sorted(num) :", sorted(num))
print("sorted(num,reverse=True) :", sorted(num,reverse=True))

num.sort()
print("num.sort() and print num :", num)
num.sort(reverse=True)
print("num.sort(reverse=True) and print num :", num)

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
