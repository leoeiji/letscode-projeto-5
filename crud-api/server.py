import pyodbc
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

# Database configuration
SERVER_NAME = "DONUTS\\MSSQL"
DATABASE = "grifinoria_airport"


class Piloto(Resource):
    def __init__(self, conn: pyodbc.Connection):
        self.conn = conn

    def get(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM piloto")
        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return jsonify(rows)

    def post(self):
        # Parameters from request
        params = request.get_json(force=True)
        rab = params.get("rab")
        nome = params.get("nome")
        sobrenome = params.get("sobrenome")
        telefone = params.get("telefone")
        email = params.get("email")
        comandante = params.get("comandante")

        # Insert query
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO piloto (rab, nome, sobrenome, telefone, email, comandante) VALUES (?, ?, ?, ?, ?, ?)",
            (rab, nome, sobrenome, telefone, email, comandante),
        )
        self.conn.commit()
        return {"message": "Piloto cadastrado com sucesso!"}, 201


if __name__ == "__main__":
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        f"Server={SERVER_NAME};"
        f"Database={DATABASE};"
        "Trusted_Connection=yes;"
    )

    # Flask server
    app = Flask(__name__)
    api = Api(app)

    # Adding API paths
    api.add_resource(Piloto, "/piloto", resource_class_kwargs={"conn": conn})

    app.run()
