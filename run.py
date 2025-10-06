from app import create_app

app = create_app()

@app.route("/")
def home():
    return "Welcome to the Flask app root!"

@app.route("/hello-vercel")
def hello_vercel():
    return "✅ Flask is running on Vercel!"

if __name__ == '__main__':
    app.run(debug=True)
