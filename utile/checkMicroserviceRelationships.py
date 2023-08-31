import os, glob, json
from json import JSONEncoder
import pandas as pd

microservices = dict()
path = "D:\\Projects\\Xtensus\\xteUtile\\JDLConfiguration"
data = dict()
for filename in glob.glob(os.path.join(path, '*.jdl')):
    startIndex = filename.rfind('\\')+1
    endIndex = filename.rfind('Config')
    microservices[filename[startIndex:endIndex].lower()] = dict()
    microservices[filename[startIndex:endIndex].lower()]["entities"] = dict()
    with open(os.path.join(os.getcwd(), filename), 'r') as file:
        data = file.readlines()
        microservices[filename[startIndex:endIndex].lower()]["data"] = data
        for line in data:
            if ("paginate" in line):
                entityIndexStart = line.find(next(filter(str.isupper, line), ''))
                entityIndexEnd = line.find("with")-1
                microservices[filename[startIndex:endIndex].lower()]["entities"][line[entityIndexStart:entityIndexEnd].strip()] = set()

for microservice in microservices.keys():
    newEntity = False
    entityName = ""
    for line in microservices[microservice]["data"]:
        if ("entity" in line):
            newEntity = True
            entityName = line[line.find(next(filter(str.isupper, line), '')):line.find("{")-1].strip()
            #print("Found New Entity :", entityName)
            continue
        if ("}" in line):
            newEntity = False
            entityName = ""
        if (newEntity==True):
            for entity in microservices[microservice]["entities"].keys():
                if (entity==entityName):
                    for otherMicroservice in microservices.keys():
                        if (otherMicroservice == microservice):
                            continue
                        if (otherMicroservice in line):
                            index = -1
                            b = False
                            for c in line:
                                index+=1
                                if (c.isalpha()):
                                    b = True
                                if (c==' ' and b == True):
                                    break
                            microservices[microservice]["entities"][entity].add(line[:index].strip())
                    break
    del microservices[microservice]["data"]

class setEncoder(JSONEncoder):
    def default(self, obj):
        return list(obj)

with open("microservices.json", "w") as outfile:
    json.dump(microservices, outfile, cls=setEncoder)

with open("microservices.json", "r") as f:
    json_data = json.load(f)

df = pd.DataFrame.from_dict(json_data)
df.to_csv("microservices.csv", index=False)