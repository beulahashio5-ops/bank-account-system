from Account import Account

class savings(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.interest_rate = 0.02
        self.withdraw_limit = 100

        # overriding withdraw method
        def withdraw(self, amount):

            # Check the withdrawal limit first
            if amount > self.withdraw_limit:
                print(f"Withdrawal cannot exceed ${self.withdrawal_limit}")

            else:
                # Use parent class withdrawal method
                super().withdraw(amount)

        def apply_interest(self):
            interest = self.get_balance() * self.interest_rate
            self.deposit(interest)

            print(f"Interest of {interest} applied. New balance:{self.get_balance()}")


            #Testing
            print("----Savings Account----")

            savings = Savings("Alice", 1000)

            print(f"Initial balance:{savings.get_balance()}")

            savings.deposit(500)

            #should fail
            savings.withdraw(200)

            #should work
            savings.withdraw(50)

            savings.apply_interest()











