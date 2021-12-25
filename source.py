import os, sys
import re

# r in front of string means raw string - no escape sequences e.g. "\n" will be accpeted!
path = r"C:\Users\1\Desktop\Python\Fritzbox\source_file.txt"

if os.path.exists(path)== False:
    print("source_file.txt does not exist!")

else:
    with open (r"c:\Users\1\Desktop\Python\Fritzbox\source_file.txt", "r") as d:
        data = d.readlines()

    def get_value(key):
        for element in data:
            x = re.search(key, element)
            if x != None:
                y = re.match(r'(.*) = (.*)', element, re.M|re.I)
                return(y.group(2))
            else:
                pass

print(get_value("EMAIL_USER2"))
print(get_value("EMAIL_PASS2"))
