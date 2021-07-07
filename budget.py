class Category:
  category_name = ""
  ledger = list()

  def __init__(self,name):
    self.category_name = name
  
  def deposit(self, amount, description=""):
    deposit_dict = dict()
    deposit_dict["amount" ] = amount
    deposit_dict["description" ] = description
    self.ledger.append(deposit_dict)
  
  #def withdraw(self, amount, description=""):
    











def create_spend_chart(categories):
  pass