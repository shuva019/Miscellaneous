#importing necessary libraries
import re, pyperclip

#create a regex for phone number
phoneRegex = re.compile(r'''
#415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?         #area code
(\s|-)                          #first separator
\d\d\d                          #first 3 digits
-                               #separator
\d\d\d\d                        #last 4 digits
(((ext(\.)?\s)|x)              #extension word part(optional)
(\d{2,5}))?                    #extension numeric part
)
''', re.VERBOSE)

#create a regex for email addresses
emailRegex = re.compile(r'''
#some.+_thing@something.com

[a-zA-z0-9_.+]+                 #name part
@                               #@symbol
[a-zA-z0-9_.+]+                 #domain name part

''', re.VERBOSE)

#paste the text from the clipboard
text = pyperclip.paste()

#extract the email/phone from the text
phoneNum = phoneRegex.findall(text)
emailAddress = emailRegex.findall(text)

allPhoneNum = []
for i in phoneNum:
    allPhoneNum.append(i[0])

#make it look good
phoneEmail = '\n'.join(allPhoneNum) + '\n' + '\n'.join(emailAddress)
print(phoneEmail)
