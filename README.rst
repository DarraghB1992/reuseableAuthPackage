===== Auth =====
Auth is a reusable authorization app for Django
Detailed documentation is in the "docs" directory.
Quick start -----------
1. Add "reusable_auth" to your INSTALLED_APPS setting like this::
    INSTALLED_APPS = (         ...         'reusable_blog',     )


2. Add these two settings to your projects settings.py:
    AUTH_USER_MODEL = 'accounts.User'
    AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend', 'accounts.backends.EmailAuth',)


3. Run `python manage.py migrate`.


4. Visit http://127.0.0.1:8000/blogs/ to view the blogs you create