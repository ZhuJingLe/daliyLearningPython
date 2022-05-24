from select import select


class Employee:
    empCount = 0

    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
        Employee.empCount += 1
 
    def displayCount(self):
        print(self)
        print('Total Employee %d'%Employee.empCount)
    
    def displayEmployee(self):
        print('Name:',self.name,',salary:',self.salary)
    
em = Employee('zhangsan',10000)
em2 = Employee('lisi',100000)
print(Employee.empCount)
em.displayEmployee()
em2.displayCount()
