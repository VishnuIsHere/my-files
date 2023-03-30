import re
txt=input('enter the email')
v=re.findall(r'[a-z]+[0-9]*[@][a-z]+[.][a-z]{2,3}',txt)
if v:
    print('valid email')
txt2=input('enter the  password')
c=re.findall(r'[A-z]+[a-z]+[0-9]*[a-z]+[a-z]{2,3}',txt2)
if c:
    print('the new password updated') 
else:
    print('incorrect password')