def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_char(s):
  try:
    s.isalpha()
    return True
  except ValueError:
    return False



#code to convert input string into tokens i.e list
#not using list directly because it cannot evaluate if num is multidigit
def tokenize(exp):
  tokens = []
  nums = ""

  for ch in exp:
    if is_number(ch) or ch=='.' :
      nums += ch
    elif is_char(ch) and ch not in ("+","^", "-", "*" ,"/", "(", ")"):
      nums += str(ord(ch))
      tokens.append(nums)
      nums=""
    else:
      if nums:
        tokens.append(nums)
        nums=""
      if ch in ("+","^", "-", "*" ,"/", "(", ")"):
        tokens.append(ch)
  if nums:
    tokens.append(nums)
  return tokens

#code of operation precedance order
def precd(ch):
  if ch == "^":
    return 3
  elif ch in ("*", "/"):
    return 2
  elif ch in ("+", "-"):
    return 1
  else:
    return 0

#code for infix to postfix conversion
def infix_to_postfix(tokens):
  postfix = []
  stack = []

  for ch in tokens:
    if is_number(ch):
      postfix.append(ch)
    else:
      if not stack or ch=="(":
        stack.append(ch)
      else:
        if ch == ")":
          while stack[-1] != "(":
            postfix.append(stack.pop())
          stack.pop()
        else:
          while stack and precd(ch) <= precd(stack[-1]):
            postfix.append(stack.pop())
          stack.append(ch)
  while stack:
    postfix.append(stack.pop())
  return postfix


def eval(num1,ch,num2):
  if ch == "+":
        return num1 + num2
  elif ch == "-":
        return num1 - num2
  elif ch == "*":
          return num1 * num2
  elif ch == "/":
        return num1 / num2
  elif ch == "^":
       return num1 ** num2
  else:
    return "Invalid Input"

#postfix evaluation
def postfix_eval(postfix):
  stack = []
  for ch in postfix:
    if is_number(ch):
      stack.append(ch)
    else:
      print(stack)
      num2 = stack.pop()
      num1 = stack.pop()
      stack.append(eval(float(num1), ch, float(num2)))

  return stack.pop()



if __name__ == "__main__":
  exp = input("Enter expression: ")
  tokens = tokenize(exp)
  print(tokens)
  postfix = infix_to_postfix(tokens)
  print(postfix)
  print(postfix_eval(postfix))
