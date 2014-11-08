# forms.py
from collections import OrderedDict

import account.forms


class SignupForm(account.forms.SignupForm):

    def __init__(self, *args, **kwargs):
        """
        Override to remove username, and sort fields so email is asked first.
        """
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]
        field_order = ['email', 'password', 'password_confirm']
        self.fields = force_field_order(self.fields, field_order)


def force_field_order(old_dict, field_order):
    """Return a new OrderedDict with rearranged keys matching field_order"""
    new_dict = OrderedDict()
    try:
        for field in field_order:
            new_dict[field] = old_dict.pop(field)
    except KeyError:
        raise KeyError("force_field_order received a field not in " +
                       "the original dictionary")
    new_dict.update(old_dict.items())
    return new_dict
