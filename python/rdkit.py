# remember to activate an environment
# and then EXECUTE THE PYTHON EXE IN THAT DIRECTORY
# ~/Miniconda/envs/chem/python.exe or something

from rdkit import Chem

smiles = ["CS(N1CCC(CC1)Nc1cc(c2ccc(C(N)=O)c(c2)OCC2CC2)[nH]n1)(=O)=O",
"CC1CC1COc1cc(ccc1C(N)=O)c1cc(NC2CCN(CC2)S(C)(=O)=O)n[nH]1",
"CS(N1CCC(CC1)Nc1cc(c2ccc(C#N)c(c2)OCC2CC2)[nH]n1)(=O)=O",]

#19,21,22,23,27,30,31,32,33

smiles2 = ["C12=NC=C(C3=CN(C(C4=CC(C)=CC=C4)C4=CC=CN=C4)N=C3)N=C1C=C(N(C1=CC(OC)=CC(OC)=C1)CCO)C=C2",
"C1=CC=C(F)C2=C1NC(=O)C(C1=NC3=C(N1)C=C(N1CCN(C)CC1)C=C3)=C2N",
"C1(NC2=CC(C3=CC=CO3)=NN2)=CC(N2CCN(C3=CC=CC=C3)CC2)=NC(N2C[C@@H](C3=CC=CC=C3)C[C@H](C(NC)=O)C2)=N1",
"C1CN(C2=NC3=C(C=C2)NN=C3C2=CN(C)N=C2)CC2=C(C(F)(F)F)N=CN12",
"C1(N[C@H](C2=NC=CC=N2)C)=C(C2=NC3=C(N=C(N4C[C@H](C)O[C@H](C)C4)C=C3C)N2)C(=O)NC2=CN(C)N=C12",
"ClC1=C(C2=CC3=C(C=C2)N=C(N[C@H]2[C@@H](NC(CC)=O)CCOC2)N=C3)C(Cl)=C(OC)C=C1OC",
"C1(C2=CN3C(=C(C4=C(F)C(C)=CC(C(NC)=O)=C4)C=N3)N=C2O[C@H]2COCC2)=CN(C2CCN(C(CC)=O)CC2)N=C1",
"N12C(=NS(=O)(=O)CC1)C(C(=O)NC1=C(OC3=CC=CC=C3Cl)C=NC=C1)=CC=C2",
"N12C(=NC=C1C1=C(F)C(C(F)F)=CC(C(NC)=O)=C1)C=C(C1=CC(C#N)=C(C)C=C1)C(O[C@@H]1COCC1)=N2"]

for s in smiles2:
    m = Chem.MolFromSmiles(s)
    i = Chem.inchi.MolToInchiKey(m)
    print(i)