from zygoat_django.settings.environment import prod_required_env, DEBUG

SHARED_DOMAIN = prod_required_env("DJANGO_SHARED_DOMAIN", default=None)
CSRF_COOKIE_DOMAIN = (SHARED_DOMAIN,)
CSRF_TRUSTED_ORIGINS = SHARED_DOMAIN and [f".{SHARED_DOMAIN}"]
SESSION_COOKIE_DOMAIN = SHARED_DOMAIN
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_COOKIE_AGE = 3600  # One hour in seconds
CSRF_COOKIE_AGE = SESSION_COOKIE_AGE
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
