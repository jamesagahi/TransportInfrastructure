country=[]
areaPerRoute=[]
populationPerRoute=[]
areaPerRouteScore=[]
populationPerRouteScore=[]

# Read data file
data_file = open("rail_data.csv", "r")
data = data_file.readlines()

# Store each set of data in its appropriate list
for i in range(5, len(data)):
    values = data[i].split(",")
    country.append((values[0]))
    areaPerRoute.append(float(values[1]))
    populationPerRoute.append(float(values[2]))

areaPerRouteMin=areaPerRoute[0]
areaPerRouteMax=areaPerRoute[0]
populationPerRouteMin=populationPerRoute[0]
populationPerRouteMax=populationPerRoute[0]

for i in range(1, len(country)):
    if areaPerRoute[i]<areaPerRouteMin:
        areaPerRouteMin=areaPerRoute[i]
    if areaPerRoute[i]>areaPerRouteMax:
        areaPerRouteMax=areaPerRoute[i]
    if populationPerRoute[i]<populationPerRouteMin:
        populationPerRouteMin=populationPerRoute[i]
    if populationPerRoute[i]>populationPerRouteMax:
        populationPerRouteMax=populationPerRoute[i]

for i in range(len(country)):
    areaPerRouteScore.append(1-(areaPerRoute[i]-areaPerRouteMin)/(areaPerRouteMax-areaPerRouteMin))
    populationPerRouteScore.append(1 - (populationPerRoute[i] - populationPerRouteMin) / (populationPerRouteMax - populationPerRouteMin))
    #print(areaPerRouteScore[i])
    #print(populationPerRouteScore[i])

areaPerRouteUser=0.9
populationPerRouteUser=0.1

countryScore=[]
countryData = []
for i in range(len(country)):
    score = (areaPerRouteScore[i]*areaPerRouteUser+populationPerRouteScore[i]*populationPerRouteUser)
    countryScore.append(score)
    countryData.append((country[i], score))


countryData.sort(key = lambda x: x[1])
countryData.reverse()
#print(countryData)
for c in countryData:
    print(c[0] + ": " + str(c[1]))



