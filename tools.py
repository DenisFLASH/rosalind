def read_lines(path):
    lines = []
    with open(path, 'r') as in_file:
        for line in in_file:
            lines.append(line.strip())
    return lines


def parse_fasta_file(path):
    """
    A file in FASTA format (.fas, .fasta) applies the following sample notation to store genetic strings:

    Example:

    >Taxon1
    CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
    TCCCACTAATAATTCTGAGG
    >Taxon2
    CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
    ATATCCATTTGTCAGCAGACACGC
    >Taxon3
    CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
    TGGGAACCTGCGGGCAGTAGGTGGAAT

    Every string in a FASTA file begins with a single-line that contains the symbol '>' 
    along with some labeling information about the string. 
    The word following the '>' symbol is the identifier of the sequence, 
    and the rest of the line is its description (both are optional). 
    There should be no space between the ">" and the first letter of the identifier.

    All subsequent lines contain the string itself; 
    it is recommended that all lines of text are shorter than 80 symbols. 
    The string ends when another line starting with '>' appears, 
    indicating the start of another sequence (or if the end of the file is reached).
    
    
    Args:
        + path (str): path to an input file
        
    Returns:
        + dictionary {str: str}:
            key:   taxon name,
            value: taxon genetic string
    """
    lines = read_lines(path)
    d = {}
    current_taxon = None
    for line in lines:
        # If it is a taxon title line, create an entry in the dictionary and set this taxon to be the current key
        if line.startswith('>'):
            taxon_name = line.strip('>')
            if taxon_name in d:
                raise Exception("Taxon {0} found more than once in a file!".format(taxon_name))
            else:
                d[taxon_name] = ''
                current_taxon = taxon_name
        # If it is a line containing part of a genetic string, add this line to the current taxon's entry (concatenate)
        else:
            d[current_taxon] += line
    return d