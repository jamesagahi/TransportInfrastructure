import sys
import json
import ast




#areaPerRouteUser=0.9
#populationPerRouteUser=0.1
areaPerRouteUser=ast.literal_eval(sys.argv[1])
populationPerRouteUser=ast.literal_eval(sys.argv[2])
electrifiedScoreUser=ast.literal_eval(sys.argv[3])

print(1)




country=[]
areaPerRoute=[]
populationPerRoute=[]
electrified=[]
areaPerRouteScore=[]
populationPerRouteScore=[]
electrifiedScore=[]

# Read data file
data_file = open("rail_data.csv", "r")
data = data_file.readlines()

# Store each set of data in its appropriate list
for i in range(5, len(data)):
    values = data[i].split(",")
    country.append((values[0]))
    areaPerRoute.append(float(values[1]))
    populationPerRoute.append(float(values[2]))
    electrified.append(float(values[3]))

areaPerRouteMin=areaPerRoute[0]
areaPerRouteMax=areaPerRoute[0]
populationPerRouteMin=populationPerRoute[0]
populationPerRouteMax=populationPerRoute[0]
electrifiedMin=electrified[0]
electrifiedMax=electrified[0]

for i in range(1, len(country)):
    if areaPerRoute[i]<areaPerRouteMin:
        areaPerRouteMin=areaPerRoute[i]
    if areaPerRoute[i]>areaPerRouteMax:
        areaPerRouteMax=areaPerRoute[i]
    if populationPerRoute[i]<populationPerRouteMin:
        populationPerRouteMin=populationPerRoute[i]
    if populationPerRoute[i]>populationPerRouteMax:
        populationPerRouteMax=populationPerRoute[i]
    if electrified[i]<electrifiedMin:
        electrifiedMin=electrified[i]
    if electrified[i]>electrifiedMax:
        electrifiedMax=electrified[i]

for i in range(len(country)):
    areaPerRouteScore.append(1-(areaPerRoute[i]-areaPerRouteMin)/(areaPerRouteMax-areaPerRouteMin))
    populationPerRouteScore.append(1 - (populationPerRoute[i] - populationPerRouteMin) / (populationPerRouteMax - populationPerRouteMin))
    electrifiedScore.append(1-(electrified[i]-electrifiedMin)/(electrifiedMax-electrifiedMin))
    #print(areaPerRouteScore[i])
    #print(populationPerRouteScore[i])

countryScore=[]
countryData = []
for i in range(len(country)):
    score = (areaPerRouteScore[i]*areaPerRouteUser+populationPerRouteScore[i]*populationPerRouteUser+electrifiedScore[i]*electrifiedScoreUser)
    countryScore.append(score)
    countryData.append((country[i], score))


countryData.sort(key = lambda x: x[1])
countryData.reverse()
#print(countryData)
#for c in countryData:
    #print(c[0] + ": " + str(c[1]))


data_to_pass_back = countryData

output=input
output = data_to_pass_back
print(json.dumps(output))

sys.stdout.flush()