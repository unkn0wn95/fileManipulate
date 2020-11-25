import os,sys
folder = '/file/location'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.mp4', '.txt')
       output = os.rename(infilename, newname)
