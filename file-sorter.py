import os
import re
import shutil

folderName = input("Please enter folder name where your site files are located:")
fileName = input("Please enter the filename of your stored website files:")

path = "/Users/David/Documents/"+folderName+"/"+fileName+"_files/"
htmlPath = 'C:/Users/David/Documents/'+folderName+'/'+fileName+'.html'

names = os.listdir(path)

for name in names:
    if (name == "css" and name != "Cascading_Style_Sheet"):
        os.rename(path+name, path + "Cascading_Style_Sheet")
        print('NOTIFICATION: Changed css file --> Cascading_Style_Sheet')
    if (name == "js" and name != "Javascripts"):
        os.rename(path+name, path + "Javascripts")
        print('NOTIFICATION: Changed js file --> Javascripts')
    
folder_name = ['images', 'css', 'js']
for x in range(0,3):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])

for files in names:
    if ".PNG" in files and not os.path.exists(path + 'images/' + files):
        shutil.move(path + files, path + 'images/' + files)
    if ".png" in files and not os.path.exists(path + 'images/' + files):
        shutil.move(path + files, path + 'images/' + files)
    if ".jpg" in files and not os.path.exists(path + 'images/' + files):
        shutil.move(path + files, path + 'images/' + files)
    if ".jpeg" in files and not os.path.exists(path + 'images/' + files):
        shutil.move(path + files, path + 'images/' + files)
    if ".JPG" in files and not os.path.exists(path + 'images/' + files):
        shutil.move(path + files, path + 'images/' + files)
    if ".SVG" in files and not os.path.exists(path + 'images/' + files):
        shutil.move(path + files, path + 'images/' + files)
    if ".svg" in files and not os.path.exists(path + 'images/' + files):
        shutil.move(path + files, path + 'images/' + files)
    if ".GIF" in files and not os.path.exists(path + 'images/' + files):
        shutil.move(path + files, path + 'images/' + files)
    if ".gif" in files and not os.path.exists(path + 'images/' + files):
        shutil.move(path + files, path + 'images/' + files)
    if ".css" in files and not os.path.exists(path + 'css/' + files):
        shutil.move(path + files, path + 'css/' + files)
    if ".webp" in files and not os.path.exists(path + 'images/' + files):
        shutil.move(path + files, path + 'images/' + files)
    if ".js" in files and not os.path.exists(path + 'js/' + files):
        shutil.move(path + files, path + 'js/' + files)

with open(htmlPath, 'r', encoding="utf-8") as htmlFile:
    with open(path+fileName+'2.html', 'w', encoding="utf-8") as htmlWrite:
        for line in htmlFile:
            string = line
            jsPatterns = ["\.\/"+fileName+"_files+(\/+[a-zA-Z0-9]+[^a-zA-Z0-9]+[a-zA-Z0-9]+\.+js)", "\.\/"+fileName+"_files+(\/[a-zA-Z0-9]+\.+js)", "\.\/"+fileName+"_files+(\/[-_%&0-9a-zA-Z \.]+\.+js)",fileName+"_files+(\/+[a-zA-Z0-9]+[^a-zA-Z0-9]+[a-zA-Z0-9]+\.+js)", fileName+"_files+(\/[a-zA-Z0-9]+\.+js)", fileName+"_files+(\/[-_%&0-9a-zA-Z \.]+\.+js)"]

            cssPatterns = ["\.\/"+fileName+"_files+(\/+[a-zA-Z0-9]+[^a-zA-Z0-9]+[a-zA-Z0-9]+\.+css)", "\.\/"+fileName+"_files+(\/[a-zA-Z0-9]+\.+css)", "\.\/"+fileName+"_files+(\/[-_%&+0-9a-zA-Z\. ]+\.+css)",fileName+"_files+(\/+[a-zA-Z0-9]+[^a-zA-Z0-9]+[a-zA-Z0-9]+\.+css)", fileName+"_files+(\/[a-zA-Z0-9]+\.+css)", fileName+"_files+(\/[-_%&+0-9a-zA-Z\. ]+\.+css)"]

            pngPatterns = ["\.\/"+fileName+"_files+(\/+[a-zA-Z0-9]+[^a-zA-Z0-9]+[a-zA-Z0-9]+\.+png)", "\.\/"+fileName+"_files+(\/[a-zA-Z0-9]+\.+png)", "\.\/"+fileName+"_files+(\/[-_%&+0-9a-zA-Z\. ]+\.+png)",fileName+"_files+(\/+[a-zA-Z0-9]+[^a-zA-Z0-9]+[a-zA-Z0-9]+\.+png)", fileName+"_files+(\/[a-zA-Z0-9]+\.+png)", fileName+"_files+(\/[-_%&+0-9a-zA-Z\. ]+\.+png)"]

            jpgPatterns = ["\.\/"+fileName+"_files+(\/+[a-zA-Z0-9]+[^a-zA-Z0-9]+[a-zA-Z0-9]+\.+jpg)", "\.\/"+fileName+"_files+(\/[a-zA-Z0-9]+\.+jpg)", "\.\/"+fileName+"_files+(\/[-_%&+0-9a-zA-Z\. ]+\.+jpg)",fileName+"_files+(\/+[a-zA-Z0-9]+[^a-zA-Z0-9]+[a-zA-Z0-9]+\.+jpg)", fileName+"_files+(\/[a-zA-Z0-9]+\.+jpg)", fileName+"_files+(\/[-_%&+0-9a-zA-Z\. ]+\.+jpg)"]

            jpegPatterns = ["\.\/"+fileName+"_files+(\/+[a-zA-Z0-9]+[^a-zA-Z0-9]+[a-zA-Z0-9]+\.+jpeg)", "\.\/"+fileName+"_files+(\/[a-zA-Z0-9]+\.+jpeg)", "\.\/"+fileName+"_files+(\/[-_%&+0-9a-zA-Z\. ]+\.+jpeg)",fileName+"_files+(\/+[a-zA-Z0-9]+[^a-zA-Z0-9]+[a-zA-Z0-9]+\.+jpeg)", fileName+"_files+(\/[a-zA-Z0-9]\.+jpeg)", fileName+"_files+(\/[-_%&+0-9a-zA-Z\. ]+\.+jpeg)"]

            svgPatterns = ["\.\/"+fileName+"_files+(\/+[a-zA-Z0-9]+[^a-zA-Z0-9]+[a-zA-Z0-9]+\.+svg)", "\.\/"+fileName+"_files+(\/[a-zA-Z0-9]+\.+svg)", "\.\/"+fileName+"_files+(\/[-_%&+0-9a-zA-Z\. ]+\.+svg)",fileName+"_files+(\/+[a-zA-Z0-9]+[^a-zA-Z0-9]+[a-zA-Z0-9]+\.+svg)", fileName+"_files+(\/[a-zA-Z0-9]+\.+svg)", fileName+"_files+(\/[-_%&+0-9a-zA-Z\. ]+\.+svg)"]

            gifPatterns = ["\.\/"+fileName+"_files+(\/+[a-zA-Z0-9]+[^a-zA-Z0-9]+[a-zA-Z0-9]+\.+gif)", "\.\/"+fileName+"_files+(\/[a-zA-Z0-9]+\.+gif)", "\.\/"+fileName+"_files+(\/[-_%&+0-9a-zA-Z\. ]+\.+gif)",fileName+"_files+(\/+[a-zA-Z0-9]+[^a-zA-Z0-9]+[a-zA-Z0-9]+\.+gif)", fileName+"_files+(\/[a-zA-Z0-9]+\.+gif)", fileName+"_files+(\/[-_%&+0-9a-zA-Z\. ]+\.+gif)"]

            webpPatterns = ["\.\/"+fileName+"_files+(\/+[a-zA-Z0-9]+[^a-zA-Z0-9]+[a-zA-Z0-9]+\.+webp)", "\.\/"+fileName+"_files+(\/[a-zA-Z0-9]+\.+webp)", "\.\/"+fileName+"_files+(\/[-_%&+0-9a-zA-Z\. ]+\.+webp)",fileName+"_files+(\/+[a-zA-Z0-9]+[^a-zA-Z0-9]+[a-zA-Z0-9]+\.+webp)", fileName+"_files+(\/[a-zA-Z0-9]+\.+wbp)", fileName+"_files+(\/[-_%&+0-9a-zA-Z\. ]+\.+webp)"]
            for pattern in jsPatterns: 
                string = re.sub(pattern, 'js'+ r'\1', string)
            for pattern in cssPatterns: 
                string = re.sub(pattern, 'css'+ r'\1', string)
            for pattern in pngPatterns: 
                string = re.sub(pattern, 'images'+ r'\1', string)
            for pattern in jpgPatterns: 
                string = re.sub(pattern, 'images'+ r'\1', string)
            for pattern in jpegPatterns: 
                string = re.sub(pattern, 'images'+ r'\1', string)
            for pattern in svgPatterns: 
                string = re.sub(pattern, 'images'+ r'\1', string)
            for pattern in gifPatterns: 
                string = re.sub(pattern, 'images'+ r'\1', string)
            for pattern in webpPatterns: 
                string = re.sub(pattern, 'images'+ r'\1', string)
                
            htmlWrite.write(string)
print('success!')

 





