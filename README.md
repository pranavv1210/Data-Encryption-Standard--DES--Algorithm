# Data Encryption Standard (DES) Implementation

## Overview

This project implements the **Data Encryption Standard (DES)** algorithm in Python. It provides:

- A **command-line interface (CLI)** for file or text encryption/decryption.
- A **Tkinter GUI** for interactive encryption/decryption of messages.

DES is a symmetric-key block cipher that encrypts data in 64-bit blocks using a 56-bit key. It is widely used in cryptography to ensure confidentiality.

---

## Features

- **Encrypt / Decrypt text** directly from the GUI.
- **Encrypt / Decrypt files** using CLI (`msg.txt`, `ct.bin`, `out.txt` optional).
- **Hexadecimal output** for ciphertext.
- **PKCS#7 padding** support for variable-length data.
- **Copy result to clipboard** directly from the GUI.
- Easy-to-use **Tkinter interface** with color-coded buttons.

---

## Algorithm Explained (Simplified)

1. **Block Cipher**: DES works on 64-bit blocks of data at a time.
2. **Key**: Uses a 56-bit key (usually represented as 16 hex characters, 8 bytes).  
3. **Rounds**: DES performs 16 rounds of substitution and permutation on each block.  
4. **Encryption**: Each round modifies the block based on the key, producing the ciphertext.  
5. **Decryption**: Uses the same key and reverses the process to retrieve the original plaintext.  
6. **Padding**: If the input data is not a multiple of 8 bytes, PKCS#7 padding is added.

---

## Usage

### 1. GUI (Recommended for simplicity)
Run the Tkinter GUI:

```bash
python gui_des.py
````

* Enter a **16-character hexadecimal key** (e.g., `133457799BBCDFF1`).
* Type **text to encrypt** or **hex to decrypt**.
* Click **Encrypt** / **Decrypt**.
* Click **Copy Result** to copy the output to clipboard.

---

### 2. Command-Line Interface (CLI)

#### Encrypt a text string:

```bash
python des.py enc --key 133457799BBCDFF1 --text "HELLODES"
```

#### Decrypt a hex string:

```bash
python des.py dec --key 133457799BBCDFF1 --hex "d73cd865cebbc7dcd74a91878705b842"
```

#### Encrypt a file:

```bash
python des.py enc --key 133457799BBCDFF1 --infile msg.txt --outfile ct.bin
```

#### Decrypt a file:

```bash
python des.py dec --key 133457799BBCDFF1 --infile ct.bin --outfile out.txt
```

---

## Examples

### Example 1: Text Encryption/Decryption (CLI)

```bash
# Encrypt text
python des.py enc --key 133457799BBCDFF1 --text "HELLODES"
# Output (ciphertext in hex)
d73cd865cebbc7dcd74a91878705b842

# Decrypt ciphertext
python des.py dec --key 133457799BBCDFF1 --hex "d73cd865cebbc7dcd74a91878705b842"
# Output (original text)
HELLODES
```

### Example 2: File Encryption/Decryption (CLI)

```bash
# Encrypt a file
python des.py enc --key 133457799BBCDFF1 --infile msg.txt --outfile ct.bin

# Decrypt the file
python des.py dec --key 133457799BBCDFF1 --infile ct.bin --outfile out.txt

# Verify output
Get-Content out.txt
# Output
HELLODES
```

### Example 3: GUI Usage

* Key: `133457799BBCDFF1`
* Text to Encrypt: `HELLODES`
* Click **Encrypt** → Result: `d73cd865cebbc7dcd74a91878705b842`
* Paste hex in input → Click **Decrypt** → Result: `HELLODES`

---

## Project Structure

```
Data-Encryption-Standard--DES--Algorithm/
│
├── des.py         # DES core logic + CLI interface
├── gui_des.py     # Tkinter GUI frontend
├── README.md      # Project documentation
└── optional sample files (msg.txt, ct.bin, out.txt)
```

---

## Dependencies

* Python 3.x
* Tkinter (usually included with Python standard library)

---

## Notes

* **Key must be 16 hex characters (8 bytes)**.
* **Input for decryption must be valid hex** (spaces/newlines are automatically handled in GUI).
* GUI provides **interactive and user-friendly encryption/decryption**.
* CLI is for quick testing or file-based operations.

---

## Author

* **Name**: Pranav Venu
* **GitHub**: [pranavv1210](https://github.com/pranavv1210)
* **Email**: [pranavv736@gmail.com](mailto:pranavv736@gmail.com)

```
