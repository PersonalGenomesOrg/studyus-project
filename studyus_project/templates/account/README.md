# Notes for customizing /account templates

Django-user-accounts can be customized in many ways. The following attempts
to describe the associated templates in the context of default and
close-to-default implementations.

**Specific to StudyUs changes:**
* Instead of signup.html, StudyUs uses two
signup templates, signup_participant.html and signup_researcher.html.

-----

### signup.html

Page for website visitor to create an account.

Context provided to this template:
* **form**: The sign up form, as defined by the SignupView's `form` attribute.
The default form is `account.forms.SignupForm`.
* **redirect_field_name**: As defined by the SignupView's `redirect_field_name`
attribute. The default value is `'next'`.
* **redirect_field_value**: Override SignupView's ACCOUNT_SIGNUP_REDIRECT_URL.
Defined in the request GET or POST parameters sent to the view, for example:
      https://yoursite.example.com/account/signup/?next='/welcome/'

### signup_closed.html

**Only used if ACCOUNT_OPEN_SIGNUP is False.**

Tells website visitors that account sign up is closed.

### email_confirmation_sent.html

**Only used if ACCOUNT_EMAIL_CONFIRMATION_REQUIRED is True.**

Page to notify user that a confirmation email has been sent.

The default value for `ACCOUNT_EMAIL_CONFIRMATION_REQUIRED` in
django-user-accounts is `False`. If `False`, new users are automatically
logged in after creating an account. If `True`, the new user is sent to this
template, which should prompt them to confirm their email address.

Context provided to this template:
* **email**: The email address the confirmation was sent to.
* **success_url**: The url returned by get_success_url() in the SignupView.
Unless overridden by a redirect field, this is `ACCOUNT_SIGNUP_REDIRECT_URL`,
which defaults to '/'.

### email_confirm.html

Page used to finalize confirmation of email. Confirmation requires a POST
request; this template should provide a button for that purpose.

Context provided to this template:
* **confirmation**: An EmailConfirmation object as defined by account.models

### email_confirmed.html

**Only used when all potential relevant settings are not set.**

* If a User is already logged in, confirmation will attempt to redirect to `ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL` (default `None`) or,
if that's not set, `ACCOUNT_LOGIN_REDIRECT_URL` (default `'/'`).

* If a User is not logged in, confirmation will attempt to redirect to
`ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL` (default `'account_login'`).

If none of the above conditions return a redirect URL, this confirmation
page is loaded. (If using default settings, django-user-accounts will not use
this page.)

Context provided to this template:
* **confirmation**: An EmailConfirmation object as defined by account.models

### login.html

Page for user to log in to their account.

Context provided to this template:
* **form**: The log in form, as defined by the LoginView's `form` attribute.
The default form is `account.forms.LoginForm`.
* **redirect_field_name**: As defined by the SignupView's `redirect_field_name`
attribute. The default value is `'next'`.
* **redirect_field_value**: Override LoginView's ACCOUNT_LOGIN_REDIRECT_URL.
Defined in the request GET or POST parameters sent to the view, for example:
      https://yoursite.example.com/account/login/?next='/welcome-back/'

### logout.html

Page for user to log out of their account. Log out requires a POST
request; this template should provide a button for that purpose.

Context provided to this template:
* **redirect_field_name**: As defined by the LogoutView's `redirect_field_name`
attribute. The default value is `'next'`.
* **redirect_field_value**: Override LogoutView's redirect to
`ACCOUNT_LOGOUT_REDIRECT_URL`. Defined in the request GET or POST parameters
sent to the view, for example:
      https://yoursite.example.com/account/login/?next='/goodbye/'

### password_reset.html

Page for requesting a password reset email.

Context provided to this template:
* **form**: The password reset form, as defined by the PasswordResetView's
`form` attribute. The default form is `accounts.forms.PasswordResetForm`.

### password_reset_sent.html

Page for reporting a password reset email has been sent.

Context provided to this template:
* **form**: The password reset form, as defined by the PasswordResetView's
`form` attribute. The default form is `accounts.forms.PasswordResetForm`.
* **resend** (sometimes): If 'resend' was received in the request.POST when
submitting the form, the context includes this argument, sets to `True`.

### password_reset_token.html

Page for reseting a password, using the token-containing URL emailed to the
user.

Context provided to this template:
* **form**: The password reset form, as defined by the
PasswordResetTokenView's `form` attribute. The default form is
`accounts.forms.PasswordResetTokenForm`.
* **uidb36**: The User id, represented in base 36 (combined with the token by
  django.contrib.auth.tokens).
* **token**: The token for password reset.

  *Note: The combined data of uidb36 and token can be used to match the
  regex used by 'account_password_reset_token' when calling reverse, e.g.*
  `{% url 'account_password_reset_token' uidb36 token %}`
* **redirect_field_name**: As defined by the PasswordResetTokenView's
`redirect_field_name` attribute. The default value is `'next'`.
* **redirect_field_value**: Override PasswordResetTokenView's redirect to
`ACCOUNT_PASSWORD_RESET_REDIRECT_URL`. Defined in the GET or POST parameters
sent to the view.

### password_reset_token.html

Page for reseting a password, using the token-containing URL emailed to the
user.

Context provided to this template:
* **form**: The password change form, as defined by the ChangePasswordView's
`form` attribute. The default form is `accounts.forms.ChangePasswordForm`.
* **redirect_field_name**: As defined by the ChangePasswordView's
`redirect_field_name` attribute. The default value is `'next'`.
* **redirect_field_value**: Override ChangePasswordView's redirect to
`ACCOUNT_PASSWORD_CHANGE_REDIRECT_URL`. Defined in the GET or POST parameters
sent to the view.

## /email subdirectory

### email_confirmation_message.txt

** Only used if ACCOUNT_EMAIL_CONFIRMATION_EMAIL is True **

The email used to confirm an account's email address. By default, email
confirmation must be done in 3 days. This time limit can be configure by
setting `ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS`.

Context provided to this template:
* **email_address**: EmailAddress from account.models
* **user**: User from django.auth.User
* **activate_url**: URL created by passing key to 'account_confirm_email',
    for example:
      https://yoursite.example.com/account/confirm_email/64cdf666b2f8560e0e6b66d0c1a7a8c1e43ca46e97aa1771c8c9fedc671ee2cf
* **current_site**: Your site. For example:
      yoursite.example.com
* **key**: The confirmation key. For example:
      64cdf666b2f8560e0e6b66d0c1a7a8c1e43ca46e97aa1771c8c9fedc671ee2cf

### email_confirmation_subject.txt

Same context as **email_confirmation_message.txt** (see above).

## password_reset_message.txt

The password reset email, containing a link for password reset. This uses
django.contrib.auth's tokens, where the default expiration is 3 days and can
be altered by setting `PASSWORD_RESET_TIMEOUT_DAYS`.

Context provided to this template:
* **user**: User object
* **current_site**: Your site.
* **password_reset_url**: URL for password reset, containing the needed token.

## password_reset_subject.txt

Same context as **password_reset_message.txt** (see above).
