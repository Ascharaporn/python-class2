def find_max(*args):
   if not args:
      return None
   max_value = args[0]
   for number in args:
      if number > max_value:
         max_value = number
   return max_value

result = find_max(3,5,7,2,5)
print(f"THE MAXIMUM VALUE IS :{result}")