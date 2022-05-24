from select import select

class Employee:
    ''''基类'''
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

# 类的内置属性
print('Employee.__doc__:',Employee.__doc__)
print('Employee.__name__:',Employee.__name__)
print('Employee.__module__:',Employee.__module__)
print('Employee.__bases__:',Employee.__bases__)
print('Employee.__dict__:',Employee.__dict__)



