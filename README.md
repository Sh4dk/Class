class employees:
    def __init__(self, first_name, last_name, email, pay):
        self.first_name= first_name
        self.last_name= last_name
        self.email= email
        self.pay= pay
    def fullname(self):
        return ('{} {}'.format(self.first_name, self.last_name))

emp_1 = employees('alex', 'robbins', 'alexrobbins@gmail.com', 50000)
emp_2 = employees('muhammed', 'ali', 'muhammedali@gmail.com', 250000)
print(emp_1.fullname())
print(emp_2.email)

        
