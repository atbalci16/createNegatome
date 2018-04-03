import os, sys, shutil
from subprocess import call

def main():
    if len(sys.argv) == 1:
        print "A pair list is required."
        return
    if len(sys.argv) >= 3:
        protein_path = sys.argv[2]
    if len(sys.argv) >= 4:
        dock_path = sys.argv[3]
    if len(sys.argv) == 5:
        preprocessed_path = sys.argv[4]
    if len(sys.argv) == 2:
        dock_path = "."
        protein_path = "."
        preprocessed_path = "."
    zdock_path = "zdock"
    print "Copying necessary files to protein directory..."
    if protein_path != ".":
        shutil.copy2(os.path.join(zdock_path, "mark_sur"), os.path.join(protein_path, "mark_sur"))
        shutil.copy2(os.path.join(zdock_path, "uniCHARMM"), os.path.join(protein_path, "uniCHARMM"))
    
    proteins = os.listdir(protein_path)
    proteins = filter(lambda x: x[len(x)-3:] == "pdb", proteins)
    command =  "./mark_sur"
    line = [command, "-", "-"]
    extension = ".pdb"
    old_path = os.getcwd()
    os.path.isdir(preprocessed_path) or os.mkdir(preprocessed_path)
    os.chdir(protein_path)

    print "Preprocessing PDB files..."
    for i in proteins:
        line[1] = i
        print line[1]
        line[2] = os.path.join("..", os.path.join(preprocessed_path, i[:len(i)-4] + "_m" + extension))
        print line[2]
        call(line)
    os.chdir(old_path)

    os.path.isdir(dock_path) or os.mkdir(dock_path)
    
    with open(sys.argv[1]) as file:
        pairs = file.readlines()
    pairs = [tuple(i.split()) for i in pairs]
    command = "zdock/zdock"
    line = [command, "-R", "-", "-L", "-", "-o", "-"]
    print "Creating docking files..."
    for (r, l) in pairs:
        line[2] = os.path.join(preprocessed_path, r+"_m"+extension)
        line[4] = os.path.join(preprocessed_path, l+"_m"+extension)
        line[6] = os.path.join(dock_path, r+"_"+l+".out")
        call(line)
    print "Done"

main()
