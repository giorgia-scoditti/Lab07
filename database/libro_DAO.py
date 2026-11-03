from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def leggi_tutti_i_libri(self):
        db = DBConnect()
        cnx = db.get_connection()
        if cnx is not None:
            print("Connection established")
        query = f"""SELECT l.* 
                    FROM libro l
                 """
        cursor = cnx.cursor()
        cursor.execute(query)
        result = []
        for row in cursor:
            libro = Libro(*row)
            result.append(libro)
        cursor.close()
        cnx.close()
        return result

    def leggi_libri_in_una_biblioteca_specifica(self, letter):
        db = DBConnect()
        cnx = db.get_connection()
        if cnx is not None:
            print("Connection established")
            query = f"""SELECT l.* 
                        FROM biblioteca b, libro l
                        WHERE l.id_biblioteca = b.id
                     """
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            for row in cursor:
                libro = Libro(*row)
                result.append(libro)
            cursor.close()
            cnx.close()
            return result