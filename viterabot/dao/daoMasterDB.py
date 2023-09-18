import sqlite3

class DaoMasterDB:
    def __init__(self) -> None:
        self.db = "src\\viteiraBot.db"
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self) -> None:
        CreateTable(self)

    def getConn(self) -> sqlite3.Connection:
        return self.conn

    def getCursor(self) -> sqlite3.Cursor:
        return self.cursor
    
    def close(self) -> None:
        self.cursor.close()
        self.conn.close()
    
class CreateTable:
    def __init__(self, dao: DaoMasterDB) -> None:
        self.conn = dao.getConn()
        self.cursor = dao.getCursor()
        self._execute()

    def _execute(self) -> None:
        # Crie a tabela 'template'
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS template (
                id INTEGER PRIMARY KEY,
                src_path TEXT
            )
        ''')

        # Crie a tabela 'coordinates'
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS coordinates (
                id INTEGER PRIMARY KEY,
                x_start REAL,
                y_start REAL,
                x_size REAL,
                y_size REAL,
                rotation REAL
            )
        ''')

        # Crie a tabela 'template_to_coordinates' com chaves estrangeiras
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS template_to_coordinates (
                id_template INTEGER,
                id_coordinate INTEGER,
                FOREIGN KEY (id_template) REFERENCES template (id),
                FOREIGN KEY (id_coordinate) REFERENCES coordinates (id)
            )
        ''')

        # Crie a tabela 'mask'
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS mask (
                id INTEGER PRIMARY KEY,
                src_path TEXT,
                x_start REAL,
                y_start REAL,
                x_size REAL,
                y_size REAL,
                rotation REAL
            )
        ''')

        # Crie a tabela 'mask_to_template' com chaves estrangeiras
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS mask_to_template (
                id_template INTEGER,
                id_mask INTEGER,
                FOREIGN KEY (id_template) REFERENCES template (id),
                FOREIGN KEY (id_mask) REFERENCES mask (id)
            )
        ''')

        # Crie a tabela 'repository'
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS repository (
                id INTEGER PRIMARY KEY,
                src_path TEXT,
                title TEXT
            )
        ''')

        # Crie a tabela 'image'
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS image (
                id INTEGER PRIMARY KEY,
                src_path TEXT,
                title TEXT,
                hash TEXT
            )
        ''')
        
        # Crie a tabela 'post'
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS post (
                id INTEGER PRIMARY KEY,
                id_image INTEGER,
                id_facebook INTEGER,
                discord BOOLEAN,
                published BOOLEAN,
                FOREIGN KEY (id_image) REFERENCES image (id)
            )
        ''')
        # Commit (salve) as alterações
        self.conn.commit()