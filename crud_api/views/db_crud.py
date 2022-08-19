import json

import pyodbc
from flask import request
from flask_restful import Resource


class DatabaseAPI(Resource):
    """Handles the interaction with a given table name

    Properties
    ----------
    conn : pyodbc.Connection
        Connection to the database
    table : str
        Name of the table to be interacted with
    """

    def __init__(self, conn: pyodbc.Connection, table: str):
        self.conn = conn
        self.table = table

    def get(self):
        """Get all rows from cursor"""
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table}")
        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
        rngData = json.dumps(rows, indent=4, sort_keys=True, default=str)
        return json.loads(rngData)

    def post(self):
        """Insert a new row in the table"""
        cursor = self.conn.cursor()
        params = request.get_json(force=True)
        query = (
            f"INSERT INTO {self.table} ("
            f"{', '.join(params.keys())}"
            f") VALUES ("
            f"{', '.join(['?'] * len(params))}"
            f")"
        )
        try:
            cursor.execute(query, tuple(params.values()))
            self.conn.commit()
            return {"message": f"{self.table.title()} cadastrado com sucesso!"}, 201
        except Exception as e:
            return {"message": f"{e}"}, 400

    def put(self):
        """Update a row in the table"""
        cursor = self.conn.cursor()
        params = request.get_json(force=True)
        key = params.pop("_key")
        value = params.pop("_value")
        query = (
            f"UPDATE {self.table} SET "
            f"{', '.join([f'{i} = ?' for i in params.keys()])}"
            f" WHERE {key} = ?"
        )
        try:
            cursor.execute(query, tuple(params.values()) + (value,))
            self.conn.commit()
            return {"message": f"{self.table.title()} atualizado com sucesso!"}, 200
        except Exception as e:
            return {"message": f"{e}"}, 400

    def delete(self):
        """Delete a row in the table"""
        cursor = self.conn.cursor()
        params = request.get_json(force=True)
        key = params.pop("_key")
        value = params.pop("_value")
        query = f"DELETE FROM {self.table} WHERE {key} = ?"
        try:
            cursor.execute(query, value)
            self.conn.commit()
            return {"message": f"{self.table.title()} excluído com sucesso!"}, 200
        except Exception as e:
            return {"message": f"{e}"}, 400
