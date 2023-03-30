# import re
# a='satpat cat batrat'
# b=re.search('^satpat.*cat$',a)
# print(b)
import re
txt = "The rain rat in Spain"
x = re.findall("The.{1}ra", txt)
print(x)
if x:
  print("YES! We have a match!")
else:
  print("No match")

