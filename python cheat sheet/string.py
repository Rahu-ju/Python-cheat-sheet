# Advanced String Methods
'''
We've covered a bunch of String class methods already, so let's keep building on those and run down some more advanced methods.

The string method lower will return the string with all characters changed to lowercase. The inverse of this is the upper method, which will return the string all in uppercase. Just like with previous methods, we call these on a string using dot notation, like "this is a string".upper(). This would return the string "THIS IS A STRING". This can be super handy when checking user input, since someone might type in all lowercase, all uppercase, or even a mixture of cases.

You can use the strip method to remove surrounding whitespace from a string. Whitespace includes spaces, tabs, and newline characters. You can also use the methods  lstrip and rstrip to remove whitespace only from the left or the right side of the string, respectively.

The method count can be used to return the number of times a substring appears in a string. This can be handy for finding out how many characters appear in a string, or counting the number of times a certain word appears in a sentence or paragraph.

If you wanted to check if a string ends with a given substring, you can use the method endswith. This will return True if the substring is found at the end of the string, and False if not.

The isnumeric method can check if a string is composed of only numbers. If the string contains only numbers, this method will return True. We can use this to check if a string contains numbers before passing the string to the int() function to convert it to an integer, avoiding an error. Useful!

We took a look at string concatenation using the plus sign, earlier. We can also use the join method to concatenate strings. This method is called on a string that will be used to join a list of strings. The method takes a list of strings to be joined as a parameter, and returns a new string composed of each of the strings from our list joined using the initial string. For example, " ".join(["This","is","a","sentence"]) would return the string "This is a sentence".

The inverse of the join method is the split method. This allows us to split a string into a list of strings. By default, it splits by any whitespace characters. You can also split by any other characters by passing a parameter.
'''



#String Reference Cheat Sheet

'''
In Python, there are a lot of things you can do with strings. In this cheat sheet, you’ll find the most common string operations and string methods.

String operations
len(string) Returns the length of the string
for character in string Iterates over each character in the string
if substring in string Checks whether the substring is part of the string
string[i] Accesses the character at index i of the string, starting at zero
string[i:j] Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.
String methods
string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
string.count(substring) Returns the number of times substring is present in the string
string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter
Check out the official documentation for all available String methods.

'''

#Formatting Strings Cheat Sheet


'''####
Python offers different ways to format strings. In the video, we explained the format() method. In this reading, we'll highlight three different ways of formatting strings. For this course you only need to know the format() method. But on the internet, you might find any of the three, so it's a good idea to know that the others exist.

Using the format() method
The format method returns a copy of the string where the {} placeholders have been replaced with the values of the variables. These variables are converted to strings if they weren't strings already. Empty placeholders are replaced by the variables passed to format in the same order.
'''
# "base string with {} placeholders".format(variables)

example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)

"""Outputs:
this is an example of using the format() method on a string
"""


'''###If the placeholders indicate a number, they’re replaced by the variable corresponding to that order (starting at zero).'''
# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""

'''###If the placeholders indicate a field name, they’re replaced by the variable corresponding to that field name. This means that parameters to format need to be passed indicating the field name.'''
# "{var1} {var2}".format(var1=value1, var2=value2)

#Formatting expressions
'''
Expr	Meaning	Example
{:d}	integer value	'{:d}'.format(10.5) → '10'
{:.2f}	floating point with that many decimals	'{:.2f}'.format(0.5) → '0.50'
{:.2s}	string with that many characters	'{:.2s}'.format('Python') → 'Py'
{:<6s}	string aligned to the left that many spaces	'{:<6s}'.format('Py') → 'Py    '
{:>6s}	string aligned to the right that many spaces	'{:>6s}'.format('Py') → '    Py'
{:^6s}	string centered in that many spaces	'{:^6s}'.format('Py') → '  Py '

'''


