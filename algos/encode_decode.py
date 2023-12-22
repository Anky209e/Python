
def encode(strs):
    encoded_str = ""
    for info in strs:
        encoded_str += str(len(info)) + "#" + info
    return encoded_str

def decode(encoded_str):
    result,i = [],0

    while i < len(encoded_str):
        j = i

        while encoded_str[j] != "#":
            j+=1
        info_len = int(encoded_str[i:j])
        info = encoded_str[j+1:j+1+info_len]
        result.append(info)
        i = j + 1 + info_len
    
    return result


strs =  ["we", "say", ":", "yes"]
encoded_str = encode(strs)
print(encoded_str)

decoded_str = decode(encoded_str)
print(decoded_str)