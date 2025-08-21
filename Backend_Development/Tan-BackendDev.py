class Account:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name

class StudentAccount(Account):
    def __init__(self, ID, name):
        super().__init__(ID, name)
        self.classes = set()
        self.is_enlistment_locked = False # This is for when the student locks their enlistment.
        self.is_enlisted = False # This is for when the adviser enlists the student.

    # Sicne the classes attricute is a set, there is no need to worry if they add the class repeatedly.
    def add_class(self, enlist_class):
        self.classes.add(enlist_class)
        
    # We need to check whether the student has already locked their enlistment.
    def lock_enlistment(self):
        try:
            if self.is_enlistment_locked:
                raise Exception(f"{self.name} has already locked their enlistment.")
        except Exception as e:
            print(e)
            return
        
        self.is_enlistment_locked = True
        print(f'{self.name} has locked enlistment.')

class AdviserAccount(Account):
    def __init__(self, ID, name):
        super().__init__(ID, name)
        self.advisees = []
        self.enlisted_advisees = []

    # We can only add students if they are not yet advisees.
    def add_advisee(self, student:StudentAccount):
        if student not in self.advisees:
            self.advisees.append(student)
            print(f'{self.name} has added Ross as an advisee.')
        else:
            print("An error has occured.")


    def print_advisees(self):
        [print(i) for i in self.advisees]

    # Here the adviser locks the enlistment for the student.
    # We need to check for when the student is an advisee of the adviser.
    def lock_enlistment_for(self, student:StudentAccount):
        try:
            if student not in self.advisees:
                raise Exception(f"Error: {student.name} is not an advisee of {self.name}")
            
            if not student.is_enlistment_locked:
                raise Exception(f"Error: {student.name}'s enlistment is not locked yet.")
        
        except Exception as e:
            print(e)
            return

        student.is_enlisted = True
        print("Ross is now enisted.")


student1 = StudentAccount("05524", "Ross")
student1.add_class("Class 1")
student1.add_class("Class 2")
student1.add_class("Class 4")
student1.lock_enlistment()
# prints Ross has locked enlistment.

adviser = AdviserAccount("01341", "Rachel")
adviser.add_advisee(student1) 
# prints: Rachel has added Ross as an advisee.
adviser.lock_enlistment_for(student1)
# prints: Ross is now enlisted.


student2 = StudentAccount("12345", "Chandler")
student2.add_class("Class 1")
student2.add_class("Class 3")


adviser.add_advisee(student2)
# prints: Rachel has added Chandler as an advisee.
adviser.lock_enlistment_for(student2)
# prints: Error: Chandler's enlistment is not locked yet.


student3 = StudentAccount("01353", "Joey")
student3.add_class("Class 5")
student3.add_class("Class 9")


adviser.lock_enlistment_for(student3)
# prints: Error: Joey is not an advisee of Rachel.

"""
Notes: I feel like the purpose of the ID is
so that if there are instances with the same names 
there will be a unique identifier for them.
For the sake of time,
I implemented the <AdviserAccount>.advisees via list, but it would be faster if it were a dict.
"""