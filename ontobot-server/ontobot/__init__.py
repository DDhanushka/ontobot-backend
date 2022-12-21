import json
from flask import Flask, jsonify, request

from ontobot.services.subkind import Subkind
from ontobot.services.factory import ODPFactory
from ontobot.services.owl import OWL

app = Flask(__name__)

data = {}

@app.route('/onto')
def get_ontos():
    # parsed_json = json.loads(data)
    sk: Subkind = ODPFactory.get_ontouml_odp(
        'subkind', data)
    sk.check_subkind()
    owl_res = OWL(data)
    # print(owl_res.get_taxonomy_json())
    return jsonify(owl_res.get_taxonomy_json())


@app.route('/onto', methods=['POST'])
def add_ontos():
    global data
    data = request.get_json()
    return "", 204


if __name__ == "__main__":
    app.run()