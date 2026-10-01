import random

from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from werkzeug.security import generate_password_hash, check_password_hash

from database import get_db_connection, init_db

app = Flask(__name__)
app.secret_key = "troque-esta-chave-antes-de-colocar-em-producao"

PLANOS = {
    "essencial": {"nome": "Essencial", "preco_exibido": "Grátis", "valor": "0"},
    "plus": {"nome": "Plus", "preco_exibido": "R$ 19/mês", "valor": "19"},
    "pro": {"nome": "Pro", "preco_exibido": "R$ 39/mês", "valor": "39"},
}


@app.route("/")
def index():
    return render_template("index.html", nome_usuario=session.get("nome"))


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    plano = request.args.get("plano", "")

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")
        plano = request.form.get("plano", "")

        if not nome or not email or not senha:
            flash("Preencha nome, e-mail e senha.")
            return render_template("cadastro.html", plano=plano)

        conn = get_db_connection()
        existente = conn.execute(
            "SELECT id FROM users WHERE email = ?", (email,)
        ).fetchone()

        if existente:
            conn.close()
            flash("Já existe uma conta cadastrada com esse e-mail.")
            return render_template("cadastro.html", plano=plano)

        senha_hash = generate_password_hash(senha)
        conn.execute(
            "INSERT INTO users (nome, email, senha_hash) VALUES (?, ?, ?)",
            (nome, email, senha_hash),
        )
        conn.commit()
        user = conn.execute(
            "SELECT * FROM users WHERE email = ?", (email,)
        ).fetchone()
        conn.close()

        session["user_id"] = user["id"]
        session["nome"] = user["nome"]

        # se veio de um plano pago, manda direto pro checkout depois de logar
        if plano in ("plus", "pro"):
            return redirect(url_for("comprar", plano=plano))

        return redirect(url_for("sistema"))

    return render_template("cadastro.html", plano=plano)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE email = ?", (email,)
        ).fetchone()
        conn.close()

        if user and check_password_hash(user["senha_hash"], senha):
            session["user_id"] = user["id"]
            session["nome"] = user["nome"]
            return redirect(url_for("sistema"))

        flash("E-mail ou senha inválidos.")
        return render_template("login.html")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/sistema")
def sistema():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    compras = conn.execute(
        "SELECT * FROM compras WHERE user_id = ? ORDER BY criado_em DESC",
        (session["user_id"],),
    ).fetchall()
    conn.close()

    return render_template("sistema.html", nome=session.get("nome"), compras=compras)


@app.route("/comprar/<plano>", methods=["GET", "POST"])
def comprar(plano):
    if plano not in PLANOS:
        return redirect(url_for("index"))

    info = PLANOS[plano]

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip().lower()

        if not nome or not email:
            flash("Preencha nome e e-mail para concluir a compra.")
            return render_template("comprar.html", plano=plano, info=info)

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO compras (user_id, plano, nome, email, valor) VALUES (?, ?, ?, ?, ?)",
            (session.get("user_id"), info["nome"], nome, email, info["valor"]),
        )
        conn.commit()
        conn.close()

        return render_template(
            "comprar_sucesso.html", plano=plano, info=info, nome=nome
        )

    nome_preenchido = session.get("nome", "")
    return render_template(
        "comprar.html", plano=plano, info=info, nome_preenchido=nome_preenchido
    )


@app.route("/api/scan")
def api_scan():
    """Alimenta o botão 'Analisar agora' da página inicial com um resultado simulado."""
    resultados = [
        {
            "item": "Arquivos do sistema",
            "status": f"{random.randint(1500, 2200)} verificados · limpos",
        },
        {
            "item": "Downloads recentes",
            "status": f"{random.randint(1, 6)} verificados · limpos",
        },
        {
            "item": "Conexões de rede",
            "status": "Nenhuma atividade suspeita",
        },
        {
            "item": "E-mails analisados",
            "status": f"{random.randint(0, 3)} links de phishing bloqueados",
        },
    ]
    return jsonify({"resultados": resultados})


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
