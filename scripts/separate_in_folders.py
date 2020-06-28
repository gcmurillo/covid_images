import pandas as pd
import os
import shutil

metadata = "../metadata.csv"

metadata_csv = pd.read_csv(metadata)
imageDir = "../images"
outputDir = "../../imagenes_clasificadas"

findings_CT = {}
findings_RX = {}

for (i, row) in metadata_csv.iterrows():
    filename = row["filename"].split(os.path.sep)[-1]
    filePath = os.path.sep.join([imageDir, filename])
    to = outputDir + "/" + row["modality"] + "/" + row["finding"]
    try:  
        if row["modality"] == 'X-ray':
            if row["finding"] not in findings_RX.keys() and (row["view"] == "PA" or row["view"] == "AP"):
                findings_RX[row["finding"]] = 1
                if not os.path.exists(to):
                    os.mkdir(to)
                shutil.copy(filePath, to)
                print(filename, 'OK')
            elif row["view"] == "PA" or row["view"] == "AP":
                findings_RX[row["finding"]] += 1
                if not os.path.exists(to):
                    os.mkdir(to)
                shutil.copy(filePath, to)
                print(filename, 'OK')
        else:
            if row["finding"] not in findings_CT.keys():
                findings_CT[row["finding"]] = 1
                if not os.path.exists(to):
                    os.mkdir(to)
                shutil.copy(filePath, to)
                print(filename, 'OK')
            else:
                findings_CT[row["finding"]] += 1
                if not os.path.exists(to):
                    os.mkdir(to)
                shutil.copy(filePath, to)
                print(filename, 'OK')
    except Exception as e:
        print(e)

print("CT: ", findings_CT)
print("RX: ", findings_RX)
report = open(outputDir + '/description.txt', 'w')
report.write("CT Images\n")
report.write("---------\n")
for i in findings_CT.keys():
    report.write(i + ": " + str(findings_CT[i]) + "\n")

report.write("\nRX Images\n")
report.write("---------\n")
for i in findings_RX.keys():
    report.write(i + ": " + str(findings_RX[i]) + "\n")
