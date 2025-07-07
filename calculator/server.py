"""Flask server exposing calculator operations."""

from flask import Flask, request, jsonify, render_template
from .core import calculate

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.get_json(force=True)
    try:
        a = float(data.get("numero1"))
        b = float(data.get("numero2"))
        operacion = data.get("operacion")
        resultado = calculate(a, b, operacion)
    except (TypeError, ValueError) as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify({"resultado": resultado})


def run():
    app.run(debug=True)


if __name__ == "__main__":
    run()
