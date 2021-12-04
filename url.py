import requests
import os

#make directory for file to copy into
directory = "cacheImage"
  
# Parent Directory path
parent_dir = "/home/be/Desktop/"
  
# mode
mode = 0o666
  
# Path
n_path = os.path.join(parent_dir, directory)
os.mkdir(n_path, mode)

url = "https://cdn.discordapp.com/attachments/882577135691264030/902309800308793415/om5han_On_Lisp_Advanced_Techniques_for_Common_Lisp-dd87aaeda934fdeeb5765b2a436e917a.png"
r = requests.get(url)
filename = url.split('/')[-1] 

with open(filename, 'wb') as f: #saves file
    newfile = f.write(r.content)
    command = "mv /home/be/Desktop/" + filename + " /home/be/Desktop/cacheImage/" + filename + " && sudo chmod 777 -R '/home/be/Desktop/cacheImage'" #command to be executed bash
    res = os.system(command)
