import mariadb
import sys
import uuid

def getConnection():
    try:
        conn = mariadb.connect(
            user="knzoonApp",
            password="appApa",
            host="database",
            port=3306,
            database="knzoon"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    
    return conn

def getLatestReadInfo(conn):
    cur = conn.cursor()
    feedid = 1
    cur.execute("select last_time, last_zone_id, last_highest_order from external_feed_read where id = ?", (feedid,))

    for (last_time, last_zone_id, last_highest_order) in cur:
        pass
    return (last_time, last_zone_id, last_highest_order)

def insertTakever(conn, newhighestorder, takeoverTime, feedItemAsString):
    cur = conn.cursor()
    sql = "insert into improved_feed_item (id, order_number, takeover_time, original_takeover) values (?, ?, ?, ?)"
    cur.execute(sql, (str(uuid.uuid4()), newhighestorder, takeoverTime, feedItemAsString))

def updateLatestReadInfo(conn, lastTime, lastZoneId, lastHighestOrder):
    cur = conn.cursor()
    sql = "update external_feed_read set last_time = ?, last_zone_id = ?, last_highest_order = ? where id = 1"
    cur.execute(sql, (lastTime, lastZoneId, lastHighestOrder))