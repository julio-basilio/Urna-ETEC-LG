
import mysql.connector


class Conexao:

    # ===== Atributos =====
    def __init__(self, dadoPesquisa=None):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "Urna"
        self.conexao = None
        self.dadoPesquisa = dadoPesquisa

    # ===== Método ligar =====
    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            if self.conexao.is_connected():
                print("Conexão realizada com sucesso!")

            return self.conexao

        except mysql.connector.Error as erro:
            print(f"Erro ao conectar ao banco: {erro}")
            self.conexao = None
            return None

    # ===== Método fechar =====
    def fechar(self):
        if self.conexao is not None and self.conexao.is_connected():
            self.conexao.close()
            print("Conexão encerrada.")

        self.conexao = None

    # ===== Método pesquisar =====
    def pesquisar(self, tabela, dado, valor):
        # Tabelas e colunas permitidas
        colunas = {
            "Eleitores": [
                "id_eleitor",
                "rm_eleitor",
                "nome_eleitor",
                "sobreN_eleitor",
                "idade_eleitor",
                "foto_eleitor",
                "curso_eleitor"
            ],
            "Candidatos": [
                "id_cand",
                "id_eleitor",
                "nome_cand",
                "numero_cand",
                "foto_cand",
                "numerosVotos_cand"
            ],
            "Votos": [
                "id_voto",
                "id_cand",
                "id_eleitor",
                "dat_voto"
            ]
        }

        if tabela not in colunas or dado not in colunas[tabela]:
            print("Tabela ou coluna inválida.")
            return None

        conexao = self.conectar()

        if conexao is None:
            return None

        cursor = None

        try:
            cursor = conexao.cursor()

            sql = (
                f"SELECT * FROM `{tabela}` "
                f"WHERE `{dado}` LIKE %s"
            )

            cursor.execute(sql, (f"%{valor}%",))

            resultado = cursor.fetchall()

            return resultado

        except mysql.connector.Error as erro:
            print(f"Erro ao pesquisar: {erro}")
            return None

        finally:
            if cursor is not None:
                cursor.close()

            self.fechar()

    # ===== Método inserir Eleitores =====
    def inserirEleitores(
        self, rm, nome, sobrenome, idade, foto, curso
    ):
        conexao = self.conectar()

        if conexao is None:
            return False

        cursor = None

        try:
            cursor = conexao.cursor()

            sql = """
                INSERT INTO Eleitores
                (
                    rm_eleitor,
                    nome_eleitor,
                    sobreN_eleitor,
                    idade_eleitor,
                    foto_eleitor,
                    curso_eleitor
                )
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            valores = (
                rm, nome, sobrenome, idade, foto, curso
            )

            cursor.execute(sql, valores)
            conexao.commit()

            print("Eleitor cadastrado com sucesso!")
            return True

        except mysql.connector.Error as erro:
            conexao.rollback()
            print(f"Erro ao inserir eleitor: {erro}")
            return False

        finally:
            if cursor is not None:
                cursor.close()

            self.fechar()

    # ===== Método inserir Candidatos =====
    def inserirCandidato(
        self, idEleitor, nomeCandidato,
        numeroCandidato, fotoCandidato
    ):
        conexao = self.conectar()

        if conexao is None:
            return False

        cursor = None

        try:
            cursor = conexao.cursor()

            sql = """
                INSERT INTO Candidatos
                (
                    id_eleitor,
                    nome_cand,
                    numero_cand,
                    foto_cand
                )
                VALUES (%s, %s, %s, %s)
            """

            valores = (
                idEleitor,
                nomeCandidato,
                numeroCandidato,
                fotoCandidato
            )

            cursor.execute(sql, valores)
            conexao.commit()

            print("Candidato cadastrado com sucesso!")
            return True

        except mysql.connector.Error as erro:
            conexao.rollback()
            print(f"Erro ao inserir candidato: {erro}")
            return False

        finally:
            if cursor is not None:
                cursor.close()

            self.fechar()

    # ===== Método inserir Votos =====
    def inserirVotos(self, idCand, idEleitor):
        conexao = self.conectar()

        if conexao is None:
            return False

        cursor = None

        try:
            cursor = conexao.cursor()

            sql = """
                INSERT INTO Votos
                (id_cand, id_eleitor, dat_voto)
                VALUES (%s, %s, CURDATE())
            """

            valores = (idCand, idEleitor)

            # verificação para ver se o Eleitor já votou antes
            
            cursor.execute(
                "SELECT id_voto FROM Votos WHERE id_eleitor = %s",
                (idEleitor,))

            votoExistente = cursor.fetchone()

            if votoExistente:
                print("Eleitor já votou!")
                return False
            
            cursor.execute(sql, valores)
            conexao.commit()

            print("Voto computado com sucesso!")
            return True

        except mysql.connector.Error as erro:
            conexao.rollback()
            print(f"Erro ao inserir voto: {erro}")
            return False

        finally:
            if cursor is not None:
                cursor.close()

            self.fechar()
