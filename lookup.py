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
