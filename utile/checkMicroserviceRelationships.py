import os, glob

microservices = dict()
path = "D:\\Projects\\Xtensus\\xteUtile\\JDLConfiguration"
for filename in glob.glob(os.path.join(path, '*.jdl')):
    startIndex = filename.rfind('\\')+1
    endIndex = filename.rfind('Config')
    microservices[filename[startIndex:endIndex].lower()] = dict()
    with open(os.path.join(os.getcwd(), filename), 'r') as file:
        data = file.readlines()
        for line in data:
            if ("paginate" in line):
                entityIndexStart = line.find(next(filter(str.isupper, line), ''))
                entityIndexEnd = line.find("with")-1
                microservices[filename[startIndex:endIndex].lower()][line[entityIndexStart:entityIndexEnd]] = set()
print(microservices)