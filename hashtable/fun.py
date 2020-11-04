def fnv1(key):
    """
    FNV-1 Hash, 64-bit
    - start hash at some large number (FNV_offset_basis)
    - the hashed variable maintains our total
    """
    FNV_offset_basis = 14695981039346656037
    FNV_prime = 1099511628211
    hashed = FNV_offset_basis
    bytes_to_hash = key.encode()
    for byte in bytes_to_hash:
        hashed = hashed * FNV_prime
        hashed = hashed ^ byte
    return hashed

print('-----FNV1-----')
print(fnv1("dad"))
print(fnv1("add"))

def djb2(key):
    """
    DJB2 hash, 32-bit
    why 5381 and * 33? they just work! nobody knows why...
    What's work? what makes these good?
    - irreversible
    - distributed evenly throughout a modulo operation
    - (which spreads them out over an array & minimizes collisions)
    """
    hashed = 5381
    bytes_to_hash = key.encode()
    for byte in bytes_to_hash:
        # the '<<' shifts the bytes to the left by 5
        #hashed = ((hashed << 5) + byte)
        hashed = ((hashed * 33) + byte)   
    return hashed

print('-----DJB2-----')
print(djb2("dad"))
print(djb2("add"))