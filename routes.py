import os

def handle_route(path, method, data=None):
    if path == "/":
        return render_template("index.html"), "text/html"
    elif path == "/submit" and method == "POST":
        return handle_form_submission(data), "text/html"
    else:
        return render_template("404.html"), "text/html"

def render_template(template_name, context=None):
    if context is None:
        context = {}
    template_path = os.path.join("templates", template_name)
    with open(template_path, "r") as template_file:
        content = template_file.read()
    for key, value in context.items():
        content = content.replace(f"{{{{ {key} }}}}", value)
    return content

def handle_form_submission(data):
    name = data.get('name', [''])[0]
    email = data.get('email', [''])[0]
    return render_template("index.html", {"name": name, "email": email})
