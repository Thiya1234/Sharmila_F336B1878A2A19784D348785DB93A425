class student:
  def __init__(self , name ,
              roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa
def sort_students(student_list):

  sorted_students=sorted(student_list
,key=lambda student:student.cgpa,
                        reverse=True)
  return sorted_students
students =[
  student("sharmi", "a123", 7.8),
  student("Manju", "a125", 8.9),
  student("brindha", "a125", 9.1),
  student("suba", "a126", 9.9)]

sorted_student=sort_students(students)


for student in sorted_student:
  print("Name : {}, Roll Number : {}, CGPA : {},".format(student.name, student.roll_number,student.cgpa))


    
                                                   