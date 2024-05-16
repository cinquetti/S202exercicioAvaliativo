from database import Database

class TeacherCRUD:
    def __init__(self, uri, user, password):
        self.db = Database(uri, user, password)

    def create(self, name, ano_nasc, cpf):
        query = f"""
        CREATE (:Teacher{{name:'{name}', ano_nasc:{ano_nasc}, cpf:'{cpf}'}})
        """
        self.db.execute_query(query)

    def read(self, name):
        query = f"""
        MATCH (t:Teacher{{name:'{name}'}})
        RETURN t
        """
        result = self.db.execute_query(query)
        return result

    def delete(self, name):
        query = f"""
        MATCH (t:Teacher{{name:'{name}'}})
        DETACH DELETE t
        """
        self.db.execute_query(query)

    def update(self, name, newCpf):
        query = f"""
        MATCH (t:Teacher{{name:'{name}'}})
        SET t.cpf = '{newCpf}'
        """
        self.db.execute_query(query)
