class BankAccount: #creates the class
   _counter = 0 #sets account
   def __init__(self, Account_Number, balance):
      BankAccount._counter += 1
      self.Account_Number = Account_Number
      self.__balance = 0.0
      self.balance = balance 
      #shows BankAccount

      print(f"Account {BankAccount._counter}")
      print(f"Account Number: {self.__Account_Number}")
      print(f"Balance: {self.__balance:.2f}")
      print()

   @property #public getter
   def Account_Number(self):
      return self.__Account_Number

   @Account_Number.setter #setter for acc number
   def Account_Number(self, value):
      self.__Account_Number = value

   @property
   def balance(self):
      return self.__balance

   @balance.setter
   def balance(self, value):
      print(f"Update balance to {value}")
      if value < 0:
         print("Balance invalid.")
      else: 
         self.__balance = float(value)

      print(f"Account Number: {self.__Account_Number}")
      print(f"Balance: {self.__balance:.2f}")
      print()

if __name__ == "__main__":
   print ("Object of class BankAccount\n")
   a1 = BankAccount(12345,1000)
   a1.balance = -100
