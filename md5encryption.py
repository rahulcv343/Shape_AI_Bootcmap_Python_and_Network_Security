# -*- coding: utf-8 -*-
"""md5encryption.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KqIYIgwBlwzLm_N4hCs_WKE5igFedPKl
"""

import hashlib 

name = input("enter the value : ")

result = hashlib.md5(name.encode())

print("your md5 encrption is :")
print(result.hexdigest())