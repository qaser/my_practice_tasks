def duplicate_encode(word):
    #your code here
    list_str = list(word.lower())
    new_str = []
    count = {}
    for i in list_str:
        count[i] = count.get(i, 0) + 1
    for j in list_str:
        if count[j] > 1:
            symbol = ')'
        else:
            symbol = '('
        new_str.append(symbol)
    return ''.join([')' if word.lower().count(c) == 1 else '(' for c in word.lower()])

print(duplicate_encode('qWsese'))


def DNA_strand(dna):
    # code here
    symbols = {
               'A': 'T',
               'T': 'A',
               'C': 'G',
               'G': 'C'
              }
    
    return ''.join([symbols[i] for i in dna if i in symbols])

print(DNA_strand("ATTGC"))