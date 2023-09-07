import os, glob

def find_all(input_string, substring):
    indexes = []
    index = input_string.find(substring)
    while index != -1:
        indexes.append(index)
        index = input_string.find(substring, index + 1)
    return indexes

microservices = ["vehicule", "stocks", "personnel"]
paths = ["D:\\Projects\\Xtensus\\"+microservice.capitalize()+"\\src\\main\\java\\com\\xtensus\\"+microservice+"\\domain" for microservice in microservices]
for path in paths:
    for filename in glob.glob(os.path.join(path, '*.java')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            data = f.readlines()
            i = -1
            for line in data:
                i += 1
                if "@Column" not in line:
                    continue
                if ("_ar\"" in line):
                    index2 = line.find("_ar\"")
                    line = line[:index2+1] + "AR" + line[index2+3:]
                indexs = find_all(line, "_")
                for index in indexs:
                    print(line[index])
                    line = line[:index] + line[index] + line[index+1].upper() + line[index+2:]
                line = line.replace('_', '')
                data[i] = line

        with open(os.path.join(os.getcwd(), filename), 'w') as f:
            f.writelines(data)