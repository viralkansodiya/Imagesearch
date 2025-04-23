app_name = "imagesearch"
app_title = "Imagesearch"
app_publisher = "test"
app_description = "test"
app_email = "test@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "imagesearch",
# 		"logo": "/assets/imagesearch/logo.png",
# 		"title": "Imagesearch",
# 		"route": "/imagesearch",
# 		"has_permission": "imagesearch.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/imagesearch/css/imagesearch.css"
# app_include_js = "/assets/imagesearch/js/imagesearch.js"

# include js, css files in header of web template
# web_include_css = "/assets/imagesearch/css/imagesearch.css"
# web_include_js = "/assets/imagesearch/js/imagesearch.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "imagesearch/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "imagesearch/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "imagesearch.utils.jinja_methods",
# 	"filters": "imagesearch.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "imagesearch.install.before_install"
# after_install = "imagesearch.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "imagesearch.uninstall.before_uninstall"
# after_uninstall = "imagesearch.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "imagesearch.utils.before_app_install"
# after_app_install = "imagesearch.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "imagesearch.utils.before_app_uninstall"
# after_app_uninstall = "imagesearch.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "imagesearch.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"imagesearch.tasks.all"
# 	],
# 	"daily": [
# 		"imagesearch.tasks.daily"
# 	],
# 	"hourly": [
# 		"imagesearch.tasks.hourly"
# 	],
# 	"weekly": [
# 		"imagesearch.tasks.weekly"
# 	],
# 	"monthly": [
# 		"imagesearch.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "imagesearch.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "imagesearch.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "imagesearch.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["imagesearch.utils.before_request"]
# after_request = ["imagesearch.utils.after_request"]

# Job Events
# ----------
# before_job = ["imagesearch.utils.before_job"]
# after_job = ["imagesearch.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"imagesearch.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

