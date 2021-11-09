from uuid import uuid4

from django.db import connection
from django.shortcuts import redirect, render
from django.urls import reverse

cursor = connection.cursor()


def runquery(query):
    try:
        cursor.execute(query)
    except Exception as e:
        return None, str(e)

    return cursor.fetchall(), None


def is_login(request):
    if "sessionID" in request.session:
        session_id = request.session["sessionID"]
        query = f"SELECT * FROM backend_session WHERE session_id = '{session_id}' and login_status=True"
        result, error = runquery(query)
        if error or not result:
            return False
        return True
    return False


def HomeView(request):
    return render(request, "index.html", {"is_login": is_login(request)})


def LoginView(request):
    template_name = "registration/login.html"
    if is_login(request):
        return redirect(reverse("home"))

    if request.method == "POST":
        user_email = request.POST.get("user_email")
        password = request.POST.get("password")
        query = (
            "SELECT * FROM backend_users WHERE user_email = '%s' AND password = '%s'"
            % (user_email, password)
        )
        result, error = runquery(query)
        if error or not result:
            return render(
                request, template_name, {"error": "Invalid username or password"}
            )

        if result:
            session_id = uuid4()
            query = f"INSERT INTO backend_session (session_id, user_id_id, login_status) VALUES ('{str(session_id)}', '{result[0][0]}', 1)"
            _, error = runquery(query)
            if error:
                return render(request, template_name, {"error": error})

            request.session["sessionID"] = str(session_id)
            return render(
                request,
                "index.html",
                {"message": "Login Successful!", "is_login": is_login(request)},
            )

    return render(request, template_name)


def LogoutView(request):
    if is_login(request):
        session_id = request.session["sessionID"]
        query = f"UPDATE backend_session SET login_status=False WHERE session_id = '{session_id}'"
        _, error = runquery(query)
        if error:
            return redirect(reverse("home", args={"message": error}))

        del request.session["sessionID"]
        return redirect(reverse("home"))

    else:
        return redirect(reverse("home"))
