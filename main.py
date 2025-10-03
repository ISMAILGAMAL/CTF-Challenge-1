from flask import Flask, request, render_template, render_template_string

app = Flask(__name__, static_folder='static', static_url_path='')

FLAG1 = "CYBERUS{example_flag_1}" 
FLAG2 = "CYBERUS{example_flag_2}" 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/supersecret")
def supersecret():
    return render_template("secret.html", flag=FLAG1)


@app.route("/preview", methods=["GET", "POST"])
def preview():
    if request.method == "POST":
        user_template = request.form.get("content", "")

        template = """
        {% extends "base.html" %}
        {% block content %}
          <h2>Live Preview</h2>
          <p>Below is the rendered output of your template:</p>
          <div class="preview-box" style="border:1px solid #ccc;padding:12px;background:#fafafa;">
        """
        template += user_template
        template += """
          </div>
          <hr>
          <p><small>Preview rendered on the server.</small></p>
        {% endblock %}
        """
        
        return render_template_string(template)
    return render_template("preview.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4444)
