import meeko_prep
import autodock_vina
import pdb_coord_parse

# Meeko: Preparation of pdbqt files, mainly for ligands
#meeko_prep.pdbqt_prep('sti571')
#mk_prepare_ligand.py -i 1t7d_lig_corrected.sdf -o 1t7d_lig_corrected.pdbqt

# Autodock Vina: Molecular Docking
#autodock_vina.vina_dock('1b12','BAL4850C','default')
#autodock_vina.vina_dock('4wvg','ok-150','default')
#autodock_vina.vina_dock('1kn9','arylomycin_backbone','arylomycin')

#autodock_vina.vina_dock('4WVJ_spsb','pk150_4wvj', [91.121, 3.153, 14.254], [30, 30, 30])
#autodock_vina.vina_dock('4WVI_spsb','pk150_4wvi', [25.574, -0.828, 13.888], [30, 30, 30])
#autodock_vina.vina_dock('4WVH_spsb','pk150_4wvh', [-24.827, 0.815, -10.751], [30, 30, 30])
#autodock_vina.vina_dock('4WVG_spsb','pk150_4wvg', [16.604, 40.407, 99.395], [30, 30, 30])
#autodock_vina.vina_dock('4WVJ_spsb','sorafenib_4wvj', [91.121, 3.153, 14.254], [30, 30, 30])

#autodock_vina.vina_dock('2hzn','NVP-AFG210', [47.491, 24.873, 41.37 ], [26, 36, 26])
#autodock_vina.vina_dock('3qrk','dp987', [19.484, 22.996, 10.682], [32, 28, 30])
#autodock_vina.vina_dock('4jxw','4jxw_ligand_pubchem', [22.7, 3.764, 13.54], [30, 30, 30])
#autodock_vina.vina_dock('1t7d','1t7d_lig_corrected', [-1.003, 49.626, 8.25], [26, 52, 26])

# PDB Coordinate Parsing
#pdb = pdb_coord_parse.parsePDB('1ZG4.pdb')
#dict = pdb_coord_parse.parse_dict(pdb[1], 70)
#print(dict)