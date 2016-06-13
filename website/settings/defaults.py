# -*- coding: utf-8 -*-
"""
Base settings file, common to all environments.
These settings can be overridden in local.py.
"""

import datetime
import os
import json
import hashlib
from datetime import timedelta

os_env = os.environ


def parent_dir(path):
    '''Return the parent of a directory.'''
    return os.path.abspath(os.path.join(path, os.pardir))

HERE = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = parent_dir(HERE)  # website/ directory
APP_PATH = parent_dir(BASE_PATH)
ADDON_PATH = os.path.join(BASE_PATH, 'addons')
STATIC_FOLDER = os.path.join(BASE_PATH, 'static')
STATIC_URL_PATH = '/static'
ASSET_HASH_PATH = os.path.join(APP_PATH, 'webpack-assets.json')
ROOT = os.path.join(BASE_PATH, '..')
BCRYPT_LOG_ROUNDS = 12

with open(os.path.join(APP_PATH, 'package.json'), 'r') as fobj:
    VERSION = json.load(fobj)['version']

# Hours before email confirmation tokens expire
EMAIL_TOKEN_EXPIRATION = 24
CITATION_STYLES_PATH = os.path.join(BASE_PATH, 'static', 'vendor', 'bower_components', 'styles')

# Minimum seconds between forgot password email attempts
SEND_EMAIL_THROTTLE = 30

# Hours before pending embargo/retraction/registration automatically becomes active
RETRACTION_PENDING_TIME = datetime.timedelta(days=2)
EMBARGO_PENDING_TIME = datetime.timedelta(days=2)
EMBARGO_TERMINATION_PENDING_TIME = datetime.timedelta(days=2)
REGISTRATION_APPROVAL_TIME = datetime.timedelta(days=2)
# Date range for embargo periods
EMBARGO_END_DATE_MIN = datetime.timedelta(days=2)
EMBARGO_END_DATE_MAX = datetime.timedelta(days=1460)  # Four years

LOAD_BALANCER = False
PROXY_ADDRS = []

# May set these to True in local.py for development
DEV_MODE = True
DEBUG_MODE = True

LOG_PATH = os.path.join(APP_PATH, 'logs')
TEMPLATES_PATH = os.path.join(BASE_PATH, 'templates')
ANALYTICS_PATH = os.path.join(BASE_PATH, 'analytics')

CORE_TEMPLATES = os.path.join(BASE_PATH, 'templates/log_templates.mako')
BUILT_TEMPLATES = os.path.join(BASE_PATH, 'templates/_log_templates.mako')

DOMAIN = 'http://mechanysm.com/'
API_DOMAIN = 'http://api.mechanysm.com/'
GNUPG_HOME = os.path.join(BASE_PATH, 'gpg')
GNUPG_BINARY = 'gpg'

# User management & registration
CONFIRM_REGISTRATIONS_BY_EMAIL = True
ALLOW_REGISTRATION = True
ALLOW_LOGIN = True

SEARCH_ENGINE = 'elastic'  # Can be 'elastic', or None
ELASTIC_URI = 'localhost:9200'
ELASTIC_TIMEOUT = 10
ELASTIC_INDEX = 'website'
SHARE_ELASTIC_URI = ELASTIC_URI
SHARE_ELASTIC_INDEX = 'share'
# For old indices
SHARE_ELASTIC_INDEX_TEMPLATE = 'share_v{}'

# Sessions
# TODO: Override OSF_COOKIE_DOMAIN in local.py in production
OSF_COOKIE_DOMAIN = '.mechanysm.com'
COOKIE_NAME = 'osf'
# TODO: Override SECRET_KEY in local.py in production
SECRET_KEY = 'CHANGEME'

# Change if using `scripts/cron.py` to manage crontab
CRON_USER = None

# External services
USE_CDN_FOR_CLIENT_LIBS = True

USE_EMAIL = True
FROM_EMAIL = 'openscienceframework-noreply@osf.io'
SUPPORT_EMAIL = 'support@osf.io'

# SMTP Settings
MAIL_SERVER = 'smtp.sendgrid.org'
MAIL_USERNAME = 'halcyonchimera'
MAIL_PASSWORD = 'codetheworldinto0blivi0n'  # Set this in local.py

# OR, if using Sendgrid's API
SENDGRID_API_KEY = None

# Mailchimp
MAILCHIMP_API_KEY = None
MAILCHIMP_WEBHOOK_SECRET_KEY = 'CHANGEME'  # OSF secret key to ensure webhook is secure
ENABLE_EMAIL_SUBSCRIPTIONS = True
MAILCHIMP_GENERAL_LIST = 'Open Science Framework General'

#Triggered emails
OSF_HELP_LIST = 'Open Science Framework Help'
WAIT_BETWEEN_MAILS = timedelta(days=7)
NO_ADDON_WAIT_TIME = timedelta(weeks=8)
NO_LOGIN_WAIT_TIME = timedelta(weeks=4)
WELCOME_OSF4M_WAIT_TIME = timedelta(weeks=2)
NO_LOGIN_OSF4M_WAIT_TIME = timedelta(weeks=6)
NEW_PUBLIC_PROJECT_WAIT_TIME = timedelta(hours=24)
WELCOME_OSF4M_WAIT_TIME_GRACE = timedelta(days=12)

# TODO: Override in local.py
MAILGUN_API_KEY = None

# TODO: Override in local.py in production
UPLOADS_PATH = os.path.join(BASE_PATH, 'uploads')
MFR_CACHE_PATH = os.path.join(BASE_PATH, 'mfrcache')
MFR_TEMP_PATH = os.path.join(BASE_PATH, 'mfrtemp')

# Use Celery for file rendering
USE_CELERY = True

# Use GnuPG for encryption
USE_GNUPG = True

# File rendering timeout (in ms)
MFR_TIMEOUT = 30000

# TODO: Override in local.py in production
DB_HOST = 'localhost'
DB_PORT = os_env.get('OSF_DB_PORT', 27017)
DB_NAME = 'osf20130903'
DB_USER = None
DB_PASS = None

# Cache settings
SESSION_HISTORY_LENGTH = 5
SESSION_HISTORY_IGNORE_RULES = [
    lambda url: '/static/' in url,
    lambda url: 'favicon' in url,
    lambda url: url.startswith('/api/'),
]

# TODO: Configuration should not change between deploys - this should be dynamic.
CANONICAL_DOMAIN = 'mechanysm.com'
COOKIE_DOMAIN = '.mechanysm.com'  # Beaker
SHORT_DOMAIN = 'mecahnysm.com'

# TODO: Combine Python and JavaScript config
COMMENT_MAXLENGTH = 500

# Profile image options
PROFILE_IMAGE_LARGE = 70
PROFILE_IMAGE_MEDIUM = 40
PROFILE_IMAGE_SMALL = 20

# Conference options
CONFERENCE_MIN_COUNT = 5

WIKI_WHITELIST = {
    'tags': [
        'a', 'abbr', 'acronym', 'b', 'bdo', 'big', 'blockquote', 'br',
        'center', 'cite', 'code',
        'dd', 'del', 'dfn', 'div', 'dl', 'dt', 'em', 'embed', 'font',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img', 'ins',
        'kbd', 'li', 'object', 'ol', 'param', 'pre', 'p', 'q',
        's', 'samp', 'small', 'span', 'strike', 'strong', 'sub', 'sup',
        'table', 'tbody', 'td', 'th', 'thead', 'tr', 'tt', 'ul', 'u',
        'var', 'wbr',
    ],
    'attributes': [
        'align', 'alt', 'border', 'cite', 'class', 'dir',
        'height', 'href', 'id', 'src', 'style', 'title', 'type', 'width',
        'face', 'size', # font tags
        'salign', 'align', 'wmode', 'target',
    ],
    # Styles currently used in Reproducibility Project wiki pages
    'styles' : [
        'top', 'left', 'width', 'height', 'position',
        'background', 'font-size', 'text-align', 'z-index',
        'list-style',
    ]
}

# Add-ons
# Load addons from addons.json
with open(os.path.join(ROOT, 'addons.json')) as fp:
    addon_settings = json.load(fp)
    ADDONS_REQUESTED = addon_settings['addons']
    ADDONS_ARCHIVABLE = addon_settings['addons_archivable']
    ADDONS_COMMENTABLE = addon_settings['addons_commentable']
    ADDONS_BASED_ON_IDS = addon_settings['addons_based_on_ids']

ADDON_CATEGORIES = [
    'documentation',
    'storage',
    'bibliography',
    'other',
    'security',
    'citations',
]

SYSTEM_ADDED_ADDONS = {
    # 'user': ['badges'],
    'user': [],
    'node': [],
}

# Piwik

# TODO: Override in local.py in production
PIWIK_HOST = None
PIWIK_ADMIN_TOKEN = None
PIWIK_SITE_ID = None

KEEN_PROJECT_ID = None
KEEN_WRITE_KEY = None
KEEN_READ_KEY = None

SENTRY_DSN = None
SENTRY_DSN_JS = None


# TODO: Delete me after merging GitLab
MISSING_FILE_NAME = 'untitled'

# Project Organizer
ALL_MY_PROJECTS_ID = '-amp'
ALL_MY_REGISTRATIONS_ID = '-amr'
ALL_MY_PROJECTS_NAME = 'All my projects'
ALL_MY_REGISTRATIONS_NAME = 'All my registrations'

# Most Popular and New and Noteworthy Nodes
POPULAR_LINKS_NODE = None  # TODO Override in local.py in production.
NEW_AND_NOTEWORTHY_LINKS_NODE = None  # TODO Override in local.py in production.

NEW_AND_NOTEWORTHY_CONTRIBUTOR_BLACKLIST = []  # TODO Override in local.py in production.

# FOR EMERGENCIES ONLY: Setting this to True will disable forks, registrations,
# and uploads in order to save disk space.
DISK_SAVING_MODE = False

# Seconds before another notification email can be sent to a contributor when added to a project
CONTRIBUTOR_ADDED_EMAIL_THROTTLE = 24 * 3600

# Google Analytics
GOOGLE_ANALYTICS_ID = None
GOOGLE_SITE_VERIFICATION = None

# Pingdom
PINGDOM_ID = None

DEFAULT_HMAC_SECRET = 'changeme'
DEFAULT_HMAC_ALGORITHM = hashlib.sha256
WATERBUTLER_URL = 'http://wb.mechanysm.com'
WATERBUTLER_ADDRS = ['127.0.0.1']

# Test identifier namespaces
DOI_NAMESPACE = 'doi:10.5072/FK2'
ARK_NAMESPACE = 'ark:99999/fk4'

EZID_USERNAME = 'changeme'
EZID_PASSWORD = 'changeme'
# Format for DOIs and ARKs
EZID_FORMAT = '{namespace}osf.io/{guid}'


USE_SHARE = True
SHARE_REGISTRATION_URL = ''
SHARE_API_DOCS_URL = ''

CAS_SERVER_URL = 'http://accounts.mechanysm.com'
MFR_SERVER_URL = 'http://mfr.mechanysm.com'

###### ARCHIVER ###########
ARCHIVE_PROVIDER = 'osfstorage'

MAX_ARCHIVE_SIZE = 5 * 1024 ** 3  # == math.pow(1024, 3) == 1 GB
MAX_FILE_SIZE = MAX_ARCHIVE_SIZE  # TODO limit file size?

ARCHIVE_TIMEOUT_TIMEDELTA = timedelta(1)  # 24 hours

ENABLE_ARCHIVER = True

JWT_SECRET = 'changeme'
JWT_ALGORITHM = 'HS256'

##### CELERY #####

# Default RabbitMQ broker
BROKER_URL = 'amqp://'

# Default RabbitMQ backend
CELERY_RESULT_BACKEND = 'amqp://'

# Modules to import when celery launches
CELERY_IMPORTS = (
    'framework.celery_tasks',
    'framework.celery_tasks.signals',
    'framework.email.tasks',
    'framework.analytics.tasks',
    'website.mailchimp_utils',
    'website.notifications.tasks',
    'website.archiver.tasks',
    'website.search.search',
    'scripts.populate_new_and_noteworthy_projects',
    'scripts.refresh_box_tokens',
    'scripts.retract_registrations',
    'scripts.embargo_registrations',
    'scripts.approve_registrations',
    'scripts.approve_embargo_terminations',
    'scripts.triggered_mails',
    'scripts.send_queued_mails',
)

# Modules that need metrics and release requirements
# CELERY_IMPORTS += (
#     'scripts.osfstorage.glacier_inventory',
#     'scripts.osfstorage.glacier_audit',
#     'scripts.osfstorage.usage_audit',
#     'scripts.osfstorage.files_audit',
#     'scripts.analytics.tasks',
#     'scripts.analytics.upload',
# )

# celery.schedule will not be installed when running invoke requirements the first time.
try:
    from celery.schedules import crontab
except ImportError:
    pass
else:
    #  Setting up a scheduler, essentially replaces an independent cron job
    CELERYBEAT_SCHEDULE = {
        '5-minute-emails': {
            'task': 'notify.send_users_email',
            'schedule': crontab(minute='*/5'),
            'args': ('email_transactional',),
        },
        'daily-emails': {
            'task': 'notify.send_users_email',
            'schedule': crontab(minute=0, hour=0),
            'args': ('email_digest',),
        },
        'refresh_box': {
            'task': 'scripts.refresh_box_tokens',
            'schedule': crontab(minute=0, hour= 2),  # Daily 2:00 a.m
            'kwargs': {'dry_run': False},
        },
        'retract_registrations': {
            'task': 'scripts.retract_registrations',
            'schedule': crontab(minute=0, hour=0),  # Daily 12 a.m
            'kwargs': {'dry_run': False},
        },
        'embargo_registrations': {
            'task': 'scripts.embargo_registrations',
            'schedule': crontab(minute=0, hour=0),  # Daily 12 a.m
            'kwargs': {'dry_run': False},
        },
        'approve_registrations': {
            'task': 'scripts.approve_registrations',
            'schedule': crontab(minute=0, hour=0),  # Daily 12 a.m
            'kwargs': {'dry_run': False},
        },
        'approve_embargo_terminations': {
            'task': 'scripts.approve_embargo_terminations',
            'schedule': crontab(minute=0, hour=0),  # Daily 12 a.m
            'kwargs': {'dry_run': False},
        },
        'triggered_mails': {
            'task': 'scripts.triggered_mails',
            'schedule': crontab(minute=0, hour=0),  # Daily 12 a.m
            'kwargs': {'dry_run': False},
        },
        'send_queued_mails': {
            'task': 'scripts.send_queued_mails',
            'schedule': crontab(minute=0, hour=12),  # Daily 12 p.m.
            'kwargs': {'dry_run': False},
        },
        'new-and-noteworthy': {
            'task': 'scripts.populate_new_and_noteworthy_projects',
            'schedule': crontab(minute=0, hour=2, day_of_week=6),  # Saturday 2:00 a.m.
            'kwargs': {'dry_run': False}
        },
    }

    # Tasks that need metrics and release requirements
    # CELERYBEAT_SCHEDULE.update({
    #     'usage_audit': {
    #         'task': 'scripts.osfstorage.usage_audit',
    #         'schedule': crontab(minute=0, hour=0),  # Daily 12 a.m
    #         'kwargs': {'send_mail': True},
    #     },
    #     'glacier_inventory': {
    #         'task': 'scripts.osfstorage.glacier_inventory',
    #         'schedule': crontab(minute=0, hour= 0, day_of_week=0),  # Sunday 12:00 a.m.
    #         'args': (),
    #     },
    #     'glacier_audit': {
    #         'task': 'scripts.osfstorage.glacier_audit',
    #         'schedule': crontab(minute=0, hour=6, day_of_week=0),  # Sunday 6:00 a.m.
    #         'kwargs': {'dry_run': False},
    #     },
    #     'files_audit_0': {
    #         'task': 'scripts.osfstorage.files_audit_0',
    #         'schedule': crontab(minute=0, hour=2, day_of_week=0),  # Sunday 2:00 a.m.
    #         'kwargs': {'num_of_workers': 4, 'dry_run': False},
    #     },
    #     'files_audit_1': {
    #         'task': 'scripts.osfstorage.files_audit_1',
    #         'schedule': crontab(minute=0, hour=2, day_of_week=0),  # Sunday 2:00 a.m.
    #         'kwargs': {'num_of_workers': 4, 'dry_run': False},
    #     },
    #     'files_audit_2': {
    #         'task': 'scripts.osfstorage.files_audit_2',
    #         'schedule': crontab(minute=0, hour=2, day_of_week=0),  # Sunday 2:00 a.m.
    #         'kwargs': {'num_of_workers': 4, 'dry_run': False},
    #     },
    #     'files_audit_3': {
    #         'task': 'scripts.osfstorage.files_audit_3',
    #         'schedule': crontab(minute=0, hour=2, day_of_week=0),  # Sunday 2:00 a.m.
    #         'kwargs': {'num_of_workers': 4, 'dry_run': False},
    #     },
    #     'analytics': {
    #         'task': 'scripts.analytics.tasks',
    #         'schedule': crontab(minute=0, hour=2),  # Daily 2:00 a.m.
    #         'kwargs': {}
    #     },
    #     'analytics-upload': {
    #         'task': 'scripts.analytics.upload',
    #         'schedule': crontab(minute=0, hour=6),  # Daily 6:00 a.m.
    #         'kwargs': {}
    #     },
    # })


WATERBUTLER_JWE_SALT = 'yusaltydough'
WATERBUTLER_JWE_SECRET = 'CirclesAre4Squares'

WATERBUTLER_JWT_SECRET = 'ILiekTrianglesALot'
WATERBUTLER_JWT_ALGORITHM = 'HS256'
WATERBUTLER_JWT_EXPIRATION = 15

DRAFT_REGISTRATION_APPROVAL_PERIOD = datetime.timedelta(days=10)
assert (DRAFT_REGISTRATION_APPROVAL_PERIOD > EMBARGO_END_DATE_MIN), 'The draft registration approval period should be more than the minimum embargo end date.'

PREREG_ADMIN_TAG = "prereg_admin"

ENABLE_INSTITUTIONS = False

ENABLE_VARNISH = False
ENABLE_ESI = False
VARNISH_SERVERS = []  # This should be set in local.py or cache invalidation won't work
ESI_MEDIA_TYPES = {'application/vnd.api+json', 'application/json'}

# Used for gathering meta information about the current build
GITHUB_API_TOKEN = None

DISCOURSE_SSO_SECRET = 'changeme'
DISCOURSE_SERVER_URL = 'http://discourse.mechanysm.com'
DISCOURSE_API_KEY = 'b1dc7fb37025f47d6cd5f109f8676819215440046c9df9e361949d3bfe54f137'
DISCOURSE_API_ADMIN_USER = 'system'

DISCOURSE_SERVER_SETTINGS = {'title': 'Open Science Framework',
                             'site_description': 'A scholarly commons to connect the entire research cycle',
                             'contact_email': 'joshu.thomas.bird@gmail.com',
                             'contact_url': '',
                             'notification_email': 'noreply@osf.io',
                             'site_contact_username': 'system',
                             'logo_url': '',
                             'logo_small_url': '',
                             'favicon_url': 'http://mechanysm.com/favicon.ico',
                             'enable_local_logins': 'false',
                             'enable_sso': 'true',
                             'sso_url': 'http://api.mechanysm.com/v2/sso',
                             'sso_secret': DISCOURSE_SSO_SECRET,
                             'sso_overrides_email': 'true',
                             'sso_overrides_username': 'true',
                             'sso_overrides_name': 'true',
                             'sso_overrides_avatar': 'true',
                             'logout_redirect': 'http://mechanysm.com/logout',
                             'cors_origins': 'http://mechanysm.com',
                             'min_topic_title_length': '0',
                             'title_min_entropy': '0',
                             'title_prettify': 'false',
                             'allow_duplicate_topic_titles': 'true',
                             }

DISCOURSE_SERVER_CUSTOMIZATIONS = [{'name': 'MFR',
                                    'enabled': 'true',
                                    'head_tag': '<link href="https://mfr.osf.io/static/css/mfr.css" media="all" rel="stylesheet">',
                                    'body_tag': '''
<style>

    #mfrIframe {

        width: 100%:

    }

</style>

<script src="https://mfr.osf.io/static/js/mfr.js"></script>
<script>
var observeDOM = (function(){
    var MutationObserver = window.MutationObserver || window.WebKitMutationObserver,
        eventListenerSupported = window.addEventListener;

    return function(obj, callback){
        if( MutationObserver ){
            // define a new observer
            var obs = new MutationObserver(function(mutations, observer){
                if( mutations[0].addedNodes.length || mutations[0].removedNodes.length )
                    callback();
            });
            // have the observer observe foo for changes in children
            obs.observe( obj, { childList:true, subtree:true });
        }
    }
})();

// Observe a specific DOM element:
observeDOM(document.body, function() {

    var topic_post = document.querySelector('.topic-post article#post_1 .cooked');

    if (!topic_post) return;
    if (document.getElementById("mfrIframe")) return;

    var mfr_div = document.createElement('div');
    mfr_div.id = "mfrIframe";
    mfr_div.classList.add('mfr', 'mrf-file');
    var reg = new RegExp('\:\/\/osf[^\/]*\/([a-z0-9]*)\/?');
    var guid = reg.exec(topic_post.textContent)[1];
    topic_post.appendChild(mfr_div);
    window.jQuery || document.write('<script src="//code.jquery.com/jquery-1.11.2.min.js">\x3C/script>');
    var mfrRender = new mfr.Render("mfrIframe", "''' + MFR_SERVER_URL + '''/render?url=''' + DOMAIN + '''"+guid+"/?action=download%26mode=render");

});


</script>
                                    ''',
                                    },
                                   {'name': 'Topic Header',
                                    'enabled': 'true',
                                    'head_tag': '',
                                    'body_tag': '''
<style>

    #project_header {

        background-color: #eee;
        box-shadow: 0 3 10px 10px rgba(0,0,0,0.4);
        overflow: hidden;
    }

    #project_header > ul > li {

        float: left;
        list-style-type: none;
        padding: 10px;
        color: #337ab7;

    }

    #project_header > ul > li:hover {

        background-color: #337ab7;
        color: #ffffff;

    }

</style>
<script>
// Observe a specific DOM element:
observeDOM(document.body, function() {

    var discourse_header = document.querySelector('header.d-header');
    var topic_post = document.querySelector('.topic-post article#post_1 .cooked');

    if (!discourse_header) return;
    if (!topic_post) return;
    if (document.getElementById("project_header")) return;

    var project_header = document.createElement('div');
    project_header.id = "project_header";

    var ul = document.createElement('ul');
    ul.classList.add("wrap");
    ul.style.margin = "0 auto";

    [
        "Project",
        "Files",
        "Wiki",
        "Analytics",
        "Registrations",
        "Forks"
    ].map(function(x) {
        var li = document.createElement("li");
        li.textContent = x
        ul.appendChild(li);
    });

    project_header.appendChild(ul);
    discourse_header.appendChild(project_header);

});
</script>
                                    ''',
                                   }]
