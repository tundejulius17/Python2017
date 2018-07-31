import re

regex = "[+]\\d{3}-\\d{2}-\\d{7}"
phone ="+358-40-1345678"
compiled_re = re.compile(regex)
res = compiled_re.match(phone)
if res != None:
    print(phone + "  matched " + res.group())
else:
    print(phone + " did not match the pattern: " + regex)

ssn = "(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}-[0-9]{3}[A-Z]"
social_security_num = "120570-467W";
compiled_re = re.compile(ssn)
res = compiled_re.match(social_security_num)
if res != None:
    print(social_security_num + "  matched " + res.group())
else:
    print(social_security_num + " did not match the pattern: " + ssn)

num_less_1000 = "(100|[1-9]{1,3})"
number_less_1000 = "1000"
compiled_re = re.compile(num_less_1000)
res = compiled_re.match(number_less_1000)
if res != None:
    print(number_less_1000 + " matched " + res.group())
else:
    print(number_less_1000 + " did not match the pattern: " + num_less_1000)

date = "((Jan)|(Feb)|(Mar)|(April)(May)|(June)|(July)|(Aug)|(Sept)|(Oct)|(Nov)|(Dec)).([1-9]|[1-2][0-9]|3[0-1]).[1-2][0-9]{3}"
date_expression = "Mar.27.1996"
compiled_re = re.compile(date)
res = compiled_re.match(date_expression)
if res != None:
    print(date_expression + "  matched " + res.group())
else:
    print(date_expression + " did not match the pattern: " + date)
