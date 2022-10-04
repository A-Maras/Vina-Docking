from meeko import MoleculePreparation
from rdkit import Chem

#Prepare .pdbqt from .mol2
def pdbqt_prep(filename):
  mol = Chem.MolFromMol2File(str(filename) + '.mol2')
  preparator = MoleculePreparation(keep_nonpolar_hydrogens=True, double_bond_penalty=100, add_index_map=True) # macrocycles flexible by default since v0.3.0
  preparator.prepare(mol)
  preparator.show_setup()
  preparator.write_pdbqt_file(str(filename) + '.pdbqt')