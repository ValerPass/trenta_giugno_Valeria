from database.DB_connect import DBConnect
from model.gene import Gene


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getLocalizzazioni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT distinct Localization 
                    FROM classification
                    """
            cursor.execute(query)
            for row in cursor:
                result.append(row["Localization"])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getArchi():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT c.Localization as l1, c2.Localization as l2
                    FROM interactions i, classification c , classification c2 
                    WHERE i.GeneID1 = c2.GeneID and i.GeneID2 = c.GeneID
                    and c.Localization != c2.Localization
                            """
            cursor.execute(query)
            for row in cursor:
                result.append((row["l1"], row["l2"]))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getPesi(n1, n2):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT count(distinct (i.`Type`)) as peso
FROM genes g, genes g2, interactions i, classification c1, classification c2
WHERE ((g.GeneID = i.GeneID1 and g2.GeneID = i.GeneID2)
or (g2.GeneID = i.GeneID1 and g.GeneID = i.GeneID2))
and c1.GeneID = g.GeneID and c2.GeneID = g2.GeneID and c1.Localization = %s and c2.Localization = %s
                        """
            cursor.execute(query, (n1,n2))
            for row in cursor:
                result.append(row["peso"])
            cursor.close()
            cnx.close()
            return result








