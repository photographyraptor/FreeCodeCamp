class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        lines = []
        lenName = int((30 - len(self.name)) / 2)
        lines.append(("*" * lenName) + self.name + ("*" * lenName))

        for ledge in self.ledger:
            am = _toString(ledge["amount"])
            lines.append(_lineFormatted(ledge["description"], am))
            
        bal = _toString(self.get_balance())
        lines.append("Total: " + bal)
        line = "\n".join(lines)
        return line

    def getName(self):
        return self.name        
        
    def deposit(self, amount, description:str=""):
        self.ledger.append({
            "amount": amount,
            "description": description})

    def withdraw(self, amount, items:str=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": amount * -1,
                "description": items})
            return True
        return False

    def get_balance(self):
        balance = 0
        for led in self.ledger:
            amount = led["amount"]
            balance += amount
        return balance

    def transfer(self, amount, to):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + to.name)
            to.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        oldBalance = self.get_balance()
        if oldBalance >= amount:
            return True
        return False

def _toString(num):
    str_num = str(num)
    decimal_index = str_num.find(".")
    if decimal_index == -1:
        str_num += ".00"
    return str_num

def _lineFormatted(first:str, last:str):
    charsLeft = 30 - len(last)
    charsFirst = len(first)
    line = ""
    if (charsFirst > charsLeft):
        line = first[0:(charsLeft-1)] + " " + last
    elif (charsFirst < charsLeft):
        line = first + (" " * (charsLeft - charsFirst)) + last
    else:
        line = first + " " + last
    
    return line

def _cleanCategories(categories):
    categSpent = []
    totalSpent = 0

    for categ in categories:
        spent = 0
        for ledge in categ.ledger:
            if (ledge["amount"] < 0):
                spent += (-1) * ledge["amount"]
        categSpent.append({ "categ": categ.getName(), "spent": spent })
        totalSpent += spent

    for catSpent in categSpent:
        catSpent["spent"] = round(catSpent["spent"] / totalSpent * 100)
        catSpent["spent"] = catSpent["spent"] - (catSpent["spent"] % 10) 

    return categSpent

def _getPercentile(nth, cleanData):
    line = ""
    if (nth == 0):
        line += "  0|"
    elif (nth == 100):
        line += "100|"
    else :
        line += " " + str(nth) + "|"

    line += _percLowerThanNth(nth, cleanData)
    return line

def _percLowerThanNth(nth, cleanData):
    line = ""
    for cleanRow in cleanData:
        if (cleanRow["spent"] >= nth):
            line += " o "
        else:
            line += "   "
    line += " "
    return line

def _getNamesVert(cleanData):
    maxLength = 0
    for cleanRow in cleanData:
        maxLength = max(maxLength, len(cleanRow["categ"]))
    
    lines = []
    for i in range(0, maxLength, 1):
        lines.append("    ")
        for cleanRow in cleanData:
            if (len(cleanRow["categ"]) > i):
                print(cleanRow["categ"][i])
                lines[i] += " " + cleanRow["categ"][i] + " "
            else:
                lines[i] += "   "
        lines[i] += " " 
    return lines  

def create_spend_chart(categories):
    cleanData = _cleanCategories(categories)
    
    lines = ["Percentage spent by category"]
    for i in range(100, -1, -10):
        lines.append(_getPercentile(i, cleanData))
    lines.append("    " +  ("---" * len(cleanData)) + "-")
    lines += _getNamesVert(cleanData)

    line = "\n".join(lines)
    return line