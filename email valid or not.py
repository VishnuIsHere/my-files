import re
txt=input('enter the email')
v=re.findall(r'[a-z]+[0-9]*[@][a-z]+[.][a-z]{2,3}',txt)
if v:
    print('valid email')
else:
    print("not valid")