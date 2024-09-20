from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads' 
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def vigenere_encrypt(plaintext, key):
    ciphertext = []
    key = key.upper()
    for i in range(len(plaintext)):
        letter = plaintext[i]
        key_letter = key[i % len(key)]
        encrypted_letter = chr(((ord(letter) - 65) + (ord(key_letter) - 65)) % 26 + 65)
        ciphertext.append(encrypted_letter)
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    plaintext = []
    key = key.upper()
    for i in range(len(ciphertext)):
        letter = ciphertext[i]
        key_letter = key[i % len(key)]
        decrypted_letter = chr(((ord(letter) - 65) - (ord(key_letter) - 65)) % 26 + 65)
        plaintext.append(decrypted_letter)
    return ''.join(plaintext)

def create_playfair_matrix(key):
    key = ''.join(sorted(set(key), key=key.index)).replace('J', 'I')
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    matrix = []
    used_chars = set(key)
    matrix.extend(key)
    matrix.extend([c for c in alphabet if c not in used_chars])
    return [matrix[i:i+5] for i in range(0, len(matrix), 5)]

def playfair_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace('J', 'I').replace(' ', '')
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    matrix = create_playfair_matrix(key)
    ciphertext = []
    
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i+1]
        row1, col1 = find_position(a, matrix)
        row2, col2 = find_position(b, matrix)
        
        if row1 == row2:
            ciphertext.append(matrix[row1][(col1 + 1) % 5])
            ciphertext.append(matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:
            ciphertext.append(matrix[(row1 + 1) % 5][col1])
            ciphertext.append(matrix[(row2 + 1) % 5][col2])
        else:
            ciphertext.append(matrix[row1][col2])
            ciphertext.append(matrix[row2][col1])
    
    return ''.join(ciphertext)

def playfair_decrypt(ciphertext, key):
    matrix = create_playfair_matrix(key)
    plaintext = []
    
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(a, matrix)
        row2, col2 = find_position(b, matrix)
        
        if row1 == row2:
            plaintext.append(matrix[row1][(col1 - 1) % 5])
            plaintext.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            plaintext.append(matrix[(row1 - 1) % 5][col1])
            plaintext.append(matrix[(row2 - 1) % 5][col2])
        else:
            plaintext.append(matrix[row1][col2])
            plaintext.append(matrix[row2][col1])
    
    return ''.join(plaintext)

def find_position(char, matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace(' ', '')
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        x1 = ord(plaintext[i]) - 65
        x2 = ord(plaintext[i+1]) - 65
        y1 = (key_matrix[0][0] * x1 + key_matrix[0][1] * x2) % 26
        y2 = (key_matrix[1][0] * x1 + key_matrix[1][1] * x2) % 26
        ciphertext += chr(y1 + 65) + chr(y2 + 65)
    
    return ciphertext

def hill_decrypt(ciphertext, key_matrix):
    det = (key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]) % 26
    det_inv = pow(det, -1, 26)
    
    inv_matrix = [
        [key_matrix[1][1] * det_inv % 26, -key_matrix[0][1] * det_inv % 26],
        [-key_matrix[1][0] * det_inv % 26, key_matrix[0][0] * det_inv % 26]
    ]
    
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        y1 = ord(ciphertext[i]) - 65
        y2 = ord(ciphertext[i+1]) - 65
        x1 = (inv_matrix[0][0] * y1 + inv_matrix[0][1] * y2) % 26
        x2 = (inv_matrix[1][0] * y1 + inv_matrix[1][1] * y2) % 26
        plaintext += chr(x1 + 65) + chr(x2 + 65)
    
    return plaintext

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    error = ""
    if request.method == 'POST':
        cipher_type = request.form['cipher_type']
        operation = request.form['operation']
        
        file = request.files.get('file')
        if file and file.filename.endswith('.txt'):
            content = file.read().decode('utf-8').upper().replace('\n', '')
        else:
            content = request.form['text'].upper().strip()
        
        key = request.form['key'].upper().strip()

        if len(key) < 12:
            error = "Key harus terdiri dari minimal 12 karakter."
        elif not content:
            error = "Silakan masukkan teks atau unggah file .txt."
        else:
            if cipher_type == 'vigenere':
                if operation == 'encrypt':
                    result = vigenere_encrypt(content, key)
                elif operation == 'decrypt':
                    result = vigenere_decrypt(content, key)
            
            elif cipher_type == 'playfair':
                if operation == 'encrypt':
                    result = playfair_encrypt(content, key)
                elif operation == 'decrypt':
                    result = playfair_decrypt(content, key)
            
            elif cipher_type == 'hill':
                key_matrix = [[3, 3], [2, 5]] 
                if operation == 'encrypt':
                    result = hill_encrypt(content, key_matrix)
                elif operation == 'decrypt':
                    result = hill_decrypt(content, key_matrix)

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
