class employees:
    num_of_emps = 0
    raise_amount = 1.09
    def __init__(self, first_name, last_name, email, pay):
        self.first_name= first_name
        self.last_name= last_name
        self.email= email
        self.pay= pay
        employees.num_of_emps += 1
    def fullname(self):
        return ('{} {}'.format(self.first_name, self.last_name))
    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, f"{first}.{last}@gmail.com", int(pay))
        
emp_1 = employees('alex', 'robbins', 'alexrobbins@gmail.com', 50000)
emp_2 = employees('muhammed', 'ali', 'muhammedali@gmail.com', 250000)
print(emp_1.fullname())
print(emp_2.email)
print(employees.num_of_emps)
print(employees.raise_amount)
employees.set_raise_amount(1.05)
print(employees.raise_amount)
emp_str_1 = 'reza-khoramdel-65000'
emp_str_2 = 'john-marston-80000'
emp_str_3 = 'dutch-carlson-50000'
new_emp_1 = employees.from_string(emp_str_1)
new_emp_2 = employees.from_string(emp_str_2)
print(new_emp_1.pay)
print(new_emp_2.email)

