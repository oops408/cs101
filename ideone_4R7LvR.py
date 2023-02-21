import base64

AKEY = 'rpa-creds'  # AES key must be either 16, 24, or 32 bytes long


def encode(key, clear):
    """
    Encode username and passwords using the key available.
    :param key:
    :param clear:
    :return:
    """
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = (ord(clear[i]) + ord(key_c)) % 256
        enc.append(enc_c)
    return base64.urlsafe_b64encode(bytes(enc))


def decode(key, enc):
    """
    Decode encrypted username and password values.
    :param key:
    :param enc:
    :return:
    """
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + enc[i] - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


val1 = encode("rpa-creds", "wuMSZB92vFk7WxlJc2bThJ9Wbaga")
print(val1)
val2 = decode("rpa-creds", "o-HCp4a3qac=")
# print(val2)
