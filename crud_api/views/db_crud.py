import pyodbc
from flask import request
from flask_restful import Resource


class DatabaseAPI(Resource):
    def __init__(self, conn: pyodbc.Connection, table: str):
        self.conn = conn
        self.table = table

    def get(self):
        """Get all rows from cursor

        Parameters
        ----------
        cursor : pyodbc.Cursor
            Cursor of the database

        Returns
        -------
        list
            List of dicts for each row
        """
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table}")
        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return rows

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
        cursor.execute(query, tuple(params.values()))
        self.conn.commit()
        return {"message": f"{self.table.title()} cadastrado com sucesso!"}, 201

    def put(self):
        """Update a row in the table"""
        cursor = self.conn.cursor()
        params = request.get_json(force=True)
        query = (
            f"UPDATE {self.table} SET "
            f"{', '.join([f'{key} = ?' for key in params.keys()])}"
            f" WHERE id = ?"
        )
        cursor.execute(query, tuple(params.values()) + (params["id"],))
        self.conn.commit()
        return {"message": f"{self.table.title()} atualizado com sucesso!"}, 200

    def delete(self):
        """Delete a row in the table"""
        cursor = self.conn.cursor()
        params = request.get_json(force=True)
        query = f"DELETE FROM {self.table} WHERE id = ?"
        cursor.execute(query, params["id"])
        self.conn.commit()
        return {"message": f"{self.table.title()} excluído com sucesso!"}, 200
