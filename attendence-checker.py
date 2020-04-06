name = input("ENTER YOUR FULL NAME: ")
fathersname = input("ENTER YOUR FATHERS NAME: ")
grade = input("ENTER YOUR GRADE: ")
print("CLASSES HELD = 190")
classes_held = 190
classes_attended = int(input("ENTER THE NUMBER OF CLASSES YOU HAVE ATTENDED: "))
attendence_percentenage = int((classes_attended/classes_held*100))
print(attendence_percentenage,"%")

if attendence_percentenage >= 75 :
    print("YOU ARE ALLOWED TO SIT IN EXAMS")
elif attendence_percentenage < 75 :
    medicalcause = input("DO YOU HAVE A MEDICAL CAUSE? (Y/N): ")    
if (medicalcause == "Y"):
    print("YOU ARE ALLOWED TO SIT IN EXAMS. DO BRING YOUR MEDICAL CERTIFICATE WITH YOU")
else:
    print("YOU ARE NOT ALLOWED TO SIT IN EXAMS")    