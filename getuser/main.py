import getpass
import os
from flask import Flask, render_template_string

app = Flask(__name__)
username = getpass.getuser()

# Get config from environment variables
app_name = os.getenv("APP_NAME", "GetUser App")
port = os.getenv("PORT", "5000")
message = os.getenv("MESSAGE", "Hello!")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{{app_name}}</title>
</head>
<body>
    <h1>{{app_name}}</h1>
    <p>Current user: {{username}}</p>
    <p>Message: {{message}}</p>
</body>
</html>
"""


@app.route("/")
def hello():
    return render_template_string(
        HTML_TEMPLATE, app_name=app_name, username=username, message=message
    )


# Health check for liveness probe
@app.route("/health")
def health():
    return "OK"


# Ready check for readiness probe
@app.route("/ready")
def ready():
    return "Ready"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(port))
