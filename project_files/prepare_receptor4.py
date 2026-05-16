
#!/usr/bin/env python
#
#
#
# $Header: /opt/cvs/python/packages/mgltools/AutoDockTools/Utilities24/prepare_receptor4.py,v 1.25.2.1 2014/09/23 22:31:07 rhuey Exp $
#
import sys
import os.path
import time
# Removed: from string import *

from MolKit import Read, allAtoms
from MolKit.protein import Protein, Residue, Chain
from Pyscf import iofc


#to use prepare_receptor4.py from AutoDockTools, the following line
# is needed:
#from AutoDockTools.MoleculePreparation import AD4LigandPreparation
# but to use it as a stand alone script and not installed in AutoDockTools
# then the following line is needed:
from AutoDockTools.MoleculePreparation import ReceptorPreparation



if __name__ == '__main__':
    import sys
    import getopt


    def usage():
        """Print helpful message."""
        print('Usage: prepare_receptor4.py -r filename')
        print()
        print('    Description of command line arguments:')
        print('        [-r]    receptor filename      (required)')
        print('        [-o]    output filename        (default is receptor.pdbqt)')
        print('        [-A]    type of hydrogens to add (e.g. "all", "polar", "none")') # Fixed: using double quotes for inner examples
        print('                                 (default is "hydrogens")') # Fixed: using double quotes
        print('        [-U]    "unacceptor" policy    (e.g. "checkhydrogens", "noreplace")') # Fixed: using double quotes for inner examples
        print('                                 (default is "checkhydrogens")') # Fixed: using double quotes
        print('        [-C]    compute gasteiger charges (default is True)')
        print('        [-p]    preserve input charges (default is False)')
        print('        [-v]    verbose output         (default is False)')
        print('        [-e]    delete input filename  (default is False)')
        print('        [-N]    delete non-standard residues (default is False)')
        print('        [-M]    maximum number of residues (default is 1000)')
        print('        [-i]    ignore input filename errors (default is False)')
        print('        [-W]    warning message handling (e.g. "ignore", "warn", "error")') # Fixed: using double quotes for inner examples
        print('                                 (default is "warn")') # Fixed: using double quotes
        print('        [-s]    select chain             (default is None)')
        print('    Example: prepare_receptor4.py -r 1HPV.pdb -o 1HPV.pdbqt -A hydrogens -U nphs_lps')

    # process command line arguments
    try:
        opt_list, args = getopt.getopt(sys.argv[1:], 'r:o:A:U:C:p:v:e:N:M:i:W:s:')
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    # required parameters
    receptor_filename = None
    # optional parameters
    output_filename = "receptor.pdbqt"
    hydrogens_to_add = 'hydrogens'
    unacceptor_policy = 'checkhydrogens'
    compute_gasteiger_charges = True
    preserve_input_charges = False
    verbose = False
    delete_input_filename = False
    delete_non_standard_residues = False
    max_residues = 1000
    ignore_input_filename_errors = False
    warning_message_handling = 'warn'
    select_chain = None

    for o, a in opt_list:
        if o in ('-r', '--r'):
            receptor_filename = a
        if o in ('-o', '--o'):
            output_filename = a
        if o in ('-A', '--A'):
            hydrogens_to_add = a
        if o in ('-U', '--U'):
            unacceptor_policy = a
        if o in ('-C', '--C'):
            if a == 'False':
                compute_gasteiger_charges = False
            else:
                compute_gasteiger_charges = True
        if o in ('-p', '--p'):
            if a == 'True':
                preserve_input_charges = True
            else:
                preserve_input_charges = False
        if o in ('-v', '--v'):
            if a == 'True':
                verbose = True
            else:
                verbose = False
        if o in ('-e', '--e'):
            if a == 'True':
                delete_input_filename = True
            else:
                delete_input_filename = False
        if o in ('-N', '--N'):
            if a == 'True':
                delete_non_standard_residues = True
            else:
                delete_non_standard_residues = False
        if o in ('-M', '--M'):
            max_residues = int(a)
        if o in ('-i', '--i'):
            if a == 'True':
                ignore_input_filename_errors = True
            else:
                ignore_input_filename_errors = False
        if o in ('-W', '--W'):
            warning_message_handling = a
        if o in ('-s', '--s'):
            select_chain = a

    if not receptor_filename:
        print('prepare_receptor4.py: receptor filename must be specified.')
        usage()
        sys.exit()

    # now prepare the receptor
    RPO = ReceptorPreparation(receptor_filename, output_filename,
                            hydrogens_to_add, unacceptor_policy,
                            compute_gasteiger_charges, preserve_input_charges,
                            verbose, delete_input_filename,
                            delete_non_standard_residues, max_residues,
                            ignore_input_filename_errors, warning_message_handling,
                            select_chain)
