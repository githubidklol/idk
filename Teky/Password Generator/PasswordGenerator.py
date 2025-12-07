import random
from random import shuffle

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QGridLayout, QPushButton

letters = "abcdefghijklmnopqrstuvwxyz"
LETTERS = letters.upper()
numbers = "0123456789"
symbols = "`~!@$#$%^&*()_+-=<>?,./:;|"

class PassGenWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator 6700")
        self.setFixedSize(QSize(840, 360))
        self.container = QWidget(self)
        self.setCentralWidget(self.container)
        self.layout = QVBoxLayout()
        self.container.setLayout(self.layout)

        #Initialize Password Generator Components
        self.initComponents()

        #Run
        self.run()

    def initComponents(self):
        self.components = QWidget()
        self.grid = QGridLayout()
        self.grid.setHorizontalSpacing(0)

        #Description Info
        self.desc = QLabel("This is Password Generator 6700\n"
                           "You can input your desire password length, number of types of words in ease! (maybe)\n"
                           "Then you can click the \"GENERATE\" button to generate password\n"
                           "⚠WARNING: IT WILL NOT GENERATE PASSWORD IF YOUR INPUT IS INVALID⚠\n")
        self.descFont = QFont()
        self.descFont.setPointSize(14)
        self.descFont.setBold(True)
        self.desc.setFont(self.descFont)
        self.desc.setAlignment(Qt.AlignmentFlag.AlignTop.AlignLeft)
        self.desc.setWordWrap(True)
        self.grid.addWidget(self.desc, 0, 0, 1, 6)

        #Password Strength Info
        passStrengthInfos = [("DARK RED = VERY WEAK", "#7F0000"), ("        RED = WEAK", "#FF0000"), ("YELLOW = MEDIUM", "#FFFF00"), ("  GREEN = STRONG", "#00FF00"), ("DARK GREEN = VERY STRONG", "#007F00")]
        self.passStrengthInfoFont = QFont()
        self.passStrengthInfoFont.setPointSize(9)
        for id, (info, color) in enumerate(passStrengthInfos):
            self.passStrengthInfo = QLabel(info)
            self.passStrengthInfo.setStyleSheet(f"color: {color};")
            self.passStrengthInfo.setFont(self.passStrengthInfoFont)
            self.grid.addWidget(self.passStrengthInfo, 1, id)

        #Password Output
        self.passOutput = QLineEdit()
        self.passOutput.setPlaceholderText("This is where your password will be generated and can be copied here")
        self.passOutputFont = QFont()
        self.passOutputFont.setPointSize(19)
        self.passOutput.setFont(self.passOutputFont)
        self.passOutput.setReadOnly(True)
        self.passOutput.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.passOutput.setFixedHeight(40)
        self.grid.addWidget(self.passOutput, 2, 0, 1, 6)

        #Input Info
        inputsInfo = ["Your Password\nRequirements:", "     # letters:", "   # LETTERS:", "  # Numbers:", "      # Symbols:", "    Password\n      length:"]
        self.inputsInfo = {}
        self.inputInfoFont = QFont()
        self.inputInfoFont.setPointSize(14)
        for id, inputInfo in enumerate(inputsInfo):
            self.inputsInfo[id] = QLabel(inputInfo)
            self.inputsInfo[id].setFont(self.inputInfoFont)
            self.grid.addWidget(self.inputsInfo[id], 3, id)

        #Generate Password
        self.generateButton = QPushButton()
        self.generateButton.setText("GENERATE")
        self.generateButtonFont = QFont()
        self.generateButtonFont.setPointSize(19)
        self.generateButtonFont.setBold(True)
        self.generateButton.setFont(self.generateButtonFont)
        self.generateButton.setFixedSize(QSize(140, 60))
        self.grid.addWidget(self.generateButton, 4, 0)

        #Input
        self.inputs = {}
        self.inputFont = QFont()
        self.inputFont.setPointSize(14)
        for id, input in enumerate(inputsInfo):
            if input == inputsInfo[0]: continue
            self.inputs[id] = QLineEdit()
            self.inputs[id].setPlaceholderText("0 ~ 1000") if id<5 else self.inputs[id].setPlaceholderText("0 ~ 5000")
            self.inputs[id].setFont(self.inputFont)
            self.grid.addWidget(self.inputs[id], 4, id)

        self.components.setLayout(self.grid)
        self.layout.addWidget(self.components)

    def run(self):
        self.generateButton.clicked.connect(self.generate)

    def generate(self):
        #Check Inputs
        totalRequiredChar, passLength, hasChar, charCount= 0, 0, 0, [0 for _ in range(4)]
        for id, input in enumerate(self.inputs.values()):
            string = input.text()
            hasChar = bool(string)
            if not hasChar or string.isdigit():
                #If valid
                if hasChar:
                    val = int(string)
                    if id == 4:
                        #If password length input is out of input range
                        if val>5000:
                            self.updateOutput(f"\"{self.inputsInfo[id+1].text().replace(" ", "")}\" input value is OUT OF INPUT RANGE ({val}>5000)", "#FF0000")
                            return
                        passLength = val
                    else:
                        #If one of other inputs is out of input range
                        if val>1000:
                            self.updateOutput(f"\"{self.inputsInfo[id+1].text().strip()}\" input value is OUT OF INPUT RANGE ({val}>1000)", "#FF0000")
                            return
                        charCount[id] = val
                        totalRequiredChar += val
            else:
                #If not, print where is invalid (priority: left -> right)
                if id == 4:
                    self.updateOutput(f"INVALID input detected in \"{self.inputsInfo[id+1].text().replace(" ", "")}\" Input!", "#FF0000")
                else:
                    self.updateOutput(f"INVALID input detected in \"{self.inputsInfo[id+1].text().strip()}\" Input!", "#FF0000")
                return

        #If password length < 4
        if (passLength < 4):
            self.updateOutput("Your password length MUST BE bigger or equal to 4 !", "#FF0000")
        #If required char > password length
        if totalRequiredChar>passLength:
            self.updateOutput(f"Total number of required char MUST BE smaller than password length! (# required char: {totalRequiredChar}, password length: {passLength})", "#FF0000")
            return

        #Generate password
        password = []
        for _ in range(charCount[0]):
            password.append(random.choice(letters))
        random.shuffle(password)
        for _ in range(charCount[1]):
            password.append(random.choice(LETTERS))
        random.shuffle(password)
        for _ in range(charCount[2]):
            password.append(random.choice(numbers))
        random.shuffle(password)
        for _ in range(charCount[3]):
            password.append(random.choice(symbols))
        random.shuffle(password)
        passLength -= totalRequiredChar
        for _ in range(passLength):
            password.append(random.choice(letters+LETTERS+numbers+symbols))
        random,shuffle(password)
        string = "".join(password)
        self.updateOutput(string, self.analyseStrength(string))

    #Check char type
    def check(self, c):
        if c.isdigit(): return 0
        if c.isalpha():
            if c.islower(): return 1
            return 2
        return 3

    #Analyse password strength
    def analyseStrength(self, password):
        hasChar, strength, prev1, prev2, count1, distinct1, distinct2 = [0 for _ in range(4)], 0, None, None, 0, 0, 0
        for id, c in enumerate(password):
            t = self.check(c)
            hasChar[t] += 1
            if prev1 != None and c==prev1:
                count1 += 1
                if count1>2: strength -= 1
                distinct1 = 1
            else:
                distinct1 += 1
                if distinct1>2: strength += 1
                prev1 = c
                count1 = 1
            if prev2 != None and t==prev2:
                distinct2 = 1
            else:
                distinct2 += 1
                if distinct2>2: distinct2 += 1
                prev2 = t
        strength += int(4**(sum([bool(_) for _ in hasChar])-1))+int(1.5**len(password))+int(3**(min(hasChar)-1))
        print(strength)
        if strength<20: return "#7F0000"
        if strength<40: return "#FF0000"
        if strength<80: return "#FFFF00"
        if strength<120: return "#00FF00"
        return "#007F00"


    def updateOutput(self, output, color):
        self.passOutput.setStyleSheet(f"color: {color};")
        self.passOutput.setText(output)