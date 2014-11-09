# Notes on this sample project

## Settings

### Required settings for studyus

    ACCOUNT_EMAIL_UNIQUE = True                 # default

### Recommended settings for studyus

    ACCOUNT_EMAIL_CONFIRMATION_EMAIL = True     # default
    ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True  # not default

### Settings available from django-user-accounts

* **ACCOUNT_OPEN_SIGNUP**:
  * **Default:** `True`
  * `True`: New users may sign up.
  * `False`: No new users may sign up.
* **ACCOUNT_LOGIN_URL**
  * **Default:** `account_login`
  * URL where users log in to their account.
* **ACCOUNT_SIGNUP_REDIRECT_URL**
  * **Default:** `"/"`
  * Location to go after successful signup.
  * **Note:** If ACCOUNT_EMAIL_CONFIRMATION_REQUIRED is `True`, SignupView instead
  returns the `email_confirmation_sent.html` template.
* **ACCOUNT_LOGIN_REDIRECT_URL**
  * **Default:** `"/"`
  * Location to go after log in.
* **ACCOUNT_LOGOUT_REDIRECT_URL**
  * **Default:** `/`
  * Location to go after log out.
* **ACCOUNT_PASSWORD_CHANGE_REDIRECT_URL**
  * **Default:** `'account_password'`
* **ACCOUNT_PASSWORD_RESET_REDIRECT_URL**
  * **Default:** `'account_login'`
* **ACCOUNT_REMEMBER_ME_EXPIRY**
  * **Default:** `60 * 60 * 24 * 365 * 10`
  * How many seconds to maintain the session (see Django sessions). The
  default is a couple leap days short of 10 years.
* **ACCOUNT_USER_DISPLAY**
  * **Default:** `lambda user: user.username`
* **ACCOUNT_CREATE_ON_SAVE**
  * **Default:** `True`
* **ACCOUNT_EMAIL_UNIQUE**
  * **Default:** `True`
* **ACCOUNT_EMAIL_CONFIRMATION_REQUIRED**
  * **Default:** `False`
  * If `False`, a new user is logged in after account creation, and may
  log in again later without having performed email confirmation. If `True`,
  a new user is not logged in after account creation, and must confirm their
  email address before being allowed to log in.
* **ACCOUNT_EMAIL_CONFIRMATION_EMAIL**
  * **Default:** `True`
* **ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS**
  * **Default:** `3`
* **ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL**
  * **Default:** `'account_login'`
* **ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL**
  * **Default:** `None`
* **ACCOUNT_EMAIL_CONFIRMATION_URL**
  * **Default:** `'account_confirm_email'`
* **ACCOUNT_SETTINGS_REDIRECT_URL**
  * **Default:** `'account_settings'`
* **ACCOUNT_NOTIFY_ON_PASSWORD_CHANGE**
  * **Default:** `True`
* **ACCOUNT_DELETION_MARK_CALLBACK**
  * **Default:** `'account.callbacks.account_delete_mark'`
* **ACCOUNT_DELETION_EXPUNGE_CALLBACK**
  * **Default:** `'account.callbacks.account_delete_expunge'`
* **ACCOUNT_DELETION_EXPUNGE_HOURS**
  * **Default:** `48`
* **ACCOUNT_HOOKSET**
  * **Default:** `'account.hooks.AccountDefaultHookSet'`
  * This setting allows you define your own hooks for specific functionality
  that django-user-accounts exposes. Point this to a class using a string
  and you can override the following methods:
    * `send_invitation_email(to, ctx)`
    * `send_confirmation_email(to, ctx)`
    * `send_password_change_email(to, ctx)`
    * `send_password_reset_email(to, ctx)`
* **ACCOUNT_TIMEZONES**
  * **Default:** `list(zip(pytz.all_timezones, pytz.all_timezones))`
* **ACCOUNT_LANGUAGES**
  * **Default:**
        [
          (code, get_language_info(code).get("name_local"))
          for code, lang in settings.LANGUAGES
        ]
* **ACCOUNT_USE_AUTH_AUTHENTICATE**
  * **Default:** `False`
