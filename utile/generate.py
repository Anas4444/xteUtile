import os, glob

microservices = ["vehicule", "stocks", "personnel"]
paths = ["D:\\Projects\\Xtensus\\"+microservice.capitalize()+"\\src\\main\\java\\com\\xtensus\\"+microservice+"\\domain" for microservice in microservices]
for path in paths:
    for filename in glob.glob(os.path.join(path, '*.java')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            data = f.readlines()
            i = -1
            for line in data:
                i += 1
                if "OneToMany" not in line:
                    continue
                if ", fetch = FetchType.EAGER" in line:
                    continue
                index = line.find(')')
                data[i] = line[:index] + ", fetch = FetchType.EAGER" + line[index:]

        with open(os.path.join(os.getcwd(), filename), 'w') as f:
            f.writelines(data)