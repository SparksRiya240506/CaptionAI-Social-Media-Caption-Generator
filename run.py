from pyngrok import ngrok
from app import app

public_url = ngrok.connect(5000)

print("Public URL:", public_url)

app.run(port=5000)