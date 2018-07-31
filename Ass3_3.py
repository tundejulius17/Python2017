
def encrypt_text(text):
    mapping_table = str.maketrans('flower', 'garlic')
    print(text.translate(mapping_table))

text = "A flower is a beautiful plant, which can be planted in the garden or " \
       "used to decorate home. One might like a flower for its colors and the " \
       "other might like a flower for its smell. A flower typically symbolizes soft feelings"

#We call the encrypt_text method here
encrypt_text(text)
