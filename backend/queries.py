CHECK_SESSION_QUERY = (
    "SELECT user_id_id FROM backend_session WHERE session_id = %s and login_status=1"
)
GET_TOP_POSTS_QUERY = "SELECT user_id_id, content from backend_posts LIMIT %s"
GET_USER_INFO_FROM_ID_QUERY = "SELECT first_name FROM backend_users WHERE user_id = %s"
GET_USER_INSTANCE_QUERY = (
    "SELECT user_id, password FROM backend_users WHERE user_email = %s"
)
CREATE_NEW_SESSION_QUERY = "INSERT INTO backend_session (session_id, user_id_id, login_status) VALUES (%s, %s, 1)"
CREATE_NEW_USER_QUERY = "INSERT INTO backend_users (user_id, user_email, password, first_name, last_name, birth_date, gender) VALUES (%s, %s, %s, %s, %s, %s, %s)"
CREATE_NEW_POST = "INSERT INTO backend_posts (post_id, user_id_id, content, timestamp, likes, shares) VALUES (%s, %s, %s, %s, 0, 0)"
