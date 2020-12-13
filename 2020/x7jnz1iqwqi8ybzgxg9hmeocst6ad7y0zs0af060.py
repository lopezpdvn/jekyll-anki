decodict = 'AABCDEFGHIJKLMNOPQRSTUVWXYZ'

def f(s):
    yield from g(s, len(s))

def g(s, k):
    if not k:
        yield ''
        return

    if k == 1:
        enc = s[0]
        if enc != '0':
            c = decodict[int(enc)]
            yield c
            return

    enc = s[k-1]
    if enc != '0':
        c = decodict[int(enc)]
        for pre_decod in g(s, k-1):
            yield pre_decod + c

    enc = int(s[k-2:k])
    if 10 <= enc <= 26:
        c = decodict[enc]
        for pre_decod in g(s, k-2):
            yield pre_decod + c

assert (*f(''),   ) == (''   ,)
assert (*f('1'),  ) == ('A'  ,)
assert (*f('12'), ) == ('AB' , 'L')
assert (*f('226'),) == ('BBF', 'VF', 'BZ')
assert (*f('111'),) == ('AAA', 'KA', 'AK')
