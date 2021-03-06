from functools import wraps
from flask_login import current_user
from flask import abort, render_template, current_app, flash


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.role_id not in permission:
                flash('ACL error!', 'danger')
                return render_template("status_code/403.html")
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def engineer_required(f):
    return permission_required(['engineer', 'admin'])(f)


def manager_required(f):
    return permission_required(['manager', 'admin'])(f)


def admin_required(f):
    return permission_required(['admin'])(f)
