from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
RailFence_cipher = RailFenceCipher()
Playfair_cipher = PlayfairCipher()
Transposition_cipher = TranspositionCipher()

#CAESAR CIPHER ALGORITHM
@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])  
    encrypted_text =  caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})




@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.json
    encrypted_text = data['encrypted_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(encrypted_text, key)
    return jsonify({'decrypted_text': decrypted_text})


#VIGENERE CIPHER ALGORITHM
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    encrypted_text = data['encrypted_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(encrypted_text, key)
    return jsonify({'decrypted_text': decrypted_text})

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = RailFence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.json
    encrypted_text = data['encrypted_text']
    key = data['key']
    decrypted_text = RailFence_cipher.rail_fence_decrypt(encrypted_text, key)
    return jsonify({'decrypted_text': decrypted_text})





@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    matrix = Playfair_cipher.create_playfair_matrix(key)
    return jsonify({'playfair_matrix': matrix})


@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    matrix = Playfair_cipher.playfair_creatematrix(key)
    encrypted_text = Playfair_cipher.playfair_encrypt(plain_text, matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    encrypted_text = data['encrypted_text']
    key = data['key']
    matrix = Playfair_cipher.create_playfair_matrix(key)
    decrypted_text = Playfair_cipher.playfair_decrypt(encrypted_text, matrix)
    return jsonify({'decrypted_text': decrypted_text})


@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = Transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    encrypted_text = data.get('encrypted_text')
    key = int(data.get('key'))
    decrypted_text = Transposition_cipher.decrypt(encrypted_text, key)
    return jsonify({'decrypted_text': decrypted_text})

#main function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)