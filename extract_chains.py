import os, sys

def main():
    
    with open(sys.argv[1]) as file:
        proteins = file.readlines()
    proteins = [i.split() for i in proteins]
    flatted_proteins = []
    
    for i in proteins:
        flatted_proteins += i
    
    proteins = list(set(flatted_proteins))
    print proteins
    os.path.isdir(sys.argv[3]) or os.mkdir(sys.argv[3])

    pdb = []
    
    print "Extracting Chains..."
    
    for i in proteins:
        
        chain = i[len(i)-1]
        pdbname = i[:4]+".pdb"
        
        with open(os.path.join(sys.argv[2], pdbname)) as file:
            pdb = file.readlines()
        
        pdb = filter(lambda x: x[:4] == "ATOM", pdb)
        pdb =filter(lambda x: x[21:22].strip() == chain, pdb)
        
        with open(os.path.join(sys.argv[3], i+".pdb"), "w") as file:
            for l in pdb:
                file.write(l)

    print "Done"

main()
