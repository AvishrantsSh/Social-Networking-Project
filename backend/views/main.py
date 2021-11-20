from django.shortcuts import redirect, render
from django.urls import reverse

from backend.queries import *
from backend.utils import is_login, runquery
from datetime import datetime
from uuid import uuid4


def HomeView(request):
    result, error = runquery(GET_TOP_POSTS_QUERY, [25])
    if error:
        return render(request, "index.html", {"error": error})

    data = []
    for row in result:
        row = list(row)
        user_result, user_error = runquery(GET_USER_INFO_FROM_ID_QUERY, [row[0]])
        if user_error or not user_result:
            return render(request, "index.html", {"error": user_error})
        data.append([user_result[0][0], row[1]])

    return render(request, "index.html", {"is_login": is_login(request), "posts": data})


def AddPostView(request):
    template_name = "add_post.html"
    user = is_login(request)
    if not user:
        return redirect(reverse("login"))

    if request.method == "POST":
        content = request.POST.get("content")
        _, error = runquery(
            CREATE_NEW_POST, [str(uuid4()), user, content, datetime.now()]
        )
        if error:
            return render(request, template_name, {"error": str(error)})
        return redirect(reverse("home"))

    return render(request, template_name, {"is_login": is_login(request)})
