class Category:

  #Constructor
  def __init__(self,name):
    self.category_name = name
    self.ledger = list()
   
  #method for print(Object)
  def __repr__(self):
    first_line = "*"*15 + self.category_name + "*"*15 +"\n"
    for dict in self.ledger:
      first_line += dict["description"] + " " + str(dict["amount"]) +"\n"

    return  first_line
  
  #deposit method that accepts an amount and description and adds amount to balance
  def deposit(self, amount, description=""):
    deposit_dict = dict()
    deposit_dict["amount" ] = amount
    deposit_dict["description" ] = description
    self.ledger.append(deposit_dict)

  #Withdraw method adds amount as negative number. If there are not enough funds, nothing should be added to the ledger.
  def withdraw(self, amount, description=""):
    if(self.check_funds(amount)):
      withdrawal_dict = dict()
      withdrawal_dict["amount" ] = -amount
      withdrawal_dict["description" ] = description
      self.ledger.append(withdrawal_dict)
      return True
    else:
      return False
    
  #returns the net balance
  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item["amount"]
    return balance

  #transfer amount from one category to another category
  def transfer(self, amount, Category):
    if(self.check_funds(amount)):
      self.withdraw(amount, "Transfer to " + Category.category_name)
      Category.deposit(amount, "Transfer from " + self.category_name)
      return True
    return False


  #checks if we have enough money to spend
  def check_funds(self, amount):
      if(self.get_balance() >= amount):
        return True
      return False
    

def create_spend_chart(categories):
  pass