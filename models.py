class StandardModel:
    def __init__(self):
        self._result = 0.0
        self.inputLabelText = "0"
        self.equationLabelText = ""
        self._operator = ""
        self._operand2 = 0.0
    
    def operandEventHandler(self, event):
        if(event.widget.cget("text") == "." and self.inputLabelText.find(".") == -1):
            if(self.inputLabelText == ""):
                self.inputLabelText = "0."
            else:
                self.inputLabelText += "."
        else:
            if(self.inputLabelText != "0" and self._result != float(self.inputLabelText)):
                self.inputLabelText += event.widget.cget("text")
            else:
                self.inputLabelText = event.widget.cget("text")
                if(len(self.equationLabelText) > 0 and self.equationLabelText[-1] == "="):
                    self.equationLabelText = ""
    
    def unaryOperatorEventHandler(self, event):
        self._operand2 = float(self.inputLabelText)
        self._operator = event.widget.cget("text")
        if(self._operator == "1/x" and self._operand2 != 0):
            self._result = 1 / self._operand2
            self._buildEquationLabelString("1/")
        elif(self._operator == "x²"):
            self._result = self._operand2 ** 2
            self._buildEquationLabelString("sqr")
        elif(self._operator == "√x"):
            self._result = self._operand2 ** 0.5
            self._buildEquationLabelString("√")
        elif(self._operator == "+/-"):
            self._result = self._operand2 * -1
            self._buildEquationLabelString("negate")
        if(self._result == int(self._result)):
            self.inputLabelText = str(int(self._result))
        else:
            self.inputLabelText = str(self._result)
    
    def binaryOperatorEventHandler(self, event):
        if(self.equationLabelText == ""):
            self._result = float(self.inputLabelText)
            self._operator = event.widget.cget("text")
            self.equationLabelText = self.inputLabelText + self._operator
        elif(float(self.inputLabelText) == self._result):
            self._operator = event.widget.cget("text")
            if(self.equationLabelText[-1] == "="):
                self.equationLabelText = self.inputLabelText + self._operator
            else:
                self.equationLabelText = self.equationLabelText[:len(self.equationLabelText)-1] + self._operator
        else:
            self._operand2 = float(self.inputLabelText)
            self._calculateResult()
            if(int(self._result) == self._result):
                self.inputLabelText = str(int(self._result))
            else:
                self.inputLabelText = str(float(self._result))
            self._operator = event.widget.cget("text")
            self.equationLabelText = self.inputLabelText + self._operator
    
    def assignmentOperatorEventHandler(self, event):
        if(self._operator in ["x²", "√x", "1/x", "+/-"]):
            self.equationLabelText += "="
        elif(self._operator in ["+", "-", "×", "÷", "%"]):
            self._operand2 = float(self.inputLabelText)
            self._calculateResult()
            if(int(self.inputLabelText) == self._operand2):
                self.equationLabelText += str(int(self._operand2)) + "="
            else:
                self.equationLabelText += str(float(self._operand2)) + "="
            if(int(self._result) == self._result):
                self.inputLabelText = str(int(self._result))
            else:
                self.inputLabelText = str(float(self._result))
    
    def clearanceOperatorEventHandler(self, event):
        if(event.widget.cget("text") == "CE"):
            self._operand2 = 0.0
            self.inputLabelText = "0"
        elif(event.widget.cget("text") == "C"):
            self._operand2 = 0.0
            self.inputLabelText = "0"
            self._result = 0.0
            self.equationLabelText = ""
        elif(event.widget.cget("text") == "<-" and self._result != float(self.inputLabelText)):
            self.inputLabelText = self.inputLabelText[:len(self.inputLabelText)-1]
            if(self.inputLabelText != ""):
                self._operand2 = float(self.inputLabelText)
            else:
                self._operand2 = 0.0
                self.inputLabelText = "0"
    
    def _calculateResult(self):
        if(self._operator == "+"):
            self._result += self._operand2
        elif(self._operator == "×"):
            self._result *= self._operand2
        elif(self._operator == "-"):
            self._result -= self._operand2
        elif(self._operator == "%" and self._operand2 != 0):
            self._result %= self._operand2
        elif(self._operator == "÷" and self._operand2 != 0):
            self._result /= self._operand2
    
    def _buildEquationLabelString(self, operator):
        if(len(self.equationLabelText)==0):
            self.equationLabelText += operator + "(" + str(int(self._operand2)) + ")"
        elif(len(self.equationLabelText) > 0 and self.equationLabelText[-1] == "="):
            self.equationLabelText = operator + "(" + self.inputLabelText + ")"
        else:
            temp = 0
            for i in range(len(self.equationLabelText)-1, -1, -1):
                if(self.equationLabelText[i] in ["+", "-", "×", "%", "÷"]):
                    temp = i + 1
                    if(temp < len(self.equationLabelText)):
                        self.equationLabelText = self.equationLabelText[:temp] + operator + "(" + self.equationLabelText[temp:] + ")"
                    else:
                        self.equationLabelText = self.equationLabelText[:temp] + operator + "(" + self.inputLabelText + ")"
                    break
                elif(self.equationLabelText[i] == "="):
                    self.equationLabelText = operator + "(" + str(self._operand2) + ")"
                    break
            if(temp == 0):
                self.equationLabelText = operator + "(" + self.equationLabelText + ")"

    def getInputLabelText(self):
        return self.inputLabelText
    
    def getEquationLabelText(self):
        return self.equationLabelText