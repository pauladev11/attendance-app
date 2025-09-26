from django.contrib.auth.decorators import user_passes_test

def admin_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_superuser)(view_func)
    return decorated_view_func

def manager_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.manager)(view_func)
    return decorated_view_func
