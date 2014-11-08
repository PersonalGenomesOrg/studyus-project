# Notes for customizing /account templates

Django-user-accounts can be customized in many ways. The following describes
the behavior of these templates in this default project set up.

### signup.html

Context provided to this template:
* **form**: The sign up form, as defined by the SignupView's `form` attribute.
The default form is `account.forms.SignupView`.
* **redirect_field_name**: As defined by the SignupView's `redirect_field_name`
attribute. The default value is `'next'`.
* **redirect_field_value**: Defined in the request GET or POST parameters
sent to SignUpView, for example:
      https://yoursite.example.com/account/signup/?next='/welcome/'

### signup_closed.html

**Only used if ACCOUNT_OPEN_SIGNUP is False.**

Tells website visitors that account sign up is closed.

### email_confirmation_sent.html

**Only used if ACCOUNT_EMAIL_CONFIRMATION_REQUIRED is True.**

Our sample project sets this to `True`; the default value in
django-user-accounts is `False`. If `False`, new users are automatically
logged in after creating an account. If `True`, the new user is sent to this
template, which should prompt them to confirm their email address.

Context provided to this template:
* **email**: The email address the confirmation was sent to.
* **success_url**: The url returned by get_success_url() in the SignupView.
Unless overridden by a redirect field, this is is ACCOUNT_SIGNUP_REDIRECT_URL,
which defaults to '/'.

## /email subdirectory

### email_confirmation_message.txt

By default, email confirmation must be done in 3 days. This time limit can
be configure by setting ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS.

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
