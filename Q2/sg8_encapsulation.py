class BankAccount #creates the class
   _counter = 0 #sets account
    def __init__(self, Account_Number, balance):
        BankAccount._counter += 1
        self._Account_Number = Account_Number
        self._balance = balance 
      #shows BankAccount

        print(f"Account {BankAccount._counter}")
        print(f"Account Number: {self._account_number}")
        print(f"Balance: {self._balance}")

   def get_balance(self):
      return self._balance
   def set_balance(self,value):
      print()
      print(f"Update balance to: {value}")
      
      if value < 0
