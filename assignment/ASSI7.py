students = {
    "koushik":(85,90,40),
    "vankai":(90,92,95),
    "meraj":(30,20,9  )
}
user_input = input("enter your name : ")
if user_input in students:
  marks = students[user_input]
  average = sum(marks)/len(marks)
  if average >= 60:
        print("you are a passed")
  else:
        print("you are failed")
else:
    print("you are not a member of the students list")
