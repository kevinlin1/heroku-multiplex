import requests

from flask import Blueprint, Flask, request
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

modules = {
        "forwarded": 8000, # os.environ[...]
        }

app = Flask(__name__)
http = requests.Session()
http.mount("http://", HTTPAdapter(max_retries=Retry(
    status=6, backoff_factor=0.5, status_forcelist=[500]
    )))

def using(module_name, port):
    module = Blueprint(module_name.replace("-", "_"), module_name)

    @module.route("/")
    @module.route("/<path:path>")
    def handle(path):
        relative_path = request.full_path[len(f"/{module_name}/"):]
        response = http.get(f"http://localhost:{port}/{relative_path}")
        return response.content, response.status_code, response.headers.items()

    return module

for module_name, port in modules.items():
    app.register_blueprint(using(module_name, port), url_prefix=f"/{module_name}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
