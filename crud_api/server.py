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
    # api.add_resource(Piloto, "/piloto", resource_class_kwargs={"conn": conn})
    # api.add_resource(Insumo, "/insumo", resource_class_kwargs={"conn": conn})
    # api.add_resource(Tripulante, "/tripulante", resource_class_kwargs={"conn": conn})
    api.add_resource(
        DatabaseAPI, "/piloto", resource_class_kwargs={"conn": conn, "table": "piloto"}
    )

    app.run()
