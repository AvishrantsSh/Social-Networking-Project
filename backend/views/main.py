from django.shortcuts import render

from backend.queries import *
from backend.utils import is_login, runquery


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
    return render(request, "add_post.html", {"is_login": is_login(request)})
