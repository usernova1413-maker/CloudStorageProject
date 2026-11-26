
from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

HTML = """
<h1>Cloud Storage System</h1>
<h3>Upload your file</h3>
<form method="POST" enctype="multipart/form-data">
<input type="file" name="file" required>
<button type="submit">Upload</button>
</form>
<p>{{ message }}</p>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        file = request.files.get("file")
        if file and file.filename:
            message = "File received: " + file.filename
    return render_template_string(HTML, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
