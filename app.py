from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)  # Perbaikan: __name__

# Simpan username dan password yang valid (contoh sederhana dengan dictionary)
valid_users = {
    'user1': 'password1',
    'user2': 'password2',
    'admin': 'adminpass'
}

# Route untuk halaman login
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Periksa username dan password dalam valid_users
        if username in valid_users and valid_users[username] == password:
            return redirect(url_for('success'))
        else:
            return "Login gagal. Username atau password salah."

    return render_template('index.html')

# Route untuk halaman sukses
@app.route('/success')
def success():
    return "Login berhasil! Selamat datang."

if __name__ == '__main__':  # Perbaikan: __main__
    app.run(debug=True)
