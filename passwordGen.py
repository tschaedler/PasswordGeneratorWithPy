import random

s = "abcdefghijkl\
mnopqrstuvwxyz1234\
4567890ABCDEFGHIJKLM\
NOPQRSTUVWXYZ!@%$^&*\
()_-+[]{};/';:;#"
passwordlen = 20
password = "".join(random.sample(s, passwordlen))
print(password)
input("Press Enter to exit...")
