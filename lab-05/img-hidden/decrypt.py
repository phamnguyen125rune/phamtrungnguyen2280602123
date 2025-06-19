import sys
from PIL import Image

def decode_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    binary_data = ""

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            for channel in (r, g, b):
                binary_data += format(channel, '08b')[-1]

    message = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        char = chr(int(byte, 2))
        if char == '\0':
            break
        message += char

    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    image_path = sys.argv[1]
    decoded_message = decode_image(image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()