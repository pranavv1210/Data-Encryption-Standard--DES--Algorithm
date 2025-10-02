import tkinter as tk
from tkinter import messagebox
from des import encrypt_bytes, decrypt_bytes

# ----------------- Functions -----------------
def encrypt_text():
    key_hex = key_entry.get().strip()
    plaintext = text_entry.get("1.0", tk.END).strip().replace("\n","").replace("\r","")
    if not key_hex or not plaintext:
        messagebox.showerror("Error", "Enter both key and text!")
        return
    try:
        key = bytes.fromhex(key_hex)
        ciphertext = encrypt_bytes(plaintext.encode("utf-8"), key)
        result_entry.delete("1.0", tk.END)
        result_entry.insert(tk.END, ciphertext.hex())
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_text():
    key_hex = key_entry.get().strip()
    ciphertext_hex = text_entry.get("1.0", tk.END).strip()
    ciphertext_hex = "".join(ciphertext_hex.split())
    if not key_hex or not ciphertext_hex:
        messagebox.showerror("Error", "Enter both key and ciphertext!")
        return
    try:
        key = bytes.fromhex(key_hex)
        plaintext = decrypt_bytes(bytes.fromhex(ciphertext_hex), key)
        result_entry.delete("1.0", tk.END)
        result_entry.insert(tk.END, plaintext.decode(errors="ignore"))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def copy_result():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get("1.0", tk.END).strip())
    messagebox.showinfo("Copied", "Result copied to clipboard!")

# ----------------- GUI Setup -----------------
root = tk.Tk()
root.title("DES Encryption / Decryption")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

# Frames
frame_key = tk.Frame(root, bg="#f0f0f0")
frame_key.pack(pady=10)

frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)

frame_buttons = tk.Frame(root, bg="#f0f0f0")
frame_buttons.pack(pady=10)

frame_result = tk.Frame(root, bg="#f0f0f0")
frame_result.pack(pady=10)

# Key
tk.Label(frame_key, text="Key (16 hex chars, 8 bytes):", bg="#f0f0f0", font=("Arial", 12)).pack()
key_entry = tk.Entry(frame_key, width=40, font=("Arial", 12))
key_entry.pack(pady=5)

# Input
tk.Label(frame_input, text="Input (text for encryption / hex for decryption):", bg="#f0f0f0", font=("Arial", 12)).pack()
text_entry = tk.Text(frame_input, height=5, width=50, font=("Arial", 12), bg="#ffffff")
text_entry.pack(pady=5)

# Buttons
encrypt_btn = tk.Button(frame_buttons, text="Encrypt", width=15, bg="#4CAF50", fg="white",
                        activebackground="#45a049", font=("Arial", 12), command=encrypt_text)
encrypt_btn.pack(side="left", padx=10)

decrypt_btn = tk.Button(frame_buttons, text="Decrypt", width=15, bg="#2196F3", fg="white",
                        activebackground="#0b7dda", font=("Arial", 12), command=decrypt_text)
decrypt_btn.pack(side="left", padx=10)

copy_btn = tk.Button(frame_buttons, text="Copy Result", width=15, bg="#FF9800", fg="white",
                     activebackground="#e68a00", font=("Arial", 12), command=copy_result)
copy_btn.pack(side="left", padx=10)

# Result
tk.Label(frame_result, text="Result:", bg="#f0f0f0", font=("Arial", 12)).pack()
result_entry = tk.Text(frame_result, height=5, width=50, font=("Arial", 12), bg="#e8e8e8")
result_entry.pack(pady=5)

root.mainloop()
