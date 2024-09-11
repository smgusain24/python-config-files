from config.app_logger import logger
import MySQLdb


host_val = 'HOST_VAL' # Hostname
user_val = 'USER_VAL' # Username
pass_val = 'PASS_VAL' # Password
db_val = 'DB_VAL' # Database name


def execute_read_query(query, params=None, cursor=None):
    try:
        database_connection = MySQLdb.connect(host=host_val, user=user_val, passwd=pass_val, db=db_val)
        logger.info(f"Executing: {query}, {params}")
        if cursor == "dict":
            cursor = database_connection.cursor(MySQLdb.cursors.DictCursor)
        else:
            cursor = database_connection.cursor()
        if params is not None:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        database_connection.close()
        return result
    except Exception as e:
        logger.error(f"Error executing read query: {e}", exc_info=True)
        return ()


def execute_insert_query(query, params=None):
    try:
        database_connection = MySQLdb.connect(host=host_val, user=user_val, passwd=pass_val, db=db_val)
        logger.info(f"Executing: {query}, {params}")
        cursor = database_connection.cursor()
        if params is not None:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        database_connection.commit()

        last_insert_id = cursor.lastrowid
        cursor.close()
        database_connection.close()
        return last_insert_id
    except Exception as e:
        logger.error(f"Error executing insert query: {e}", exc_info=True)
        return None


def execute_insert_many_query(query, params=None):
    try:
        database_connection = MySQLdb.connect(host=host_val, user=user_val, passwd=pass_val, db=db_val)
        logger.info(f"Executing: {query}, {params}")
        cursor = database_connection.cursor()
        if params is not None:
            cursor.executemany(query, params)
        else:
            cursor.execute(query)
        database_connection.commit()

        last_insert_id = cursor.lastrowid
        cursor.close()
        database_connection.close()
        return last_insert_id
    except Exception as e:
        logger.error(f"Error executing insert query: {e}", exc_info=True)
        return None


def execute_update_query(query, params=None):
    try:
        database_connection = MySQLdb.connect(host=host_val, user=user_val, passwd=pass_val, db=db_val)
        logger.info(f"Executing: {query}, {params}")
        cursor = database_connection.cursor()
        if params is not None:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        database_connection.commit()
        cursor.close()
        database_connection.close()
        return True
    except Exception as e:
        logger.error(f"Error executing update query: {e}", exc_info=True)
        return False


def execute_update_many_query(query, params=None):
    try:
        database_connection = MySQLdb.connect(host=host_val, user=user_val, passwd=pass_val, db=db_val)
        logger.info(f"Executing: {query}, {params}")
        cursor = database_connection.cursor()
        if params is not None:
           cursor.executemany(query, params)
        else:
           cursor.execute(query)
        database_connection.commit()
        cursor.close()
        database_connection.close()
        return True
    except Exception as e:
        logger.error(f"Error executing update query: {e}")
        return False


def execute_delete_query(query, params=None):
    try:
        database_connection = MySQLdb.connect(host=host_val, user=user_val, passwd=pass_val, db=db_val)
        logger.info(f"Executing: {query}, {params}")
        cursor = database_connection.cursor()
        if params is not None:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        database_connection.commit()
        cursor.close()
        database_connection.close()
        return True
    except Exception as e:
        logger.error(f"Error executing delete query: {e}", exc_info=True)


