from webbrowser import get
from valoffdoa import getAllValuations

data = getAllValuations() 

totalArea = 0

for entry in data:
    valuationReports = entry["ValuationReport"]
    #print(valuationReports)
    for valuationReport in valuationReports:
       # print(valuationReport)
        if valuationReport["FloorUse"] == "STORE":
            print((valuationReport)["Area"],"+", totalArea, "=", end="")
            totalArea += valuationReport["Area"]
            print(totalArea)


print(totalArea)