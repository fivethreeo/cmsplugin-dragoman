#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cmsplugin_dragoman
from djeasytests.testsetup import TestSetup

settings = {
    'DEBUG': True,
    'SITE_ID': 1,
    'STATIC_URL': '/static/', 
    'INSTALLED_APPS': [
        'cmsplugin_dragoman_test_project',
        'djangocms_text_ckeditor',
        'cms',
        'cms.stacks',
        'mptt',
        'menus',
        'south',
        'sekizai',
        'djangocms_admin_style',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'dragoman_blog',
        'dragoman_blog_admin',
        'cmsplugin_dragoman',
        'taggit',
    ],
    'USE_TZ': True,
    'MIDDLEWARE_CLASSES': (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.doc.XViewMiddleware',
        'django.middleware.common.CommonMiddleware',
        'cms.middleware.page.CurrentPageMiddleware',
        'cms.middleware.user.CurrentUserMiddleware',
        'cms.middleware.toolbar.ToolbarMiddleware',
        'cms.middleware.language.LanguageCookieMiddleware',
    ),
    'TEMPLATE_CONTEXT_PROCESSORS' : (
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.i18n',
        'django.core.context_processors.request',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'cms.context_processors.media',
        'sekizai.context_processors.sekizai',
    ),
    'CMS_TEMPLATES' : (
        ('basic.html', 'Basic Template'),
    ),
    'DRAGOMAN_BLOG_ENTRY_MODEL': ('cmsplugin_dragoman.dragoman_models.Entry', 'cmsplugin_dragoman'),
    'ROOT_URLCONF': 'cmsplugin_dragoman_test_project.urls',
    'LANGUAGE_CODE': 'en',
    'LANGUAGES': (
        ('en', 'English'),
        ('ja', u'日本語')
    )
}
    
testsetup = TestSetup(appname='cmsplugin_dragoman', test_settings=settings, version=cmsplugin_dragoman.get_version())

if __name__ == '__main__':
    testsetup.run(__file__)
