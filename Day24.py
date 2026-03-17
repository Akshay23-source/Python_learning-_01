import os

folder_path = "your_folder_path"

files = os.listdir(folder_path)

for i, file in enumerate(files):
    old_name = os.path.join(folder_path, file)
    new_name = os.path.join(folder_path, f"file_{i}.txt")
    
    os.rename(old_name, new_name)
    
    
    
    
    
  import os
import shutil

source = "your_folder"

for file in os.listdir(source):
    if file.endswith(".jpg"):
        shutil.move(file, "images/")
        
        
        
        
        
  import webbrowser

webbrowser.open("https://google.com")      