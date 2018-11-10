class Rna(str):
    base_pairs = {'A': 'U', 'U': 'A',  'G': 'C', 'C': 'G', 'a': 'u', 'u': 'a',  'g': 'c', 'c': 'g'}

    def __init__(self):
        self.sequence = sequence
        for base in self.sequence:
            if base not in self.base_pairs:
                raise ValueError('RNA sequence can contain only A, U, G and C bases')

    def gc(self):
        return (self.count('G')+self.count('g')+self.count('C')+self.count('c')) / len(self) * 100

    def reverse_complement(self):
        complement = ''
        for base in self:
            complement += self.base_pairs[base]
        return complement[::-1]


class Dna(Rna):
    base_pairs = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'a': 't', 't': 'a', 'g': 'c', 'c': 'g'}

    def __init__(self):
        self.sequence = sequence
        for base in self.sequence:
            if base not in self.base_pairs:
                raise ValueError('DNA sequence can contain only A, T, G and C bases')

    def transcribe(self):
        dna_to_rna = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G', 'a': 'u', 't': 'a', 'g': 'c', 'c': 'g'}
        rna = ''
        for base in self:
            rna += dna_to_rna[base]
        return Rna(rna)
