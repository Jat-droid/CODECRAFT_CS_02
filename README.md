# CODECRAFT_CS_02 - Image Encryption via Pixel Manipulation

## 📝 Task Description
This Python script encrypts and decrypts images using a simple XOR operation on pixel RGB values.

## 🔐 How It Works
- Takes an image (e.g., PNG, JPG) and applies an XOR operation to each pixel with a numeric key.
- Running the function twice with the same key decrypts the image.

## 🖼️ Features
- Simple XOR-based pixel encryption
- Decryption using the same function
- Uses the `Pillow` library

## 🚀 How to Run

### 📦 Requirements
Install Pillow library:
```bash
pip install pillow
```

### ▶️ Steps
1. Save an image named `original.png` in the same folder as the script.
2. Run the script using:
```bash
python image_cipher.py
```

3. Output file `encrypted.png` will be saved.
4. To decrypt:
   - Rename `encrypted.png` to input file, and set output as `decrypted.png`
   - Run the script again.

## 💡 Example
```python
# Encrypt:
encrypt_decrypt_image("original.png", "encrypted.png", 123)

# Decrypt:
encrypt_decrypt_image("encrypted.png", "decrypted.png", 123)
```

## 📁 Repository Naming Convention
Name your GitHub repo: `CODECRAFT_CS_02`

---
