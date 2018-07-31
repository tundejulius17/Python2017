import re

text="A flower is a beautiful plant, which can be planted in the garden " \
     "or used to decorate home. One might like a flower for its colors and the " \
     "other might like a flower for its smell. A flower typically symbolizes soft feelings"

for x in re.finditer('flower', text):
    print("flower indexes are: ", x.start(), x.end())





