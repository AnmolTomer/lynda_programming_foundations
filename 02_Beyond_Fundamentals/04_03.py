# Regular expressions

# Strings sometimes need complex searches and manipulations. Many programming languages offer regular expressions just for this very reason.
# Reg-ex allows us to create a description of the pattern that we want to match, we may then check a string against the reg-ex, and if it matches we may use one or more method to perform what we want on results. Regex can be made up of letters, numbers and special characters. In regex each character has a specific meaning and we can put these characters to gether to describe exactly what we need.
"""
Indicate specific text you are looking for, by enclosing it in slashses. /hello/
Backslashes with characters mark many patterns in a regular expression.
\d - Digit
\w - Word
. - Any character
+ - One or more occurences
* - Zero or more
? - 0 or 1
"""

import re

five_digit_zip = '98101'
nine_digit_zip = '98101-0003'
phone_number = '234-567-8901'

five_digit_expression = r'\d{5}'
# 5 occurences of preceeding expression, the digit, now when we have an expression, we want to compare it to strings
# search takes 2 arguments, regular expression and the string to compare against.
# Matched object returned, as this and second string contains 5 digits in a row.
print(re.search(five_digit_expression, five_digit_zip))
print(re.search(five_digit_expression, nine_digit_zip))
print(re.search(five_digit_expression, phone_number))  # Didn't match

# Fortunately regex patterns are written for many common patterns and we do not need to create something as complicated as email verification regex right off the bat. Being able to recognize a regex when you see one is important.
