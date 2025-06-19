import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)
    width, height = img.size

    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'

    data_index = 0
    pixels = img.load()

    for y in range(height):
        for x in range(width):
            pixel = list(pixels[x, y])

            for i in range(3):
                if data_index < len(binary_message):
                    pixel[i] = int(format(pixel[i], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1

            pixels[x, y] = tuple(pixel)

            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    encoded_image_path = "encoded_image.png"
    img.save(encoded_image_path)
    print("Steganography complete. Encoded image saved as", encoded_image_path)

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return

    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)

if __name__ == "__main__":
    main()
