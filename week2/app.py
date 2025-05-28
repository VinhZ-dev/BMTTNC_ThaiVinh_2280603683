from flask import Flask, render_template, request, jsonify # Đã thêm jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Router routes for home page
@app.route("/")
def home():
    """Renders the home page (index.html)."""
    return render_template('index.html')

# CAESAR CIPHER ALGORITHM ROUTES
caesar_cipher = CaesarCipher()

@app.route("/caesar")
def caesar():
    """Renders the Caesar cipher page (caesar.html)."""
    return render_template('caesar.html')

# Cập nhật route cho Caesar Cipher để khớp với HTML
@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt_web():
    """Handles Caesar cipher encryption requests from the web form."""
    data = request.json # Thay đổi từ request.form sang request.json
    plain_text = data.get('plain_text')
    key = data.get('key')
    
    if not plain_text or key is None:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    
    try:
        key = int(key)
    except ValueError:
        return jsonify({'error': 'Key must be an integer'}), 400

    try:
        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        return jsonify({'encrypted_message': encrypted_text}) # Trả về JSON
    except Exception as e:
        return jsonify({'error': f'Encryption failed: {str(e)}'}), 500

# Cập nhật route cho Caesar Cipher để khớp với HTML
@app.route("/caesar/decrypt", methods=['POST'])
def caesar_decrypt_web():
    """Handles Caesar cipher decryption requests from the web form."""
    data = request.json # Thay đổi từ request.form sang request.json
    cipher_text = data.get('cipher_text')
    key = data.get('key')

    if not cipher_text or key is None:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    
    try:
        key = int(key)
    except ValueError:
        return jsonify({'error': 'Key must be an integer'}), 400

    try:
        decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
        return jsonify({'decrypted_message': decrypted_text}) # Trả về JSON
    except Exception as e:
        return jsonify({'error': f'Decryption failed: {str(e)}'}), 500

# VIGENERE CIPHER ALGORITHM ROUTES
vigenere_cipher = VigenereCipher()

@app.route("/vigenere")
def vigenere():
    """Renders the Vigenere cipher page (vigenere.html)."""
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt_web():
    """Handles Vigenere cipher encryption requests from the web form."""
    data = request.json # Thay đổi từ request.form sang request.json
    plain_text = data.get('plain_text')
    key = data.get('key')

    if not plain_text or not key:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    
    if not key.isalpha():
        return jsonify({'error': 'Vigenere key must contain only alphabetic characters'}), 400

    try:
        encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text}) # Trả về JSON
    except Exception as e:
        return jsonify({'error': f'Encryption failed: {str(e)}'}), 500

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt_web():
    """Handles Vigenere cipher decryption requests from the web form."""
    data = request.json # Thay đổi từ request.form sang request.json
    cipher_text = data.get('cipher_text')
    key = data.get('key')

    if not cipher_text or not key:
        return jsonify({'error': 'Missing cipher_text or key'}), 400

    if not key.isalpha():
        return jsonify({'error': 'Vigenere key must contain only alphabetic characters'}), 400
        
    try:
        decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text}) # Trả về JSON
    except Exception as e:
        return jsonify({'error': f'Decryption failed: {str(e)}'}), 500

# RAIL FENCE CIPHER ALGORITHM ROUTES
railfence_cipher = RailFenceCipher()

@app.route("/railfence")
def railfence():
    """Renders the Rail Fence cipher page (railfence.html)."""
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt_web():
    """Handles Rail Fence cipher encryption requests from the web form."""
    data = request.json # Thay đổi từ request.form sang request.json
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

    try:
        encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text}) # Trả về JSON
    except Exception as e:
        return jsonify({'error': f'Encryption failed: {str(e)}'}), 500

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt_web():
    """Handles Rail Fence cipher decryption requests from the web form."""
    data = request.json # Thay đổi từ request.form sang request.json
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

    try:
        decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text}) # Trả về JSON
    except Exception as e:
        return jsonify({'error': f'Decryption failed: {str(e)}'}), 500

# PLAYFAIR CIPHER ALGORITHM ROUTES
playfair_cipher = PlayFairCipher()

@app.route("/playfair")
def playfair():
    """Renders the Playfair cipher page (playfair.html)."""
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt_web():
    """Handles Playfair cipher encryption requests from the web form."""
    data = request.json # Thay đổi từ request.form sang request.json
    plain_text = data.get('plain_text')
    key = data.get('key')

    if not plain_text or not key:
        return jsonify({'error': 'Missing plain_text or key'}), 400

    if not key.isalpha():
        return jsonify({'error': 'Playfair key must contain only alphabetic characters'}), 400

    try:
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
        return jsonify({'encrypted_text': encrypted_text}) # Trả về JSON
    except Exception as e:
        return jsonify({'error': f'Encryption failed: {str(e)}'}), 500

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt_web():
    """Handles Playfair cipher decryption requests from the web form."""
    data = request.json # Thay đổi từ request.form sang request.json
    cipher_text = data.get('cipher_text')
    key = data.get('key')

    if not cipher_text or not key:
        return jsonify({'error': 'Missing cipher_text or key'}), 400

    if not key.isalpha():
        return jsonify({'error': 'Playfair key must contain only alphabetic characters'}), 400

    try:
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
        return jsonify({'decrypted_text': decrypted_text}) # Trả về JSON
    except Exception as e:
        return jsonify({'error': f'Decryption failed: {str(e)}'}), 500

# TRANSPOSITION CIPHER ALGORITHM ROUTES
transposition_cipher = TranspositionCipher()

@app.route("/transposition")
def transposition():
    """Renders the Transposition cipher page (transposition.html)."""
    return render_template('transposition.html')

@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt_web():
    """Handles Transposition cipher encryption requests from the web form."""
    data = request.json # Thay đổi từ request.form sang request.json
    plain_text = data.get('plain_text')
    key = data.get('key')
    
    if not plain_text or key is None:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    
    try:
        key = int(key)
    except ValueError:
        return jsonify({'error': 'Key must be an integer'}), 400

    try:
        encrypted_text = transposition_cipher.encrypt(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text}) # Trả về JSON
    except Exception as e:
        return jsonify({'error': f'Encryption failed: {str(e)}'}), 500

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt_web():
    """Handles Transposition cipher decryption requests from the web form."""
    data = request.json # Thay đổi từ request.form sang request.json
    cipher_text = data.get('cipher_text')
    key = data.get('key')

    if not cipher_text or key is None:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    
    try:
        key = int(key)
    except ValueError:
        return jsonify({'error': 'Key must be an integer'}), 400

    try:
        decrypted_text = transposition_cipher.decrypt(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text}) # Trả về JSON
    except Exception as e:
        return jsonify({'error': f'Decryption failed: {str(e)}'}), 500


# Main function to run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)