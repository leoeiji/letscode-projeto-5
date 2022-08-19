import pyodbc
from flask import Flask
from flask_restful import Api

from views.db_crud import DatabaseAPI

if __name__ == "__main__":
    # Database configuration
    SERVER_NAME = "DONUTS\\MSSQL"
    DATABASE = "grifinoria_airport"

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
    tables_urls = {
        "companhia_aerea": "/companhia_aerea",
        "piloto": "/piloto",
        "tripulante": "/tripulante",
        "aeronave": "/aeronave",
        "voo": "/voo",
        "insumo": "/insumo",
        "cartao_embarque": "/cartao_embarque",
        "passageiro": "/passageiro",
        "bagagem": "/bagagem",
        "voo_piloto": "/voo_piloto",
        "voo_tripulante": "/voo_tripulante",
        "insumo_voo": "/insumo_voo",
    }

    for table, url in tables_urls.items():
        api.add_resource(
            DatabaseAPI,
            url,
            endpoint=table,
            resource_class_kwargs={"conn": conn, "table": table},
        )

    app.run()
