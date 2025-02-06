import mariadb
import sys
import os

def getConnection():
    try:
        conn = mariadb.connect(
            user="knzoonApp",
            password=os.environ['DB_USER_PASSWORD'],
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
    cur.execute("select last_time, last_zone_id from external_feed_read where id = ?", (feedid,))

    for (last_time, last_zone_id) in cur:
        pass
    return (last_time, last_zone_id)

def insertTakever(conn, zoneId, takeoverTime, feedItemAsString):
    cur = conn.cursor()
    sql = "insert into improved_feed_item (zone_id, takeover_time, original_takeover) values (?, ?, ?)"
    cur.execute(sql, (zoneId, takeoverTime, feedItemAsString))

def updateLatestReadInfo(conn, lastTime, lastZoneId):
    cur = conn.cursor()
    sql = "update external_feed_read set last_time = ?, last_zone_id = ? where id = 1"
    cur.execute(sql, (lastTime, lastZoneId))
