# try:
#     userinput = int(input("Enter the Number : "))
#
# except ZeroDivisionError:
#     print("ZeroDivisionerror")
#
# except ValueError:
#     print("ValueError")
#
# except Exception:
#     print("Exception")
#
# else:
#     print("User have give us : ", userinput)
#
# finally:
#     print("Thanks you for using this programm")

import re
import re
pattern = "^(?=.*[a-z0-9]) (?=.*[0-9])(?=.*[#@$!])"
text = "995krishna665"
if re.match(pattern, text, re.I):
    print("Match Found!")
else:
    print("Match Not Found!")
    