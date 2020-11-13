import modules.db_module as db
from modules.plan_module import Plan
from modules.resource_module import Resource

def fetch_plan_info(p):
    """
    This functions searchs for a plan in the database and
    returns its information in a list of Plan objects.
    :param p: plan name.
    :returns list: list of Plan objects.
    """
    conn = db.create_connection()
    cur = conn.cursor()
    plan = []
    cur.execute("select * from learning_plans where name = ?;",(p,))
    result = cur.fetchall()

    for row in result:
        plan.append(Plan(row[0],row[1],row[2],row[3],row[4],row[5]))

    cur.close()

    return plan

def select_plan(user, plan_id):
    """
    This function add a plan to the user list of plans.
    :param user: an object of User module.
    :param plan_id: the plan id.
    :returns bool: True if successfully added, False otherwise.
    """
    user_id = get_user_id(user)
    plan_id = int(plan_id)
    conn = db.create_connection()
    cur = conn.cursor()

    if user_id > 0:
        try:
            cur.execute("insert into user_plan values(?,?);",(user_id, plan_id,))

            conn.commit()
            cur.close()
            return True
        
        except conn.Error as err:
            
            print(err)
            cur.close()
            return False
            
    else:
        return False

def get_user_id(username):
    """
    This functions gets the user ID from the database.
    :param username: the desired username to get his ID.
    :returns int: the uesr ID.
    """

    conn = db.create_connection()
    cur = conn.cursor()

    cur.execute("select user_id from users where username = ?;",(username,))
    result = cur.fetchone()
    
    if result is None:
        return 0
    else:
        return int(''.join(map(str, result)))
    
    cur.close()

def get_user_plans(username):
    """
    This function return the current user plans.
    :param username: the desired user to get his list of plans.
    :returns list: a list of current user plans.
    """
    user_plans = []
    conn = db.create_connection()
    cur = conn.cursor()

    try:

        cur.execute("select learning_plans.* from learning_plans join user_plan,users "
        +"on user_plan.user_id = users.user_id and user_plan.plan_id = learning_plans.plan_id"
        +" where username = ?",(username,))
        result = cur.fetchall()

        
        for row in result:
            user_plans.append(Plan(row[0],row[1],row[2],row[3],row[4],row[5]))

        cur.close()
        return user_plans
    except conn.Error as err:
        print(err)
        return

def get_resources_list(plan_id):
    """
    This function gets a list of resources under the current plan.
    :param plan_id: the desired plan to get its list of resources.
    :returns: a list of plan resources.
    """
    resources = []
    conn = db.create_connection()
    cur = conn.cursor()
    try:
        cur.execute("select learning_resources.* from learning_resources join"
        +" learning_plans,plan_resource on plan_resource.plan_id=learning_plans.plan_id "
        +"and plan_resource.resource_id=learning_resources.resource_id where learning_plans.plan_id"
        +" = ?;",(plan_id,))
        result = cur.fetchall()

        for row in result:
            resources.append(Resource(row[0],row[1],row[2],row[3]))
        
        cur.close()
        return resources
    except conn.Error as err:
        print(err)
        return

def mark_plan_complete(plan_id, user_id):
    """
    This function removes a given plan for a given user as completed.
    :param plan_id: the desired plan ID.
    :param user_id: the desired user ID.
    :returns bool: True if successfully removed, False otherwise.
    """
    conn = db.create_connection()
    cur = conn.cursor()

    try:
        cur.execute("delete from user_plan where user_id = ? and plan_id = ?;",(user_id, plan_id
        ,))
        conn.commit()
        cur.close()
        return True
    except conn.Error as err:
        print(err)
        return False