from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mi Página Web</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
            }
            
            .container {
                text-align: center;
                margin: 100px auto;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            
            h1 {
                color: #333;
            }
            
            p {
                color: #666;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>¡Hola, curso Python!</h1>
            <p>Esta es mi primera página web con Python y Flask.</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)