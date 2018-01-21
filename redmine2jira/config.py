# -*- coding: utf-8 -*-

from __future__ import absolute_import


##########################################################################
#
# Redmine to JIRA Importers plugin
#
# Copyright (C) 2018, Michele Cardone
#
# config.py - Core application configuration settings
#
##########################################################################

########
# Core #
########

# The export feature of this tool offer a way to filter issues
# via a query string.Among the several filter parameters there's
# one by issue ID(s).
# However, depending on your Redmine version, it might not be
# available in your Redmine REST API,
# As it's not known which specific version introduced it,
# the tool embeds a mechanism to guess if it's available or not.
# If you don't know this detail we suggest to leave the
# CHECK_ISSUE_ID_FILTER_AVAILABILITY setting to its default value:
# every time the 'issue_id' filter is used the tool will automatically:
#
# - Verify its availability
# - Prompt the result of the verification
# - Propose to change the ISSUE_ID_FILTER_AVAILABLE setting
#   according to the result
# - Propose to disable CHECK_ISSUE_ID_FILTER_AVAILABILITY
#   to avoid performing the same check again in the future
#
# For instance it may be useful to re-enable CHECK_ISSUE_ID_FILTER_AVAILABILITY
# if the Redmine instance version changed.
#
CHECK_ISSUE_ID_FILTER_AVAILABILITY = True
ISSUE_ID_FILTER_AVAILABLE = True

# Custom Redmine to Jira users mappings used during issue export.
# The mapping is defined via usernames (login names). When no
# mapping is defined for a referenced Redmine user, by default
# the tool will map the Redmine username to the Jira one as it is.
#
# NOTE: The concept of "Jira user" is also extended to Jira Service Desk
#       "portal only customers".
#
CUSTOM_USERS_MAPPINGS = {
    #
    # Example:
    #
    #    'alice.cooper': 'dave.grohl',
    #    ...
}

# Custom Redmine groups to Jira users mappings used during issue export.
# The only relations between issues and groups is via the "Assignee"
# field, and only if issue assignment to groups is explicitly allowed
# in the Redmine instance settings.
# However, as Jira does not (and will not) support issue assignment to groups
# (https://jira.atlassian.com/browse/JRASERVER-1397) one possible mapping
# is from group names to user names. It's worth to check out the section
# "Managing Issues via a User Account" in the following KB article:
#
# https://confluence.atlassian.com/jira/how-do-i-assign-issues-to-multiple-users-207489749.html#HowdoIassignissuestomultipleusers-ManagingIssuesviaaUserAccount
#
# Therefore in such scenario the mapping is defined between Redmine
# group names and Jira usernames. When no mapping is defined for a
# referenced group the tool will prompt the user to input a Jira username.
#
# NOTE: The concept of "Jira user" is also extended to Jira Service Desk
#       "portal only customers".
#
CUSTOM_GROUPS_MAPPINGS = {
    #
    # Example:
    #
    #    'lead-developers': 'linus.torvalds',
    #    ...
}


###########
# Redmine #
###########

REDMINE_USE_HTTPS = True
REDMINE_HOST = 'redmine.example.com'
REDMINE_API_KEY = '<put-administrator-user-redmine-api-key>'

#
# Issue tracking configuration
#

ALLOW_CROSS_PROJECT_ISSUE_RELATIONS = False

# The value of this setting in Redmine comes from a selection list.
# Here the list values are collapsed to a boolean
# using the following criterion:
# - "disabled"   -> False
# - Other values -> True
ALLOW_CROSS_PROJECT_SUBTASKS = False

ALLOW_ISSUE_ASSIGNMENT_TO_GROUPS = False


# Overrides default settings with user defined ones, if any...
try:
    from redmine2jira.config_local import *  # noqa
except ImportError:
    pass


# Compose Redmine URL...
REDMINE_URL = ('{protocol}://{host}'
               .format(protocol=('https' if REDMINE_USE_HTTPS else 'http'),
                       host=REDMINE_HOST))