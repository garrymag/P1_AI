###################################################
# Projeto 1 AI 2017/2018                          #
# IST                                             #
# PEDRO SILVA                                     #
# ANDRE BAIAO                                     #
###################################################

from myclass import *

def reader(file):

    pb = problem()

# Reads text file
    text = open(file,"r")
    for line in text:
        if line[0] == "V":
            pb.vertices.append(line)
        elif line[0] == "E":
            pb.edges.append(line)
        elif line[0] == "L":
            pb.launches.append(line)
    text.close()
    
    cleaner(pb)

    return pb

def cleaner(pb):
    
#cleans useless info from text file
    a = []
    b = []
    c = []
    
    
    for i in pb.vertices:
        a.append(i.split())
        
    for j in pb.edges:
        b.append(j.split())
        
    for k in pb.launches:
        c.append(k.split())

    for m in range(0,len(b)):
        b[m].pop(0)#pops "E"
    for n in range(0,len(c)):
        c[n].pop(0)#pops "L"
    
    pb.vertices = a
    pb.edges = b
    pb.launches = c
         
##debug
##def main():
##    pb = problem([],[],[])
##    file = input("file name: ")
##    reader(file,pb)
##    cleaner(pb)
##    return pb
