# Generating substrings of a string with variable sized holes. 
# Unoptimized

D = ['cow' ,'com','boo', 'soo', 'coo', 'co', 'so', 'cobo', 'show', 'boshow', 'bow', 'mow', 'cobomshow']
D.extend(list('cobomshow'))
_cache = {}

def findallsubstrs(S,L):
    # memoize this since this inner loop is called 
    # multiple times
    if (S,L) in _cache:
        return _cache[(S,L)]
    substrs = []
    for i in range(len(S)-L+1):
        substr = S[i:i+L]
        substrs.append(substr)
    _cache[(S,L)] = substrs
    return substrs


def findsubstrs(S,L,D):
    print 'String: %s' % S
    print 'Length: %d'  % L
    print 'Dictionary: %s' % D  

    if L > len(S):
        return []
    # for 0 sized holes
    substrs = set([x for x in findallsubstrs(S,L) if x in D]) 
    n = len(S) + 1
    holesizemin = 1
    holesizemax = n - L
    for holesize in range(holesizemin, holesizemax):
        for holepos in range(0,n):
            validsubstr = ''.join([S[0:holepos],S[holepos+holesize:]])
            for substr in findallsubstrs(validsubstr,L):
                if substr in D:
                    if substr not in substrs:
                        substrs.add(substr)
    return list(substrs)
     


for L in (4,3,6,9,1):
    print '='*80
    print "Output :%s" % findsubstrs('cobomshow', L , D)
