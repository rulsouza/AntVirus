from flask import Blueprint, flash, redirect, render_template, request, url_for

from models import records

# EXEMPLO:
# Cada grupo deverá substituir "records" pela entidade principal
# do seu próprio projeto, como livros, pacientes ou produtos.
# Para cada entidade nova: um arquivo em models/ e um em routes/.
records_bp = Blueprint("records", __name__, url_prefix="/sistema/registros")


@records_bp.route("/")
def listar_registros():
    return render_template("records/lista.html", records=records.listar_registros())


@records_bp.route("/novo", methods=["GET", "POST"])
def novo_registro():
    if request.method == "POST":
        title = request.form["title"].strip()
        description = request.form["description"].strip()

        if not title:
            flash("Informe um título para o registro.", "danger")
            return render_template("records/form.html", record=None)

        records.criar_registro(title, description)
        flash("Registro criado com sucesso.", "success")
        return redirect(url_for("records.listar_registros"))

    return render_template("records/form.html", record=None)


@records_bp.route("/<int:record_id>/editar", methods=["GET", "POST"])
def editar_registro(record_id):
    record = records.buscar_registro(record_id)

    if record is None:
        flash("Registro não encontrado.", "danger")
        return redirect(url_for("records.listar_registros"))

    if request.method == "POST":
        title = request.form["title"].strip()
        description = request.form["description"].strip()

        if not title:
            flash("Informe um título para o registro.", "danger")
            return render_template("records/form.html", record=record)

        records.atualizar_registro(record_id, title, description)
        flash("Registro atualizado com sucesso.", "success")
        return redirect(url_for("records.listar_registros"))

    return render_template("records/form.html", record=record)


@records_bp.route("/<int:record_id>/excluir", methods=["POST"])
def excluir_registro(record_id):
    # DELETE remove um registro. Por isso, usamos POST para esta ação.
    records.excluir_registro(record_id)
    flash("Registro excluído.", "success")
    return redirect(url_for("records.listar_registros"))
