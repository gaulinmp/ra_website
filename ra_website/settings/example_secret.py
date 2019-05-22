# -*- coding: utf-8 -*-
# Don't check this into version control.

# Email config for sending
DEFAULT_FROM_EMAIL = 'web@example.com'
EMAIL_HOST = 'mail.example.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'web@example.com'
EMAIL_HOST_PASSWORD = 'youremailpassword_seewhywedontcheckthisin?'
EMAIL_USE_SSL = True

SECRET_KEY = 'yoursecretkey_againdontcheckthisin'

# Your google analytics IDs
GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-XXXXXXXX-X'
GOOGLE_ANALYTICS_DOMAIN = 'example.com'

# Extra site info
ADMINS = (
    ('Mac Gaulin', 'admin@example.com'),
)

MANAGERS = ADMINS
