from PIL import Image

def encrypt_decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img = img.convert("RGB")
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            # XOR encryption/decryption
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)
    print(f"Processed image saved as: {output_path}")

# Example usage
# Make sure to have an image named 'original.png' in the same folder
input_file = "original.png"       # Input image filename
output_file = "encrypted.png"     # Output encrypted/decrypted image filename
key = 123                         # Encryption/Decryption key

encrypt_decrypt_image(input_file, output_file, key)

# To decrypt, run again using encrypted.png as input and new output name:
# encrypt_decrypt_image("encrypted.png", "decrypted.png", 123)
