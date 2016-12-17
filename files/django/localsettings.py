# List of all stock Django settings:
#       https://docs.djangoproject.com/en/1.10/ref/settings/
#
# Mandatory settings from Django: SECRET_KEY, STATIC_ROOT, MEDIA_ROOT, DEFAULT_FROM_EMAIL
# Mandatory settings used by this HP: XMPP_HOSTS, CONTACT_ADDRESS, DEFAULT_XMPP_HOST

import os
import re

from datetime import timedelta
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

###############################
# Normal Django configuration #
###############################

# Database configuration
# See also: https://docs.djangoproject.com/en/1.10/ref/databases/
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'homepage',
        'USER': 'django',
        'PASSWORD': 'PutYourPasswordHere',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
}

# Admins that get tracebacks
ADMINS = (
    ('Philipp Hübner', 'philipp.huebner@rwth-aachen.de'),
)

# Hostnames that this page runs under
# Note that if not set, the hostnames from XMPP_HOSTS will be used.
ALLOWED_HOSTS = (
    'jabber.rwth-aachen.de', 'www.jabber.rwth-aachen.de', 'upload.jabber.rwth-aachen.de', 'jabber-dev.itc.rwth-aachen.de',
)

# Static and media files configuration
STATIC_ROOT = '/srv/www/jabber.rwth-aachen.de/static/'
MEDIA_ROOT = '/srv/www/upload.jabber.rwth-aachen.de/'
MEDIA_URL = 'https://upload.jabber.rwth-aachen.de/'

# Set this to True during development
DEBUG = False

# Set this to something long and unique
SECRET_KEY = 'whatever'

#########################
# General configuration #
#########################

# The copyright notice at the bottom of the page. "%(year)s is replaced with the current year, and
# "%(brand)s" is replaced with the "BRAND" key of the current site.
#COPYRIGHT_NOTICE = _('© %(year)s, %(brand)s.')
COPYRIGHT_NOTICE = _('© %(year)s, RWTH Aachen University.')

MIN_USERNAME_LENGTH = 5
MAX_USERNAME_LENGTH = 32

# Require a unique email address. By default an address can be used by multiple accounts.
REQUIRE_UNIQUE_EMAIL = True

##########
# Caches #
##########
# See also: https://docs.djangoproject.com/en/dev/topics/cache/

# Django uses an in-memory cache by default. In development, it's recommended you use a persistent
# cache because the xmpp_backends.dummy.DummyBackend uses Djangos cache.
#CACHES = {
#    "default": {
#        "BACKEND": "django_redis.cache.RedisCache",
#        "LOCATION": "redis://127.0.0.1:6379/1",
#
#        # Use this in development, that way users don't disappear from the "backend" (which is just
#        # this redis cache).
#        #"TIMEOUT": None,  # never expire
#        "OPTIONS": {
#            "CLIENT_CLASS": "django_redis.client.DefaultClient",
#        },
#    },
#}

##################
# Email settings #
##################

# Email settings (see Django docs for all options)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False

###########
# Logging #
###########

# The log format used. Note that Celery also has more specific settings below.
#LOG_FORMAT = '[%(asctime).19s %(levelname)-8s] %(message)s' # .19s = only first 19 chars

# Log level used for our own code
LOG_LEVEL = 'INFO'

# Log level used for any library code
LIBRARY_LOG_LEVEL = 'WARN'

############################
# XMPP hosts configuration #
############################

# Connection to the XMPP server.
XMPP_BACKENDS = {
    'default': {
        'BACKEND': 'xmpp_backends.ejabberd_xmlrpc.EjabberdXMLRPCBackend',
        'uri': 'http://localhost:4560',
        'user': 'admin',
        'server': 'jabber.rwth-aachen.de',
        'password': 'PutYourPasswordHere',
    },
}

# Hosts handled by this domain (used in registration form etc.)
XMPP_HOSTS = {
    'jabber.rwth-aachen.de': {
        # A list of hostnames where this host configuration should be used. If a request does not
        # match any host, the host named in DEFAULT_XMPP_HOST will be used. The setting is the same
        # as Djangos global "ALLOWED_HOSTS" setting. Set an empty list if the site is not served by
        # any domain (e.g. where we don't allow registration anyway).
        'ALLOWED_HOSTS': [
            'jabber.rwth-aachen.de',
        ],

        # The "brand name" of this site, used in various user interface elements. The default is
        # the domain name.
        'BRAND': 'jabber.rwth-aachen.de',

        # The base URL used for creating absolute links. The default is https://<hostname>.
        #CANONICAL_BASE_URL='https://jabber.rwth-aachen.de',

        # The "Form" address used in confirmation emails and by the contact form. If not set, the
        # global DEFAULT_FROM_EMAIL setting will be used.
        'DEFAULT_FROM_EMAIL': 'noreply@jabber.rwth-aachen.de',

        # Where the contact form sends emails to. If not set, the global CONTACT_ADDRESS setting
        # will be used.
        'CONTACT_ADDRESS': 'jabber@rwth-aachen.de',

        # Set to False to disable registration for this host. The host will still be usable e.g. in
        # "reset password" forms, but not in the registration form.
        'REGISTRATION': True,

        # Set to true if a user could use an email address from this domain for registration
        'ALLOW_EMAIL': False,

        # GPG fingerprint of the key used for signing encrypted messages. The fingerprint listed
        # here must exist in GPG_KEYDIR with the name "<fingerprint>.key".
        'GPG_FINGERPRINT': 'PutYourKeyHere',  # Used for signing, no 0x prefix!

        # GPG fingerprints (without 0x prefix) of the recipients of the contact address. If this is
        # set, contact emails are encrypted if the user has a GPG key configured (and is logged
        # in, obiously). Public keys listed here must exist in GPG_KEYDIR with the name
        # <fingerprint>.pub.
        #CONTACT_GPG_FINGERPRINTS = [
        #    '...',
        #],
    },
}

# Default address the contact form sends emails to.
CONTACT_ADDRESS = 'jabber@rwth-aachen.de'

# If set, the contact form will name this MUC as primary contact address.
CONTACT_MUC = 'jabber@muc.jabber.rwth-aachen.de'

# Default email used when a host in XMPP_HOSTS does not define one.
DEFAULT_FROM_EMAIL = 'noreply@jabber.rwth-aachen.de'

# The default host used on this site. This affects the default selection in some <select> HTML form
# elements, as well as for content that should be the same accross all hosts, e.g. the canonical
# URL of a blog post.
DEFAULT_XMPP_HOST = 'jabber.rwth-aachen.de'

################
# Social media #
################
# Various social media accounts
#FACEBOOK_PAGE = 'RWTHAachenUniversity'
#TWITTER_HANDLE = 'RWTH'

########################
# Celery configuration #
########################
# See also: http://docs.celeryproject.org/en/latest/configuration.html

CELERY_BROKER_URL = 'redis://localhost:6379/0'

# The log format used by the celery loggers. If None (the default), the same as LOG_FORMAT will be
# used.
#CELERYD_LOG_FORMAT = None

# The format used for Celery task loggers (-> get_task_logger()). The default is the same as the
# normal default, except that the task name is added.
#CELERYD_TASK_LOG_FORMAT = '[%(asctime).19s %(levelname)-8s] [%(task_name)s] %(message)s'

######################
# Anti-Spam settings #
######################

# CAPTCHAs
ENABLE_CAPTCHAS = True
CAPTCHA_LENGTH = 8
CAPTCHA_FONT_SIZE = 32

# DNS-based Blackhole List
# IPs that are on one of these DNSBLs are not allowed to use views that use core.views.DnsBlMixin.
DNSBL = (
    'sbl.spamhaus.org',
    'xbl.spamhaus.org',
    'proxies.dnsbl.sorbs.net',
    'spam.abuse.ch',
    'cbl.abuseat.org',
)

# A manually maintained list of IP addresses or networks that are blocked. Used by the
# BlocklistMixin.
#SPAM_BLACKLIST = {
#    '192.0.2.0',  # You can use IP addresses...
#    '192.0.0.0/28',  # ... or network ranges
#}

# Ratelimits
# Enforce a rate limit per IP for views that use core.views.RateLimitMixin. Use one of the
# constants in core.constants.ACTIVITY_*.
#
#RATELIMIT_CONFIG = {
#    ACTIVITY_REGISTER: (
#        (timedelta(hours=1), 5, ),
#    ),
#    ACTIVITY_FAILED_LOGIN: (
#        (timedelta(minutes=30), 3, ),
#    ),
#}

# Domains that cannot be used for registration because they are used for SPAM
BANNED_EMAIL_DOMAINS = {'spam.com', 'spam.net', }

# Do not allow registrations using email addresses matching any of the given regular expressions.
# If you just want to match a specific domain, please use BANNED_EMAIL_DOMAINS instead, it will
# display a more specific error message and the check is a lot faster.
#EMAIL_BLACKLIST = (
#    re.compile('^[a-z]@'),  # one-letter email addresses are mean for some reason ;-)
#)

# If set, only allow registrations if the users email address matches any of the listed regular
# expressions. Note that BANNED_EMAIL_DOMAINS and EMAIL_BLACKLIST is checked first.
EMAIL_WHITELIST = (
    re.compile('rwth-aachen\.de$'),
    re.compile('fh-aachen\.de$'),
    re.compile('katho-nrw\.de$'),
)

#####################
# GPG configuration #
#####################

# GPG keyserver used for fetching keys
GPG_KEYSERVER = 'http://pool.sks-keyservers.net:11371'

# Location of the *private* key files used for signing GPG emails. This directory is expected
# to contain the private keys configured in the GPG_FINGERPRINT setting in XMPP_HOSTS. The name
# of the files should be <fingerprint>.key.
GPG_KEYDIR = '/srv/django/gnupg'

# Custom GPG backend.
# NOTE: The backend here is never used verbatim in production. All public keys for users come from
#       the database, private keys come from the filesystem (see GPG_KEYDIR). Every GPG operation
#       is done in a separate keyring that is deleted after use. This is done to (a) isolate users
#       from each other and (b) because of various threading issues with GPG.
#
#GPG_BACKENDS = {
#    'default': {
#        'BACKEND': 'gpgmime.gpgme.GpgMeBackend',
#        'HOME': os.path.join(ROOT_DIR, 'gnupg'),
#        # Optional settings:
#        'PATH': '/home/...',  # Path to 'gpg' binary
#        'ALWAYS_TRUST': True,   # Ignore trust in all operations
#        'OPTIONS': {...},  # Any custom options for the specific backend implementation
#    },
#}

####################
# Privacy settings #
####################

# When UserLogEntry records are deleted. These are log entries in the "Recent activity" tab of
# the user.
USER_LOGENTRY_EXPIRES = timedelta(days=31)

##############################
# XEP-0363: HTTP File Upload #
##############################
# See also: https://github.com/mathiasertl/django-xmpp-http-upload

XMPP_HTTP_UPLOAD_ACCESS = (
    # This user has no limits
    ('^philipp.huebner@jabber\.rwth-aachen\.de$', {}),
    # Users on these domains have more explicit limits
    ('@jabber\.rwth-aachen\.de$' , {
      # User may not upload a file larger then 30MB
      # should match max_size setting in ejabberd.yml
      'max_file_size': 30 * 1024 * 1024,

      # User may not upload more then 150 MB in total
      'max_total_size': 150 * 1024 * 1024,

      # User may not upload more then 50 MB per hour
      'bytes_per_timedelta': {
          'delta': timedelta(hours=1),
          'bytes': 100 * 1024 * 1024,
      },

      # User may not do more then 30 uploads per hour
      'uploads_per_timedelta': {
          'delta': timedelta(hours=1),
          'uploads': 30,
      },
  }),
)

# How long files are shared before they are deleted:
XMPP_HTTP_UPLOAD_SHARE_TIMEOUT = 86400 * 31

# Top-level domain to use
XMPP_HTTP_UPLOAD_URL_BASE = 'https://jabber.rwth-aachen.de'
