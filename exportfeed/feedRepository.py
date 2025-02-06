from datetime import datetime
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


def read_feed_from_beginning():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("select takeover_time, original_takeover from improved_feed_item order by takeover_time, zone_id limit 1001")
            return cur.fetchall()


def read_feed_after_specified_time(time: datetime):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("select takeover_time, original_takeover from improved_feed_item where takeover_time > ? order by takeover_time, zone_id limit 1001", (time,))
            return cur.fetchall()
