from database import Database

# URI, usuário e senha do banco de dados Neo4j
uri = "bolt://localhost:7687"
user = "neo4j"
password = "password"

# Instanciando a classe Database
db = Database(uri, user, password)

# Query 1: Buscar pelo professor cujo nome seja "Renzo", retornar ano_nasc e CPF
query1 = """
MATCH (t:Teacher{name:'Renzo'})
RETURN t.ano_nasc, t.cpf
"""

# Query 2: Buscar pelos professores cujo nome começa com "M", retornar name e cpf
query2 = """
MATCH (t:Teacher)
WHERE t.name STARTS WITH 'M'
RETURN t.name, t.cpf
"""

# Query 3: Buscar pelos nomes de todas as cidades, retornar os nomes
query3 = """
MATCH (c:City)
RETURN c.name
"""

# Query 4: Buscar pelas escolas onde o número esteja entre 150 e 550, retornar nome, endereço e número
query4 = """
MATCH (s:School)
WHERE s.number >= 150 AND s.number <= 550
RETURN s.name, s.address, s.number
"""

# Query 5: Encontrar o ano de nascimento do professor mais jovem e do professor mais velho
query5 = """
MATCH (t:Teacher)
WITH min(t.ano_nasc) AS minYear, max(t.ano_nasc) AS maxYear
MATCH (youngest:Teacher{ano_nasc: minYear}), (oldest:Teacher{ano_nasc: maxYear})
RETURN youngest.ano_nasc AS youngest_birth_year, oldest.ano_nasc AS oldest_birth_year
"""

# Query 6: Encontrar a média aritmética para os habitantes de todas as cidades
query6 = """
MATCH (c:City)
RETURN avg(c.population) AS average_population
"""

# Query 7: Encontrar a cidade cujo CEP seja igual a "37540-000" e retornar o nome com todas as letras "a" substituídas por "A"
query7 = """
MATCH (c:City{cep:'37540-000'})
RETURN replace(c.name, 'a', 'A') AS modified_name
"""

# Query 8: Para todos os professores, retornar um caractere, iniciando a partir da 3ª letra do nome
query8 = """
MATCH (t:Teacher)
RETURN substring(t.name, 3, 1) AS third_character
"""

# Executando as queries
result1 = db.execute_query(query1)
result2 = db.execute_query(query2)
result3 = db.execute_query(query3)
result4 = db.execute_query(query4)
result5 = db.execute_query(query5)
result6 = db.execute_query(query6)
result7 = db.execute_query(query7)
result8 = db.execute_query(query8)

# Exibindo os resultados
print("Resultado da Query 1:")
for record in result1:
    print(record)

print("\nResultado da Query 2:")
for record in result2:
    print(record)

print("\nResultado da Query 3:")
for record in result3:
    print(record)

print("\nResultado da Query 4:")
for record in result4:
    print(record)

print("\nResultado da Query 5:")
for record in result5:
    print(record)

print("\nResultado da Query 6:")
for record in result6:
    print(record)

print("\nResultado da Query 7:")
for record in result7:
    print(record)

print("\nResultado da Query 8:")
for record in result8:
    print(record)

# Fechando a conexão com o banco de dados
db.close()
