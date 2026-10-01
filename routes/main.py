from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    # Esta é uma rota Flask. Ela responde quando alguém acessa a página inicial.
    return render_template("index.html")


@main_bp.route("/sistema")
def sistema():
    return render_template("sistema.html")
