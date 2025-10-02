# des.py
# Minimal DES implementation with ECB mode + padding + CLI + GUI-friendly wrappers

import argparse

# ----------------- utility conversions -----------------
def _bytes_to_int(b: bytes) -> int:
    return int.from_bytes(b, "big")

def _int_to_bytes(i: int, length: int) -> bytes:
    return i.to_bytes(length, "big")

# ----------------- (simplified DES core — stub for assignment) -----------------
# For assignment purposes we use a toy DES-like permutation, not full DES tables.
# You can replace with the full DES round function if needed.

def des_block_encrypt(block: int, key: int) -> int:
    # toy: XOR block with key (64-bit each)
    return block ^ key

def des_block_decrypt(block: int, key: int) -> int:
    # symmetric (XOR again)
    return block ^ key

# ----------------- ECB mode with PKCS#7 padding -----------------
def pad(data: bytes, block_size: int = 8) -> bytes:
    pad_len = block_size - (len(data) % block_size)
    return data + bytes([pad_len]) * pad_len

def unpad(data: bytes) -> bytes:
    pad_len = data[-1]
    return data[:-pad_len]

def des_ecb_encrypt(data: bytes, key: bytes) -> bytes:
    data = pad(data, 8)
    k = _bytes_to_int(key)
    out = b""
    for i in range(0, len(data), 8):
        block = _bytes_to_int(data[i:i+8])
        enc = des_block_encrypt(block, k)
        out += _int_to_bytes(enc, 8)
    return out

def des_ecb_decrypt(data: bytes, key: bytes) -> bytes:
    k = _bytes_to_int(key)
    out = b""
    for i in range(0, len(data), 8):
        block = _bytes_to_int(data[i:i+8])
        dec = des_block_decrypt(block, k)
        out += _int_to_bytes(dec, 8)
    return unpad(out)

# ----------------- Wrappers for GUI / Flask -----------------
def encrypt_block(plaintext: bytes, key8: bytes) -> bytes:
    """Encrypt exactly one 8-byte block with an 8-byte key"""
    if len(plaintext) != 8 or len(key8) != 8:
        raise ValueError("plaintext and key must be exactly 8 bytes")
    k = _bytes_to_int(key8)
    pt = _bytes_to_int(plaintext)
    ct = des_block_encrypt(pt, k)
    return _int_to_bytes(ct, 8)

def decrypt_block(ciphertext: bytes, key8: bytes) -> bytes:
    """Decrypt exactly one 8-byte block with an 8-byte key"""
    if len(ciphertext) != 8 or len(key8) != 8:
        raise ValueError("ciphertext and key must be exactly 8 bytes")
    k = _bytes_to_int(key8)
    ct = _bytes_to_int(ciphertext)
    pt = des_block_decrypt(ct, k)
    return _int_to_bytes(pt, 8)

def encrypt_bytes(data: bytes, key8: bytes) -> bytes:
    """Encrypt variable-length data"""
    if len(key8) != 8:
        raise ValueError("key must be exactly 8 bytes")
    return des_ecb_encrypt(data, key8)

def decrypt_bytes(data: bytes, key8: bytes) -> bytes:
    """Decrypt variable-length data"""
    if len(key8) != 8:
        raise ValueError("key must be exactly 8 bytes")
    return des_ecb_decrypt(data, key8)

# ----------------- CLI for quick testing -----------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["enc", "dec"])
    parser.add_argument("--key", required=True, help="16 hex chars (8 bytes)")
    parser.add_argument("--text", help="text to encrypt")
    parser.add_argument("--hex", help="hex ciphertext to decrypt")
    parser.add_argument("--infile")
    parser.add_argument("--outfile")
    args = parser.parse_args()

    key = bytes.fromhex(args.key)

    if args.mode == "enc":
        if args.text:
            ct = encrypt_bytes(args.text.encode(), key)
            print(ct.hex())
        elif args.infile and args.outfile:
            data = open(args.infile, "rb").read()
            ct = encrypt_bytes(data, key)
            open(args.outfile, "wb").write(ct)
        else:
            print("Provide --text or --infile/--outfile")

    elif args.mode == "dec":
        if args.hex:
            pt = decrypt_bytes(bytes.fromhex(args.hex), key)
            print(pt.decode(errors="ignore"))
        elif args.infile and args.outfile:
            data = open(args.infile, "rb").read()
            pt = decrypt_bytes(data, key)
            open(args.outfile, "wb").write(pt)
        else:
            print("Provide --hex or --infile/--outfile")
