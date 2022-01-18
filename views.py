import tkinter
from tkinter import font

class calculatorButton(tkinter.Button):
    def __init__(self, parent, background = None, **kwargs):
        super().__init__(master=parent, **kwargs)
        self.background = ""
        if(background==None):
            self.background = kwargs["bg"]
        else:
            self.background = background
        self.bind("<Enter>", self._enterEventHandler)
        self.bind("<Leave>", self._leaveEventHandler)
    
    def _enterEventHandler(self, event):
        self.configure(background="#7f7f7f")
    
    def _leaveEventHandler(self, event):
        self.configure(background=self.background)
    
    def bindMouseButton1Event(self, callbackFunction):
        self.bind("<Button-1>", callbackFunction)

class StandardView(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.configure(bg="#383837")
        self.attributes('-alpha', 0.9)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        self.title("Calculator")
        self.labelsDictionary = {}
        self.buttonsDictionary = {}

        # title containing frame
        titleFrame = tkinter.Frame(master=self, bg="#383837", bd=0)
        titleFrame.grid(row=0, column=0, sticky=tkinter.W, padx=13, pady=10)
        titleFrame.columnconfigure(0, weight=1)

        # input label frame
        inputFrame = tkinter.Frame(master=self, bg="#383837", bd=0)
        inputFrame.grid(row=1, column=0, sticky=tkinter.E)
        inputFrame.columnconfigure(0, weight=1)

        # calculator buttons frame
        self.buttonsFrame = tkinter.Frame(master=self, bg="#383837", bd=0)
        self.buttonsFrame.grid(row=2, column=0, sticky=(tkinter.W, tkinter.E, tkinter.N, tkinter.S), padx=3, pady=5)
        for i in range(4):
            self.buttonsFrame.columnconfigure(i, weight=1)
        for j in range(6):
            self.buttonsFrame.rowconfigure(j, weight=1)
        self.buttonsFrame.focus_set()

        # calling the labels creater function
        self.createLabels(titleFrame, inputFrame)

        # calling the buttons creater function
        self.createButtons(self.buttonsFrame)
    
    def createLabels(self, tF, iF):
        # common style dictionary for labels
        labelStyle = {
            "bg": "#383837",
            "fg": "#ffffff",
            "bd": 0
        }
        
        # dictionary for labels
        self.labelsDictionary["titleLabel"] = tkinter.Label(
            master=tF, text="Standard", font=("sanserif", 17), **labelStyle
        )
        self.labelsDictionary["titleLabel"].grid(row=0, column=0, sticky=tkinter.W)

        self.labelsDictionary["equationLabel"] = tkinter.Label(
            master=iF, text="", font=("sanserif", 11), **labelStyle
        )
        self.labelsDictionary["equationLabel"].grid(row=0, column=0, sticky=tkinter.E, padx=5)

        self.labelsDictionary["inputLabel"] = tkinter.Label(
            master=iF, text="", font=("sanserif", 40, "bold"), **labelStyle
        )
        self.labelsDictionary["inputLabel"].grid(row=1, column=0, sticky=tkinter.E, padx=5)
    
    def createButtons(self, bF):

        #style theme for operator buttons like +, /, -, etc...
        operatorButtonsStyle = {
            "bd": 0,
            "bg": "#1f1f1e",
            "fg": "#ffffff",
            "font": ("sanserif", 16)
        }

        #style theme for operand buttons like 1, 2, 3, etc...
        operandButtonsStyle = {
            "bd": 0,
            "bg": "#000000",
            "fg": "#ffffff",
            "font": ("sanserif", 16)
        }

        #buttons for first row i.e; row=0
        self.buttonsDictionary[0] = {
            "%": calculatorButton(parent=bF, text="%", **operatorButtonsStyle),
            "CE": calculatorButton(parent=bF, text="CE", **operatorButtonsStyle),
            "C": calculatorButton(parent=bF, text="C", **operatorButtonsStyle),
            "backSpace": calculatorButton(parent=bF, text="<-", **operatorButtonsStyle)
        }

        #buttons for 2nd row i.e; row=1
        self.buttonsDictionary[1] = {
            "1/x": calculatorButton(parent=bF, text="1/x", **operatorButtonsStyle),
            "x²": calculatorButton(parent=bF, text="x²", **operatorButtonsStyle),
            "√": calculatorButton(parent=bF, text="√x", **operatorButtonsStyle),
            "÷": calculatorButton(parent=bF, text="÷", **operatorButtonsStyle)
        }

        # buttons for 3rd row i.e. row=2
        self.buttonsDictionary[2] = {
            "7": calculatorButton(parent=bF, text="7", **operandButtonsStyle),
            "8": calculatorButton(parent=bF, text="8", **operandButtonsStyle),
            "9": calculatorButton(parent=bF, text="9", **operandButtonsStyle),
            "×": calculatorButton(parent=bF, text="×", **operatorButtonsStyle)
        }
        
        # buttons for 4th row i.e. row=3
        self.buttonsDictionary[3] = {
            "4": calculatorButton(parent=bF, text="4", **operandButtonsStyle),
            "5": calculatorButton(parent=bF, text="5", **operandButtonsStyle),
            "6": calculatorButton(parent=bF, text="6", **operandButtonsStyle),
            "-": calculatorButton(parent=bF, text="-", **operatorButtonsStyle)
        }

        #buttons for 5th row i.e. row=4
        self.buttonsDictionary[4] = {
            "1": calculatorButton(parent=bF, text="1", **operandButtonsStyle),
            "2": calculatorButton(parent=bF, text="2", **operandButtonsStyle),
            "3": calculatorButton(parent=bF, text="3", **operandButtonsStyle),
            "+": calculatorButton(parent=bF, text="+", **operatorButtonsStyle)
        }

        #buttons for 6th row i.e. row=5
        self.buttonsDictionary[5] = {
            "+/-": calculatorButton(parent=bF, text="+" + "/" + "-", **operatorButtonsStyle),
            "0": calculatorButton(parent=bF, text="0", **operandButtonsStyle),
            ".": calculatorButton(parent=bF, text=".", **operatorButtonsStyle),
            "=": calculatorButton(parent=bF, text="=", background="#5c5c5c", **operatorButtonsStyle)
        }

        # placing the buttons
        for i in range(6):
            for j, button in enumerate(self.buttonsDictionary[i].values()):
                if (i % 2 == 0):
                    if (j % 2 == 0):
                        button.grid(row=i, column=j, sticky=(tkinter.W, tkinter.E, tkinter.N, tkinter.S), padx=2, pady=2)
                    elif (j % 2 != 0):
                        button.grid(row=i, column=j, sticky=(tkinter.W, tkinter.E, tkinter.N, tkinter.S), pady=2)
                elif (i % 2 != 0):
                    if (j % 2 == 0):
                        button.grid(row=i, column=j, sticky=(tkinter.W, tkinter.E, tkinter.N, tkinter.S), padx=2)
                    elif (j % 2 != 0):
                        button.grid(row=i, column=j, sticky=(tkinter.W, tkinter.E, tkinter.N, tkinter.S))

    def getButtonsDictionary(self):
        return self.buttonsDictionary
    
    def updateInputLabel(self, data):
        if(data != None and len(data) >= 0):
            self.labelsDictionary["inputLabel"].configure(text = data)
    
    def updateEquationLabel(self, data):
        if(data != None and len(data) >= 0):
            self.labelsDictionary["equationLabel"].configure(text = data)