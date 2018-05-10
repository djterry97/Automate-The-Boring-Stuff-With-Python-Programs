#! python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

        # are code (optional)
(
((\d\d\d)|(\(\d\d\d\)))?
        # first separator
(\s|-)
        # first 3 digits
\d\d\d
        # separator
-
        # last 4 digits
\d\d\d\d
        # extension (optional)
((ext(\.)?\s|x)
(\d{2,5}))?
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.com

# name
[a-zA-Z0-9_.+]+
# @ symbol
@
# domain name
[a-zA-Z0-9_.+]+
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()


# Extract the email/phone from the text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# print(allPhoneNumbers)
# print(extractedEmail)

#TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) +  '\n' +'\n'.join(extractedEmail)
pyperclip.copy(results)
