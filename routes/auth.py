from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from models import users

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    # GET normalmente é utilizado para carregar a página.
    # POST normalmente é utilizado quando enviamos um formulário.
    if request.method == "POST":
        # Aqui buscamos os dados enviados pelo formulário.
        name = request.form["name"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        if not name or not email or not password:
            flash("Preencha todos os campos.", "danger")
            return render_template("cadastro.html")

        if not users.criar_usuario(name, email, generate_password_hash(password)):
            flash("Este e-mail já está cadastrado.", "danger")
            return render_template("cadastro.html")

        flash("Conta criada! Agora faça seu acesso.", "success")
        # redirect envia o usuário para outra rota.
        return redirect(url_for("auth.login"))

    return render_template("cadastro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        user = users.buscar_usuario_por_email(email)

        if user and check_password_hash(user["password"], password):
            # Em um sistema real, use sessões e autenticação adequada.
            # Neste exemplo, o objetivo é apenas praticar formulário e validação.
            return redirect(url_for("main.sistema"))

        flash("E-mail ou senha incorretos.", "danger")

    return render_template("login.html")
