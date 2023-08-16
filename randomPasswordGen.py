import tkinter as tk
import random



#Basic temp for whole window
window = tk.Tk()
window.title("EZPass Secure Password Generator")
window.geometry("480x480")
window.maxsize(480,480)
window.config(background="#B0E0E6")

topText = tk.Label(window, text="Secure Password Generator!", height=3, font=("SimSun",20),  background="#B0E0E6")
topText.pack()


passFrame = tk.Frame(window, bg="#B0E0E6")
passFrame.pack()
passwordSizeLabel = tk.Label(passFrame,text="Password Length: ", font=("SimSun", 12), background="#B0E0E6")
passwordSizeLabel.pack(side="left",padx=1)


passEntry = tk.Entry(passFrame)
passEntry.pack(side="right")

#Function to generate the password and with added functionality for exlcuding special characters based on user needs
def generateClicked():
    passwordSize = int(passEntry.get())
    if passwordSize <= 0 or passwordSize > 50:
        generatedPasswordLabel.config(text="Error: Failed To Meet Password Size Requirements")
        return
    
    excludeSpecialCharacters = excludeCharacters.get()
    autoCopyToClipboard = automaticallyCopyClipboard.get()

    special_characters = '!@#$*'
    numbers = '0123456789'
    letters = 'abcdefghijklmnopqrstuvwxyz'
    upperCaseletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


    allTogether = special_characters + numbers + letters + upperCaseletters
    if excludeSpecialCharacters:
        allTogether = numbers + letters + upperCaseletters

    global generatedPassword
    generatedPassword = ''.join(random.choice(allTogether) for _ in range(passwordSize))
    generatedPasswordLabel.config(text="Generated Password: \n" + generatedPassword)

    if autoCopyToClipboard:
       window.clipboard_clear()
       window.clipboard_append(generatedPassword)
       window.update()



#Selectables Frame and methods for functionality
selectablesFrame = tk.Frame(window, bg="#B0E0E6")
selectablesFrame.pack()

excludeCharacters = tk.BooleanVar()
excludeSpecialChars = tk.Checkbutton(selectablesFrame, text="Exclude Special Characters", variable=excludeCharacters, background="#B0E0E6", height=3)
excludeSpecialChars.pack()

automaticallyCopyClipboard = tk.BooleanVar()
autoCopyClip = tk.Checkbutton(selectablesFrame, text="Automatically Copy To Clipboard", variable=automaticallyCopyClipboard, background="#B0E0E6", height=3)
autoCopyClip.pack()

generateButton = tk.Button(text="Generate Password", padx=10, pady=10, command=generateClicked)
generateButton.pack()

generatedPasswordLabel = tk.Label(window, text="Generated Password: ", background="#B0E0E6", height=3,  font=("SimSun", 12))
generatedPasswordLabel.pack()





#Allows for the program to run while this loop is active
window.mainloop()