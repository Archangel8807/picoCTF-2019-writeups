import sys

d = {'11101110101000': 'z', '101110101000': 'l', '111010111000': 'k', '101011101000': 'f', '1010101000': 'h', '1010111000': 'u', '11101000': 'n', '10111000': 'a', '111011101000': 'g', '101010111000': 'v', '111010101000': 'b', '10101000': 's', '10111011101000': 'p', '101110111000': 'w', '11101011101000': 'c', '1110111010111000': 'q', '111000': 't', '1110111000': 'm', '1110101000': 'd', '11101110111000': 'o', '11101010111000': 'x', '1011101110111000': 'j', '1011101000': 'r', '1110101110111000': 'y', '101000': 'i', '1000': 'e', '0000': ' '}
buf = ""
# `xxd -b -c1 output | cut -d" " -f2 | tr -d "\n"`
secret = "100011101000111010111010001110111011100011101010001000111010100011101010001110101010001110111010111000111010111000101110111011100010111011101110001110100011101010100010101110100011101110101000"
while len(secret) > 0:
    buf += secret[0]
    secret = secret[1:]
    if buf in d:
        sys.stdout.write(d[buf])
        buf = ""

sys.stdout.write('\n')