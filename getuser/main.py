import getpass
import signal
import sys
from flask import Flask, render_template_string

app = Flask(__name__)
username = getpass.getuser()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Info</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .container {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            text-align: center;
            max-width: 400px;
            width: 90%;
        }
        h1 {
            color: #333;
            margin-bottom: 1rem;
            font-size: 2rem;
        }
        .username {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            padding: 1rem 2rem;
            border-radius: 10px;
            font-size: 1.5rem;
            font-weight: bold;
            margin: 1rem 0;
            display: inline-block;
        }
        .status {
            color: #666;
            font-size: 0.9rem;
            margin-top: 1rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>👋 Hello!</h1>
        <div class="username">{{ username }}</div>
        <p class="status">Application is running successfully</p>
    </div>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, username=username)


def signal_handler(signum, frame):
    print(f"Received signal {signum}. Shutting down...")
    sys.exit(0)


def main():
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    print(f"Starting web server for user: {username}")
    print("Web UI available at: http://0.0.0.0:5000")

    app.run(host="0.0.0.0", port=5000, debug=False)


if __name__ == "__main__":
    main()
