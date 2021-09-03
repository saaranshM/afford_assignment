def compress(data):
    
    sdict = {}
    for i in data:
        if i in sdict.keys():
            sdict[i] += 1
        else:
            sdict[i] = 1

    compressed = ""
    for key, value in sdict.items():
        compressed += str(key) + str(value)

    return compressed

def decompress(data):
    uncompressed_string = ""
    split_string = [data[i:i+2] for i in range(0, len(data), 2)]

    for i in split_string:
        uncompressed_string += i[0] * int(i[1])
    
    return uncompressed_string

string_to_compress = "aaaaaaabbbbbbccccccABBBXXXXSSSS"
print("String to compress is: ", string_to_compress)

compressed = compress(string_to_compress)
print("Compressed: "  + compressed )

decompressed = decompress(compressed)
print("Decompressed: " + decompressed)