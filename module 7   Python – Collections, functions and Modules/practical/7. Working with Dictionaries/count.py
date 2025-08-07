# Count Frequency of Each Character in a String
myStr = "Hello My name is Piyush Prajapati"
myStr = myStr.lower()          
myDict = {}

for ch in myStr:
    if ch not in myDict:
        myDict[ch] = myStr.count(ch)   

for key, value in myDict.items():
    print(f"{key} : {value}")
