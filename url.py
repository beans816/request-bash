import requests
import os

#make directory for file to copy into
directory = "cacheImag"
  
# Parent Directory path
parent_dir = "/home/be/Desktop/"
  
# mode
mode = 0o666
  
# Path
n_path = os.path.join(parent_dir, directory)
os.mkdir(n_path, mode)

url = "https://cdn.discordapp.com/attachments/882577135691264030/902309800308793415/om5han_On_Lisp_Advanced_Techniques_for_Common_Lisp-dd87aaeda934fdeeb5765b2a436e917a.png"
r = requests.get(url)

with open('test.png', 'wb') as f: #saves file
    newfile = f.write(r.content)
    command = "mv /home/be/Desktop/test.png /home/be/Desktop/cacheImag/test.png && sudo chmod 777 -R '/home/be/Desktop/cacheImag'" #command to be executed bash
    res = os.system(command)
