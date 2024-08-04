import base64

value = input("Input string for decoding: ")
ascii_s = ""

for i in range(0, len(value), 2):
    hex_pair = value[i:i+2]
    ascii_s += chr(int(hex_pair, 16))

reversed = ascii_s[::-1]
decoded = base64.b64decode(reversed)
print("Secret: "+decoded.decode())