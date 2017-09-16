from django.http import HttpResponseRedirect


def if_login(view):
    def new_view(request, *args, **kwargs):
        if not 'id' in request.session :
            return HttpResponseRedirect('/user/login/')
        return view(request, *args, **kwargs)
    return new_view