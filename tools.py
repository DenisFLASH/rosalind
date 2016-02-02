import re
import urllib.request



def read_lines(path):
    lines = []
    with open(path, 'r') as in_file:
        for line in in_file:
            lines.append(line.strip())
    return lines



def read_fasta_file(path):
    """
    Read FASTA file given its path.
    
    Args:
        + path (str): path to a FASTA file, either local or URL
    """
    if path.starswith('http://'):
        req = urllib.request.Request(path, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = str(response.read())
        #lines = 
    
    lines = read_lines(path)
    return parse_fasta_lines(lines)



def parse_fasta_lines(lines):
    """
    Parse lines of FASTA file.
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
        + lines (list of str): lines representing content of a file
        
    Returns:
        + dictionary {str: str}:
            key:   taxon name,
            value: taxon genetic string
    """
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



    
# TODO deprecated
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



def punnett_square(factor1, factor2):
    """
    Args:
        + factor1,2 (str): 2 characters string representing a factor composed of 2 alleles
    Returns:
        {str: float} dict : probabilities of each possible outcome of mating process
    """
    outcome_probs = {}
    for allele_f1 in factor1:
        for allele_f2 in factor2:
            outcome = ''.join(sorted([allele_f1, allele_f2]))
            if outcome in outcome_probs:
                outcome_probs[outcome] += 1
            else:
                outcome_probs[outcome] = 1
    # Normalizing to obtain total probability equal 1
    for outcome in outcome_probs:
        outcome_probs[outcome] /= 4
    return outcome_probs



def find_indices_of_matches(s, t):
    """
    Find all appearances of a substirng in a string.
    
    Args:
        + s (str): initial string
        + t (str): substring to look for in the initial string
       
    Returns:
        + (list of int): list of starting positions of subsring in the initial string 
        
    Note:
        Overlap is allowed when matching the substring.
    """
    starting_positions = list()
    # regex pattern including lookahead assertion (?=...)
    pattern = r'(?=({0})).'.format(t)
    matches = re.finditer(pattern, s)
    for match in matches:
        # Add 1 to get 1-based positions
        #print(match.start() + 1, match.group(1), end=', ')
        starting_positions.append(match.start() + 1)
    return starting_positions
