class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.no_of_greetings = 0

    def __repr__(self):
        return "Person's name : {0}, contact: {1}, {2}".format(self.name, self.email, self.phone)

    def print_contact_info(self):
        print("Person's name: {0}, {0}'s phone number and email address: {1}{2}".format(self.name,self.email,self.phone))

    def greet(self, other_person):

        print('Hello %s, I am %s!' % (other_person.name, self.name))
        self.no_of_greetings += 1

    def add_friend(self, friend):
        return self.friends.append(friend)

    def num_of_friends(self):
        print(len(self.friends))

    def greeting_count(self):
        print(self.no_of_greetings)




sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
#print(sonny.print_contact_info())
jordan = Person('Jordan','jordan@aol.com', '495-586-3456')
print(jordan)
sonny.greet(jordan)
jordan.friends.append('Beyza')
print(jordan.friends)
jordan.add_friend('beyza')
print(jordan.friends)
jordan.num_of_friends()

jordan.greet(sonny)
jordan.greet(sonny)
print(jordan.greeting_count())

print(sonny.email, sonny.phone)
print(jordan.email, jordan.phone)
#-----------------------------------------------------
class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print('{0} {1} {2}'.format(self.year, self.make,self.model))
car = Vehicle('Nissan', 'Leaf', 2015)
print(car.make, car.model, car.year)
car.print_info()
