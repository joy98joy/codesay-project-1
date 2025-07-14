
def main():
  num = input("Enter number: ")
  exponent= input("Enter exponent: ")
  try:
    num= float(num)
  except ValueError:
    return print("Invalid number input.")
  try:
    exponent = int(exponent)
  except ValueError:
    return print ("Invalid exponent input.")
  if exponent == 0:
    return print("Result:",1)
  result = 1.0
  if exponent > 0:
    for i in range(exponent):
      result *= num
  else:
    for i in range(abs(exponent)):
      result *=num
    result = 1.0 /result

  return print("Result:",result)

if __name__ == "__main__":
    main()


    