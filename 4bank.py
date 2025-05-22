# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing 
# the bank name. Show that it affects all instances.

class Bank :
    #Class variable
    bank_name= "National Bank"

    #Class method to change the bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    # Instance method to display bank name
    def display_bank(self):
        print(f"Bank Name: {self.bank_name}")

# Create two instances
customer1 = Bank()
customer2 = Bank()

# Display original bank name from both instances
print("Before change:")
customer1.display_bank()
customer2.display_bank()

# Change bank name using class method
Bank.change_bank_name("Habib Bank")

# Display updated bank name from both instances
print("\nAfter change:")
customer1.display_bank()
customer2.display_bank()