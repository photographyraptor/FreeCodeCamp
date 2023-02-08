def arithmetic_arranger(*problems):
  item1 = []
  item2 = False;  
  lines = ["", "", ""]
  if (len(problems) == 2):
    item1, item2 = problems
    lines.append("")
  else:
    item1 = problems[0]

  if (len(item1) > 5):
    return "Error: Too many problems."    

  for p in item1:
    splitted = p.split(" ")
    if (splitted[1] != "+") and (splitted[1] != "-"):
      return "Error: Operator must be \'+\' or \'-\'."
      
    l0 = len(splitted[0])
    l2 = len(splitted[2])
    if (l0 > 4) or (l2 > 4):
      return "Error: Numbers cannot be more than four digits."

    try:
      int(splitted[0])
      int(splitted[2])
    except (TypeError, ValueError):
      return "Error: Numbers must only contain digits."
    
    if (lines[0] != ""):
      lines[0] += (" " * 4)
      lines[1] += (" " * 4)
      lines[2] += (" " * 4)
      if (item2):
        lines[3] += (" " * 4)
    
    mx = max(l0,l2)    
    lines[0] += (" " * 2)
    lines[1] += splitted[1] + " "
    lines[2] += ("-" * (2 + mx))
    
    if (item2):
      op = ""
      if (splitted[1] == "+"):
        op = str(int(splitted[0]) + int(splitted[2]))
      else:
        op = str(int(splitted[0]) - int(splitted[2]))
      lop = len(op)

      if (mx>lop):
        lines[3] += (" " * (mx-lop)) + op
      elif (mx<lop):
        lines[3] += (" " * (lop-mx)) + op
      else:
        lines[3] += (" " * 2) + op
    
    if (l0>l2):
      lines[0] = lines[0] + splitted[0]
      lines[1] = lines[1] + (" " * (l0-l2)) + splitted[2]
    elif (l0<l2):
      lines[0] = lines[0] + (" " * (l2-l0)) + splitted[0]
      lines[1] = lines[1] + splitted[2]
    else:
      lines[0] = lines[0] + splitted[0]
      lines[1] = lines[1] + splitted[2]

  line = "\n".join(lines)
  return line