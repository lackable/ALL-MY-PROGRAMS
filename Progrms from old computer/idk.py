work_hours = [("cassie",100),("joe",200),("kassie",50),("doug", 20),("turk",400)]



def employee_of_month(work_hours):


    hours_max = 0
    employee_max = ''

    for name, hours in work_hours:
        if hours > hours_max:
            hours_max = hours
            employee_max = name
        else:
            pass
    return(employee_max,hours_max)
    
