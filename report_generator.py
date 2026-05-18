student_name = input("Enter student name: ")
backend_marks = int(input("Enter Backend marks: "))
frontend_marks = int(input("Enter Frontend marks: "))
design_marks= int(input("Enter Design marks: "))


def average(backend_marks, frontend_marks, design_marks):
    calculate_average= (backend_marks+frontend_marks+design_marks)/3
    return calculate_average

def grade(calculate_average):
    calculate_average=(backend_marks+frontend_marks+design_marks)/3
    
    if calculate_average>=80:
        return "A"
    elif calculate_average >=79 and calculate_average<=79:
        return "B"
    elif calculate_average >=60 and calculate_average <=69:
        return "C"
    elif calculate_average >=50 and calculate_average <=59:
        return "D"
    else:
        return "E"
    
    
    
def generate_report(student_name,backend_marks, frontend_marks,design_marks,):
    average_marks=average(backend_marks, frontend_marks,design_marks)
    final_grade= grade(average_marks)
    report={
        "name":student_name,
        "Backend": backend_marks,
        "Frontend":frontend_marks,
        "Design":design_marks,
        "Average": round(average_marks),
        "Grade": final_grade

    }
    return report

print(generate_report(student_name,backend_marks,frontend_marks,design_marks))



    

 
