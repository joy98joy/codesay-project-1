NumFirst = input("Enter number: ")
Operator = input("Enter operator(+, -, *, /): ")
NumSecond= input("Enter number: ")
def calculator():

  
  try:
    NumFirst = int(NumFirst)
    NumSecond = int(NumSecond)

  except NumSecond == 0:
    print("Error: Division by zero.")
  exit()

  def add(NumFirst, NumSecond):
    return NumFirst + NumSecond
  def subtract(NumFirst, NumSecond):
    return NumFirst - NumSecond
  def multiply(NumFirst, NumSecond):
    return NumFirst * NumSecond
  def divide(NumFirst, NumSecond):
    return NumFirst / NumSecond
  if Operator not in ['+', '-', '*', '/']:
    return print("Invalid operator.")
  
  elif Operator == '+':
    result = add(NumFirst, NumSecond)
  elif Operator == '-':
    subtract(NumFirst, NumSecond)
  elif Operator == '*':
    multiply(NumFirst, NumSecond)
  elif Operator == '/':
    divide(NumFirst, NumSecond)

  return print(f"Result: {result}")

calculator()
  
  






  # def calculate(NumFirst, Operator, NumSecond):
  #     try:
  #         NumFirst = float(NumFirst)
  #         NumSecond = float(NumSecond)
  #     except ValueError:
  #         return print("Invalid input. Please enter numeric values.")

  #     if Operator == '+':
  #         return NumFirst + NumSecond
  #     elif Operator == '-':
  #         return NumFirst - NumSecond
  #     elif Operator == '*':
  #         return NumFirst * NumSecond
  #     elif Operator == '/':
  #         if NumSecond == 0:
  #             return print("Error: Division by zero.")
  #         return NumFirst / NumSecond
  #     else:
  #         return print("Invalid operator. Please use +, -, *, or /.")
    
    




  # if __name__ == "__main__":