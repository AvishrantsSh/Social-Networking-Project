from django.db import connection
from backend.queries import CHECK_SESSION_QUERY
import hashlib
import hmac
import os


def hash_password(password: str):
    """
    Hash the provided password with a randomly-generated salt and return the
    salt and hash to store in the database.
    """
    salt = os.urandom(16)
    pw_hash = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
    return [salt.hex(), pw_hash.hex()]


def check_password(salt, pw_hash, password: str) -> bool:
    """
    Given a previously-stored salt and hash, and a password provided by a user
    trying to log in, check whether the password is correct.
    """
    return hmac.compare_digest(
        pw_hash, hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
    )


def runquery(query, params=None):
    with connection.cursor() as cursor:
        try:
            cursor.execute(query, params)
        except Exception as e:
            return None, str(e)

        return cursor.fetchall(), None


def is_login(request):
    if "sessionID" in request.session:
        session_id = request.session["sessionID"]
        result, error = runquery(CHECK_SESSION_QUERY, [session_id])
        if not result:
            return False
        if error:
            raise (error)
        return True

    return False
