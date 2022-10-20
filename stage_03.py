with open("artifacts01.txt", "r") as f:
    text = f.read()


with open("artifacts02.txt", "w") as f:
    text = f.write(text + "added lines")

print("end of stage 03")
#git remote add origin https://github.com/mohan143341/DVC-basic-demo.git
