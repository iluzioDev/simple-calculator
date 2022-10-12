def printBorder():
  print("---------------------------------")

def requestOp():
  return int(input("Operand: "))

def menu():
  while True:
    printBorder()
    print("\tSIMPLE CALCULATOR")
    printBorder()
    print("[0] Exit")
    print("[1] Addition")
    print("[2] Substraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[5] Modulo")
    print("[6] Power")
    printBorder()
    option = int(input("Please, choose your option -> "))
    printBorder()

    op1, op2, result, operator = None, None, None, ""
    if (0 < option < 7):
      op1 = requestOp()
      op2 = requestOp()

    match(option):
      case 0:
        print("See you soon!")
        break
      case 1:
        operator = "+"
        result = op1 + op2
      case 2:
        operator = "-"
        result = op1 - op2
      case 3:
        operator = "*"
        result = op1 * op2
      case 4:
        operator = "/"
        result = op1 / op2
      case 5:
        operator = "%"
        result = op1 % op2
      case 6:
        operator = "**"
        result = op1 ** op2
        
    printBorder()
    if (0 < option):
      print (f"{op1} {operator} {op2} = {result}")

  printBorder()
  return None

menu()