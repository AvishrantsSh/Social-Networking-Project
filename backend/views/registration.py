from django.shortcuts import redirect, render
from django.urls import reverse
from uuid import uuid4
from backend.queries import (
    CREATE_NEW_SESSION_QUERY,
    CREATE_NEW_USER_QUERY,
    GET_USER_INSTANCE_QUERY,
)

from backend.utils import check_password, hash_password, is_login, runquery


def LoginView(request):
    template_name = "registration/login.html"
    if is_login(request):
        return redirect(reverse("home"))

    if request.method == "POST":
        user_email = request.POST.get("user_email")
        password = request.POST.get("password")
        result, error = runquery(GET_USER_INSTANCE_QUERY, [user_email])
        if error or not result:
            return render(request, template_name, {"error": "Invalid credentials"})

        salt, hash = result[0][1].split("$$")
        if check_password(bytes.fromhex(salt), bytes.fromhex(hash), password):
            session_id = uuid4()
            _, error = runquery(
                CREATE_NEW_SESSION_QUERY, [str(session_id), result[0][0]]
            )
            if error:
                return render(request, template_name, {"error": error})

            request.session["sessionID"] = str(session_id)
            return redirect(reverse("home"))
        else:
            return render(request, template_name, {"error": "Invalid credentials"})

    return render(request, template_name)


def LogoutView(request):
    if is_login(request):
        session_id = request.session["sessionID"]
        query = f"UPDATE backend_session SET login_status=0 WHERE session_id = '{session_id}'"
        _, error = runquery(query)
        if error:
            raise (error)

        del request.session["sessionID"]
        return redirect(reverse("home"))

    else:
        return redirect(reverse("home"))


def SignUpView(request):
    template_name = "registration/signup.html"
    if is_login(request):
        return redirect(reverse("home"))

    if request.method == "POST":
        user_id = str(uuid4())
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        user_email = request.POST.get("user_email")
        password = request.POST.get("password")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")

        password = "$$".join(hash_password(password))
        _, error = runquery(
            CREATE_NEW_USER_QUERY,
            [user_id, user_email, password, f_name, l_name, dob, gender],
        )
        if error:
            if error[:6] == "UNIQUE":
                return render(request, template_name, {"error": "User Already Exists"})
            return render(request, template_name, {"error": str(error)})

        session_id = uuid4()
        _, error = runquery(CREATE_NEW_SESSION_QUERY, [str(session_id), user_id])
        if error:
            raise error

        request.session["sessionID"] = str(session_id)
        return redirect(
            reverse("home"),
        )

    return render(request, template_name)
