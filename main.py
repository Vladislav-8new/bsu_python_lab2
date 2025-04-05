import glob

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction as GC

def gc_ratio(filename):
    with open(filename) as handle:
        records_dict = {}
        for record in SeqIO.parse(handle, "fasta"):
            dna = record.seq
            gc_percentage = GC(dna)
            records_dict[record.id] = round(gc_percentage, 6)
    return records_dict


if __name__ == '__main__':
    fasta_files_list = glob.glob("*.fasta")
    all_sequences_ratio = {}

    for file in fasta_files_list:
        seq = gc_ratio(file)
        all_sequences_ratio.update(seq)

    max_ratio = max(all_sequences_ratio.values())

    for key, value in all_sequences_ratio.items():
        if value == max_ratio:
            print(f"{key}\n{value}")