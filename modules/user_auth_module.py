import modules.db_module
import logging

def verify_login(username, password):
    """
    A user login verification function.
    :param user: user object of the User module.
    :param conn: database connection.
    :returns: True if user is existed, false otherwise. 
    """
    conn = modules.db_module.create_connection()
    cur = conn.cursor()

    try:
        cur.execute('select * from users where username=?',(username,))
        exists = cur.fetchone()
        if exists == None:
            cur.close()
            return False
        else:
            cur.execute('SELECT password FROM users WHERE username =?;', (username,))
            result = cur.fetchone()
    except conn.Error as err:
        print(err)
        return False
    
    cur.close()
    
    if result[0] == password:
        return True
    else:
        return False


def register_user(user):
    """
    This function register an account for the user.
    :param user: user object of the user module.
    :param conn: database connection.
    :returns: True if user is successfuly registered, false otherwise. 
    """
    conn = modules.db_module.create_connection()
    cur = conn.cursor()

    try:
        cur.execute('insert into users(username, password, email, role) values(?,?,?,?);',(user.username,
        user.password, user.email, user.role,))
        conn.commit()
        cur.close()
        return True

    except conn.Error as err:
        print(err)
        return False
