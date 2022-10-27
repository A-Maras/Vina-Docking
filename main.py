import meeko_prep
import autodock_vina
import pdb_coord_parse

# Meeko: Preparation of pdbqt files, mainly for ligands
#meeko_prep.pdbqt_prep('sti571')


# Autodock Vina: Molecular Docking
#autodock_vina.vina_dock('1b12','BAL4850C','default')
#autodock_vina.vina_dock('4wvg','ok-150','default')
#autodock_vina.vina_dock('1kn9','arylomycin_backbone','arylomycin')
#autodock_vina.vina_dock('1b12_chainA','penem_cleaned','default')

# PDB Coordinate Parsing
#pdb = pdb_coord_parse.parsePDB('1ZG4.pdb')
#dict = pdb_coord_parse.parse_dict(pdb[1], 70)
#print(dict)