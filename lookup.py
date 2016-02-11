rna_codon_to_amino_acid = {\
'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',\
'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',\
'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',\
'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',\
'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',\
'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',\
'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',\
'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',\
'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',\
'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',\
'UAA':'Stop','CAA':'Q', 'AAA':'K', 'GAA':'E',\
'UAG':'Stop','CAG':'Q', 'AAG':'K', 'GAG':'E',\
'UGU':'C',   'CGU':'R', 'AGU':'S', 'GGU':'G',\
'UGC':'C',   'CGC':'R', 'AGC':'S', 'GGC':'G',\
'UGA':'Stop','CGA':'R', 'AGA':'R', 'GGA':'G',\
'UGG':'W',   'CGG':'R', 'AGG':'R', 'GGG':'G' \
}


amino_acid_to_rna_codon = {\
'A': ['GCG', 'GCA', 'GCU', 'GCC'],\
'C': ['UGC', 'UGU'],\
'D': ['GAU', 'GAC'],\
'E': ['GAG', 'GAA'],\
'F': ['UUU', 'UUC'],\
'G': ['GGA', 'GGU', 'GGG', 'GGC'],\
'H': ['CAC', 'CAU'],\
'I': ['AUC', 'AUA', 'AUU'],\
'K': ['AAA', 'AAG'],\
'L': ['UUG', 'CUA', 'CUC', 'CUU', 'UUA', 'CUG'],\
'M': ['AUG'],\
'N': ['AAC', 'AAU'],\
'P': ['CCU', 'CCC', 'CCA', 'CCG'],\
'Q': ['CAA', 'CAG'],\
'R': ['CGC', 'AGA', 'AGG', 'CGA', 'CGG', 'CGU'],\
'S': ['AGC', 'AGU', 'UCU', 'UCG', 'UCC', 'UCA'],\
'Stop': ['UAA', 'UAG', 'UGA'],\
'T': ['ACU', 'ACA', 'ACC', 'ACG'],\
'V': ['GUC', 'GUG', 'GUU', 'GUA'],\
'W': ['UGG'],\
'Y': ['UAU', 'UAC']\
}


# Masses in Daltons (Da = 1/12 mass of Carbon-12 molecule)
monoisotopic_mass = {\
'A':   71.03711,\
'C':   103.00919,\
'D':   115.02694,\
'E':   129.04259,\
'F':   147.06841,\
'G':   57.02146,\
'H':   137.05891,\
'I':   113.08406,\
'K':   128.09496,\
'L':   113.08406,\
'M':   131.04049,\
'N':   114.04293,\
'P':   97.05276,\
'Q':   128.05858,\
'R':   156.10111,\
'S':   87.03203,\
'T':   101.04768,\
'V':   99.06841,\
'W':   186.07931,\
'Y':   163.06333\
}

water_molecule_mass = 18.01056 # Da
