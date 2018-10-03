import os
if os.path.exists("Python-Playground/ManipulateFiles/Created File.txt"):
  os.remove("Python-Playground/ManipulateFiles/Created File.txt")
else:
  print("The file does not exist")