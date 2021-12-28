work_hours = [('Raj',420),('Saksham',1000),('Priya' , 200),('Andrew', 500),('Paul',390),('Gautam',140)]
def employee_of_month(work_hours):
    employee_max = 0
    employee_month = '' 
    for employee,hours in work_hours:
        if hours > employee_max:
            employee_max = hours
            employee_month = employee
        else:
            pass


        
    return(employee_month,hours)

print(employee_of_month(work_hours))

