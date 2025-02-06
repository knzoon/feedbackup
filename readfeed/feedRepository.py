import mariadb
import sys
import os


def get_connection():
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


def get_latest_read_info(conn):
    cur = conn.cursor()
    feed_id = 1
    cur.execute("select last_time, last_zone_id from external_feed_read where id = ?", (feed_id,))

    for (last_time, last_zone_id) in cur:
        pass
    return (last_time, last_zone_id)


def insert_takeover(conn, zone_id, takeover_time, feed_item_as_string):
    cur = conn.cursor()
    sql = "insert into improved_feed_item (zone_id, takeover_time, original_takeover) values (?, ?, ?)"
    cur.execute(sql, (zone_id, takeover_time, feed_item_as_string))


def update_latest_read_info(conn, last_time, last_zone_id):
    cur = conn.cursor()
    sql = "update external_feed_read set last_time = ?, last_zone_id = ? where id = 1"
    cur.execute(sql, (last_time, last_zone_id))
