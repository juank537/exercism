def convert(number):
  result = ""
  dict_number = {3: "Pling", 5: "Plang", 7: "Plong"}
  for key in dict_number.keys():
    if number % key == 0:
      result += dict_number[key]
    
  if not result:
    return str(number)
  return result


#  Solución sencilla


def convert_two(number):
    """Convert number into string."""
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    if not result:
        return str(number)
    return result