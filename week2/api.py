from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher # Thêm dòng này

app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data.get('plain_text')
    key = data.get('key')
    
    if not plain_text or key is None:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    
    try:
        key = int(key)
    except ValueError:
        return jsonify({'error': 'Key must be an integer'}), 400

    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text')
    key = data.get('key')

    if not cipher_text or key is None:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    
    try:
        key = int(key)
    except ValueError:
        return jsonify({'error': 'Key must be an integer'}), 400

    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data.get('plain_text')
    key = data.get('key')

    if not plain_text or not key:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    
    # Đảm bảo key chỉ chứa các ký tự chữ cái
    if not key.isalpha():
        return jsonify({'error': 'Vigenere key must contain only alphabetic characters'}), 400

    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text')
    key = data.get('key')

    if not cipher_text or not key:
        return jsonify({'error': 'Missing cipher_text or key'}), 400

    # Đảm bảo key chỉ chứa các ký tự chữ cái
    if not key.isalpha():
        return jsonify({'error': 'Vigenere key must contain only alphabetic characters'}), 400
        
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# RAILFENCE CIPHER ALGORITHM
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.json
    plain_text = data.get('plain_text')
    key = data.get('key')

    if not plain_text or key is None:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    
    try:
        key = int(key)
        if key <= 1:
            return jsonify({'error': 'Rail Fence key must be an integer greater than 1'}), 400
    except ValueError:
        return jsonify({'error': 'Rail Fence key must be an integer'}), 400

    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text')
    key = data.get('key')

    if not cipher_text or key is None:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    
    try:
        key = int(key)
        if key <= 1:
            return jsonify({'error': 'Rail Fence key must be an integer greater than 1'}), 400
    except ValueError:
        return jsonify({'error': 'Rail Fence key must be an integer'}), 400

    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})


# PLAYFAIR CIPHER ALGORITHM # Thêm phần này
playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data.get('key')

    if not key:
        return jsonify({'error': 'Missing key'}), 400
    
    if not key.isalpha():
        return jsonify({'error': 'Playfair key must contain only alphabetic characters'}), 400

    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route("/api/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data.get('plain_text')
    key = data.get('key')

    if not plain_text or not key:
        return jsonify({'error': 'Missing plain_text or key'}), 400

    if not key.isalpha():
        return jsonify({'error': 'Playfair key must contain only alphabetic characters'}), 400

    # Playfair mã hóa cần matrix, nên tạo lại matrix ở đây hoặc truyền từ creatematrix
    # Để đơn giản, chúng ta sẽ tạo matrix lại trong mỗi hàm encrypt/decrypt
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text')
    key = data.get('key')

    if not cipher_text or not key:
        return jsonify({'error': 'Missing cipher_text or key'}), 400

    if not key.isalpha():
        return jsonify({'error': 'Playfair key must contain only alphabetic characters'}), 400

    # Tương tự, tạo matrix lại trong hàm decrypt
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})

# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)