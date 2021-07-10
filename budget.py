class Category:
  category_name = ""
  ledger = list()
  balance = 0

  #Constructor
  def __init__(self,name):
    self.category_name = name
   
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
    self.balance += amount

  #Withdraw method adds amount as negative number. If there are not enough funds, nothing should be added to the ledger.
  def withdraw(self, amount, description=""):
    if(self.check_funds(amount)):
      withdrawal_dict = dict()
      withdrawal_dict["amount" ] = -amount
      withdrawal_dict["description" ] = description
      self.ledger.append(withdrawal_dict)
      self.balance -= amount
      return True
    else:
      return False
    
  #returns the net balance
  def get_balance(self):
    return self.balance

  #transfer amount from one category to another category
  def transfer(self, amount, Category):
    if(self.check_funds(amount)):
      transfer_from = "Transfer to " + Category.category_name
      self.withdraw(amount, transfer_from)
      transfer_to = "Transfer from " + self.category_name
      Category.deposit(amount, transfer_to)
      return True
    else:
      return False


  #checks if a given amount is greater than net balance
  def check_funds(self,amount):
      if(amount > self.balance):
        return False
      else: 
        return True
    

def create_spend_chart(categories):
  pass