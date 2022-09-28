import re

def arithmetic_arranger(problems, status=False):
  first = ""
  operator = ""
  lines = ""
  second = ""
  sum = ""
  res = ""
  overall = ""

  if len(problems) > 5:
    return "Error: Too many problems."
    
  for prb in problems:
    first_num = prb.split(" ")[0]
    operator = prb.split(" ")[1]
    second_num = prb.split(" ")[2]

    if re.search("[^\s0-9.+-]", prb):
      if re.search("[/]", prb) or re.search("[*]", prb):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

    if len(first_num) > 4 or len(second_num) > 4:
      return "Error: Numbers cannot be more than four digits."
      

    if operator == "+":
      sum = str(int(first_num) + int(second_num))
    if operator == "-":
      sum = str(int(first_num) - int(second_num))

    length = max(len(first_num), len(second_num)) + 2
    top = str(first_num).rjust(length)
    bottom = operator + str(second_num).rjust(length - 1)
    solution = str(sum).rjust(length)
    
    line = ""
    for i in range(length):
      line += "-"

    if prb != problems[-1]:
      first += top + '    '
      second += bottom + '    '
      lines += line + '    '
      res += solution + '    '
    else:
      first += top
      second += bottom
      lines += line 
      res += solution
  
  if status:
    overall = first + "\n" + second + "\n" + lines + "\n" + res 
  else:
    overall = first + "\n"  + second + "\n" + lines 
  return overall
