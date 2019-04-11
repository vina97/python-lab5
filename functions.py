


import pymysql



def showTasks():
    sql = "SELECT  *  FROM task ORDER BY todo"
    conn = pymysql.connect(user='root', password='MarcoVinai97', host='localhost', database='task')
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return res


def newTask(elem):
    sql = "INSERT INTO task (todo) values (%s)"
    conn = pymysql.connect(user='root', password='MarcoVinai97', host='localhost', database='task')
    cursor = conn.cursor()
    cursor.execute(sql, (elem,))
    cursor.close()
    conn.commit()
    conn.close()


def removeTask(id_elem):
    sql = "DELETE FROM task WHERE id = %s"
    conn = pymysql.connect(user='root', password='MarcoVinai97', host='localhost', database='task')
    cursor = conn.cursor()
    cursor.execute(sql, (id_elem,))
    cursor.close()
    conn.commit()
    conn.close()

