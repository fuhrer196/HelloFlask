from app import app

@app.route('/')
@app.route('/index')

def index():
    return """
    <html>
        <head><title> :D </title></head>
        <body><center> To the world, hello I say </center></body>
    </html>
    """

