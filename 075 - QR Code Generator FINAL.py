import pyqrcode
from tkinter import *
from tkinter import messagebox

def genCode():
    inputString = enterTextField.get()
    scale = enterScaleField.get()

    if len(scale):
        try:
            scale = int(scale)

        except:
            messagebox.showerror("Error", "Scale should be an INTEGER.")

            return

    else:
        scale = 5

    if len(inputString):
        qrCode = pyqrcode.create(inputString)

        savePath = "C:\\Users\\Mohamed\\Documents\\Python Scripts\\" + inputString + "_" + str(scale)
        
        qrCode.png(savePath + ".png", scale = scale)
        qrCode.svg(savePath + ".svg", scale = scale)
        messagebox.showinfo("Success!", "Your QR code has been generated and saved in this location:" + savePath + ".png, .svg")

    else:
        messagebox.showerror("There has been a problem.", "Text field is empty.")
        
def clearAll():
    enterTextField.delete(0, END)
    enterScaleField.delete(0, END)
    #enterTextField.focus_set()

if __name__ == "__main__":
    window = Tk()
    window.configure(background = "grey")
    window.geometry("400x150")
    window.title("QR Code Generator")

    enterTextLabel = Label(window, text = "Type text here:", fg = "white", bg = "red")
    enterTextLabel.grid(row = 2, column = 1, sticky = "W", padx= "10", pady = "10")

    enterTextField = Entry(window)
    enterTextField.grid(row = 2, column = 2, sticky = "W", ipadx = "40", pady = "10")

    
    enterScaleLabel = Label(window, text = "Enter scale (1-10):", fg = "white", bg = "red")
    enterScaleLabel.grid(row = 3, column = 1, sticky = "W", padx = "10", pady = "10")

    enterScaleField = Entry(window)
    enterScaleField.grid(row = 3, column = 2, sticky = "W", pady = "10")

    generateButton = Button(window, text = "Generate QR code", bg = "blue", fg = "white", command = genCode)
    generateButton.grid(row = 4, column = 2, sticky = "W", pady = "5")

    clearButton = Button(window, text = "Clear", bg = "red", fg = "white", command = clearAll)
    clearButton.grid(row = 4, column = 3, sticky = "W", pady = "5")

    quitButton = Button(window, text = "QUIT", bg = "red", fg = "white", command = window.destroy)
    quitButton.grid(row = 4, column = 4, sticky = "W", pady = "5")

    window.mainloop()
