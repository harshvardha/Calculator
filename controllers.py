class controller:
    def __init__(self, viewObject, modelObject):
        self.viewObject = viewObject
        self.modelObject = modelObject
        self.buttonsDictionary = self.viewObject.getButtonsDictionary()
        rowNumberKeys = list(self.buttonsDictionary.keys())
        buttonObjectKeys: list
        for row in rowNumberKeys:
            buttonObjectKeys = list(self.buttonsDictionary[row].keys())
            for key in buttonObjectKeys:
                if(key in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]):
                    self.buttonsDictionary[row][key].bind("<Button-1>", self.operandEventHandler)
                elif(key in ["+", "-", "÷", "%", "×"]):
                    self.buttonsDictionary[row][key].bind("<Button-1>", self.binaryOperatorEventHandler)
                elif(key in ["1/x", "x²", "√", "+/-"]):
                    self.buttonsDictionary[row][key].bind("<Button-1>", self.unaryOperatorEventHandler)
                elif(key == "="):
                    self.buttonsDictionary[row][key].bind("<Button-1>", self.assignmentOperatorEventHandler)
                elif(key in ["CE", "C", "backSpace"]):
                    self.buttonsDictionary[row][key].bind("<Button-1>", self.clearanceOperatorEventHandler)
        self.viewObject.updateInputLabel(self.modelObject.getInputLabelText())
        self.viewObject.mainloop()
    
    def operandEventHandler(self, event):
        self.modelObject.operandEventHandler(event)
        self.updateEquationAndInputLabel()
    
    def unaryOperatorEventHandler(self, event):
        self.modelObject.unaryOperatorEventHandler(event)
        self.updateEquationAndInputLabel()
    
    def binaryOperatorEventHandler(self, event):
        self.modelObject.binaryOperatorEventHandler(event)
        self.updateEquationAndInputLabel()
    
    def assignmentOperatorEventHandler(self, event):
        self.modelObject.assignmentOperatorEventHandler(event)
        self.updateEquationAndInputLabel()
    
    def clearanceOperatorEventHandler(self, event):
        self.modelObject.clearanceOperatorEventHandler(event)
        self.updateEquationAndInputLabel()
    
    def updateEquationAndInputLabel(self):
        self.viewObject.updateInputLabel(self.modelObject.getInputLabelText())
        self.viewObject.updateEquationLabel(self.modelObject.getEquationLabelText())