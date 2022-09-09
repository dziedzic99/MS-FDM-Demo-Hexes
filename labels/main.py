import csv
# from cairosvg import svg2png
import subprocess

startfrom = 30


def dostuff():
    with open('file.csv', mode='r') as infile:
        reader = csv.reader(infile)
        parentnum = 0
        num = 0
        numlist = []
        for i in range(startfrom):
            next(reader)
        for person in reader:
            num += 1
            print("Robię teraz", person[0])
            with open('template.svg', 'r') as template:
                svg = template.read()
                svg=svg.replace("TITLE", person[1])
                svg=svg.replace("SUBT", person[2])
                svg=svg.replace("HH:MM", person[3])
                svg=svg.replace("LH", person[4])
                svg=svg.replace("IPER", person[5])
                svg=svg.replace("MASS", person[6])
                svg=svg.replace("ND", person[7])
                svg=svg.replace("IPAT", person[8])
                svg=svg.replace("DESIGNATION", person[0])


            with open("results/"+str(person[0])+".svg",'w') as resultfile:
                resultfile.write(svg)
                # svg2png(bytestring=svg,write_to="results/"+str(person[0])+".png")
            subprocess.run(["inkscape","results/"+str(person[0])+".svg","-d","1200","-o","results/pngs/"+str(person[0])+".png"])
            numlist.append("results/pngs/"+str(person[0])+".png")
            if num == 4:
                subprocess.run(["convert","-append"]+numlist+["results/printables/"+str(parentnum)+".png"])
                parentnum += 1
                num = 0
                numlist = []



dostuff()
