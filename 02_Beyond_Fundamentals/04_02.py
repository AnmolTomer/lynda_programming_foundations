# finding patterns in strings

first_name = 'elon'
last_name = 'musk'
note = 'award: 2014 EDISON ACHIEVEMENT AWARD'

first_name_cap = first_name.capitalize()
last_name_cap = last_name.capitalize()

print(first_name_cap)
print(last_name_cap)

# .find() and .index() gives us a reference to the first occurence of text we specify.
# .rfind() and .rindex() provides the last occurence.

award_location = note.find('award: ')
print(award_location)
award_text = note[7:]
print(award_text)  
# Print award name
