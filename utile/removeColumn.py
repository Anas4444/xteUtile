import os, glob

def find_all(input_string, substring):
    indexes = []
    index = input_string.find(substring)
    while index != -1:
        indexes.append(index)
        index = input_string.find(substring, index + 1)
    return indexes

microservices = ["stocks"]
restricted = ["Authority", "User", "package-info"]
paths = ["D:\\Projects\\Xtensus\\"+microservice.capitalize()+"\\src\\main\\java\\com\\xtensus\\"+microservice+"\\domain" for microservice in microservices]
for path in paths:
    for filename in glob.glob(os.path.join(path, '*.java')):
        entity = filename.split('\\')[-1]
        if any(word in entity for word in restricted):
            continue
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            data = f.readlines()
            i = -1
            relationship = False
            for line in data:
                i += 1
                if "@Column" in line and "_" in line:
                    if ("_ar\"" in line):
                        index2 = line.find("_ar\"")
                        line = line[:index2+1] + "AR" + line[index2+3:]
                    elif ("_ht\"" in line):
                        index2 = line.find("_ht\"")
                        line = line[:index2+1] + "HT" + line[index2+3:]
                    elif ("_tva\"" in line):
                        index2 = line.find("_tva\"")
                        line = line[:index2+1] + "TVA" + line[index2+4:]
                    elif ("_ttc\"" in line):
                        index2 = line.find("_ttc\"")
                        line = line[:index2+1] + "TTC" + line[index2+4:]
                    indexs = find_all(line, "_")
                    for index in indexs:
                        line = line[:index] + line[index] + line[index+1].upper() + line[index+2:]
                    line = line.replace('_', '')
                    data[i] = line
                if "@ManyToOne" in line and "@JoinColumn" not in data[i+1]:
                    relationship = True
                if (relationship == True and "private" in line):
                    relationship = False
                    data.insert(i-1, f"    @JoinColumn(name=\"{line.split()[-1][:-1]}\", nullable=true)\n")

        with open(os.path.join(os.getcwd(), filename), 'w') as f:
            f.writelines(data)