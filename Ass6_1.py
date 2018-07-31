import re

text= "The sky may be sunny or cloudy, but still you should try to do your best to achieve your tiny joy"
print(re.findall(r"\w+y",text))