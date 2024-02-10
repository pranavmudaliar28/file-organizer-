import os, shutil

try:
    os.mkdir("Documents")
    os.mkdir("Video")
    os.mkdir("Audio")
    os.mkdir("Pictures")
    os.mkdir("Zip")
    os.mkdir("Other")
except Exception as e:
    pass
audio=["mp3","wav"]
video=["mp4","mov"]
documents=["docx","pptx","txt"]
pictures=["png","jpg","jpeg","webp"]
zip=["zip","rar"]

for file in os.listdir():
    name,ext=os.path.splitext(file)
    for i in audio:
        if i in ext.lower():
            if os.path.isfile(file):
                shutil.move(file,"Audio")
    for i in documents:
        if i in ext.lower():
            if os.path.isfile(file):
                shutil.move(file,"Documents")
    for i in video:
        if i in ext.lower():
            if os.path.isfile(file):
                shutil.move(file,"Video")
    for i in pictures:
        if i in ext.lower():
            if os.path.isfile(file):
                shutil.move(file,"Pictures")
    for i in zip:
        if i in ext.lower():
            if os.path.isfile(file):
                shutil.move(file,"Zip")
    else:
        if os.path.isfile(file):
            shutil.move(file, "Other")