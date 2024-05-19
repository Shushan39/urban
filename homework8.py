grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
rez_1 = sum(grades[0])/len(grades[0])
rez_2 = sum(grades[1])/len(grades[1])
rez_3 = sum(grades[2])/len(grades[2])
rez_4 = sum(grades[3])/len(grades[3])
rez_5 = sum(grades[4])/len(grades[4])
grades_average = [[rez_1], [rez_2], [rez_3], [rez_4],[rez_5]]
students_list = list(students)
students_list.sort()
d = dict(zip(students_list, grades_average))
print(d)
