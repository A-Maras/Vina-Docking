from meeko import MoleculePreparation
from rdkit import Chem

#Prepare .pdbqt from .mol2
def pdbqt_prep(filename):
  mol = Chem.MolFromMol2File((str(filename) + '.mol2'))
  #mol = Chem.MolFromPDBFile((str(filename) + '.pdb'))
  #mol = Chem.MolFromMolFile((str(filename) + '.mol'))
  preparator = MoleculePreparation() # macrocycles flexible by default since v0.3.0
  preparator.prepare(mol)
  preparator.show_setup()
  preparator.write_pdbqt_file(str(filename) + '.pdbqt')