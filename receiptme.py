import re

receiptName = "fredMeyers"

inputreader = open(receiptName + "receipt.txt", "r").readlines()

ryanTotal = 0
ryanItems = 0
tristanTotal = 0
tristanItems = 0
collinTotal = 0
collinItems = 0
tadTotal = 0
tadItems = 0

theTotal = 0
totalItems = 0

outputReader = open(receiptName + "output.txt", "w")

for entry in inputreader:
    entry.replace("\n", "")
    amountF = re.split(" ", entry)
    if len(amountF) < 2:
        continue
    amount = float(amountF[0])
    theTotal += amount
    totalItems += 1
    splAmt = float(len(amountF)) - 1

    for person in amountF[1:]:
        if "ry" in person:
            ryanTotal += amount/splAmt
            ryanItems += 1
        if "tr" in person:
            tristanTotal += amount/splAmt
            tristanItems += 1
        if "td" in person:
            tadTotal += amount/splAmt
            tadItems += 1
        if "co" in person:
            collinTotal += amount/splAmt
            collinItems += 1
    outputReader.write(entry + "( " + str(splAmt) + " people )-")
    outputReader.write("Ryan SubTotal: " + str(round(ryanTotal, 2)) + " Tristan SubTotal: " + str(round(tristanTotal, 2)) + " Collin SubTotal: " + str(round(collinTotal, 2)) + " Tad SubTotal: " + str(round(tadTotal, 2)) + "\n\n")
print ("Ryan Total:", round(ryanTotal, 2), "- Items:", ryanItems)
print ("Tristan Total:", round(tristanTotal, 2), "- Items:", tristanItems)
print ("Collin Total:", round(collinTotal, 2), "- Items:", collinItems)
print ("Tad Total:", round(tadTotal, 2), "- Items:", tadItems)
print ("Total:", round(ryanTotal + tristanTotal + collinTotal + tadTotal, 2))
print ("Number of Items:", totalItems)
print ("Unsplit Total:", round(theTotal, 2))
