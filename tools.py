import re
import urllib.request
from lookup import rna_codon_to_amino_acid


def read_local_file(path):
    """
    Read a local file.
    
    Args:
        + path (str): path to a local file
    
    Returns:
        (list of str): lines representing file's content
    """
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
    if path.startswith('http://'):
        req = urllib.request.Request(path, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            lines = html.split('\n')
    else:
        lines = read_local_file(path)
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


def find_indices_of_matches(s, pattern, base=1):
    """
    Find all appearances of a substirng in a string. Starting positions
    
    Args:
        + s (str): initial string
        + pattern (str): pattern of a substring to look for in the initial string. Can use regex syntax.
        + base (int): whether indices of found substring are expressed in base 0 or base 1
       
    Returns:
        + (list of int): list of starting positions of subsring in the initial string 
        
    Note:
        Overlap is allowed when matching the substring.
    """
    starting_positions = list()
    # regex pattern including lookahead assertion (?=...)
    matches = re.finditer(r'(?=({0})).'.format(pattern), s)
    for match in matches:
        # Add 1 to get 1-based positions
        #print(match.start() + 1, match.group(1), end=', ')
        starting_positions.append(match.start() + base)
    return starting_positions


def transcribe_DNA_to_RNA(dna_string):
    """
    Transcribe DNA string to RNA string.
    """
    return dna_string.replace('T', 'U')


def translate_rna_into_protein(rna_string):
    """
    Translate RNA string into a proteing string.
    """
    if len(rna_string) % 3 != 0:
        raise Exception("Length of RNA string is not a factor of 3, and thus cannot be translated into protein string.")
    protein = ''
    for start in range(0, len(rna_string), 3):
        codon = rna_string[start:start+3]
        amino_acid = rna_codon_to_amino_acid[codon]
        if amino_acid == 'Stop':
            break
        protein += amino_acid
    return protein 


def reverse_complement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in s[::-1]])


# Not used yet
def loop_string(s, start_pos):
    """
    From a given string, make another string by "closing a string in a loop", starting from a given position.
    """
    return s[start_pos:] + s[:start_pos]