from vina import Vina
import os
from datetime import datetime


def create_dir(directory):
    if not os.path.exists(directory):
        print('Creating Directory ' + directory)
        os.makedirs(directory)


def vina_dock(receptor_file, ligand_file, grid_coord, grid_size):
    # Create output folder for the energy minimization and docking files, plus the poses binding affinity
    creation_time = datetime.now()
    create_dir('outputs/' + str(creation_time))

    v = Vina(sf_name='vina')

    #v.set_receptor(rigid_pdbqt_filename='receptors/' + str(receptor_file) + '.pdbqt', flex_pdbqt_filename='test.pdbqt')
    v.set_receptor('receptors/' + str(receptor_file) + '.pdbqt')
    v.set_ligand_from_file('ligands/' + str(ligand_file) + '.pdbqt')

    # Compute vina maps
    v.compute_vina_maps(center=grid_coord, box_size=grid_size)
    #elif maps == 'testcase_1iep':
        #v.compute_vina_maps(center=[15.190, 53.903, 16.917], box_size=[20, 20, 20])
   # elif maps == 'testcase_1fpu':
      #  v.compute_vina_maps(center=[12.201, 54.303, 15.54], box_size=[30, 38, 22])
    #elif maps == 'arylomycin':  #4.116,-7.565,4.912 - used for docking Arylomycin A2 30, 30, 30 size
       # v.compute_vina_maps(center=[4.116,-7.565,4.912],
                           # box_size=[30, 30, 30])
    #else:
        #print('unknown map profile: enter "default" or "testcase"')

    # Score the current pose
    energy = v.score()
    print('Score before minimization: %.3f (kcal/mol)' % energy[0])

    # Create output folder for the energy minimization and docking files

    # Minimized locally the current pose
    energy_minimized = v.optimize()
    print('Score after minimization : %.3f (kcal/mol)' % energy_minimized[0])
    v.write_pose('outputs/' + str(creation_time) + '/' + str(receptor_file) +
                 '_' + str(ligand_file) + '_vina_minimized.pdbqt',
                 overwrite=True)

    # Dock the ligand
    v.dock(exhaustiveness=36, n_poses=20)
    v.write_poses('outputs/' + str(creation_time) + '/' + str(receptor_file) +
                  '_' + str(ligand_file) + '_vina.pdbqt',
                  n_poses=20,
                  overwrite=True)
