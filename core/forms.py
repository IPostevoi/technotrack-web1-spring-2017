# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from django.core.urlresolvers import reverse
from crispy_forms.bootstrap import Field
from crispy_forms.layout import Submit, Layout, Fieldset


class SearchForm(forms.Form):
    search = forms.CharField(required=False)

    def __init__(self):
        super(SearchForm, self).__init__()
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_method = 'get'
        self.helper.form_action = reverse('core:items')
        self.helper.layout = Layout(
                     Field('search', placeholder='Искать',
                           css_class="form-control"))

        self.helper.add_input(Submit('submit', 'Submit', css_class="btn btn-default"))
        self.helper.form_class = "navbar-form navbar-right"



