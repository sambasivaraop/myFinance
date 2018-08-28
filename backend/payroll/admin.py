from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from . models import User, Payslip, Investment


# class EmployeeInvestmentMapAdmin(admin.ModelAdmin):
#     """InvestmentAdmin class to list-display/filter."""
#
#     list_display = ('investment', 'institute_name', 'policy_no',
#                     'declaration', 'rental_address', 'rent_amnt_PM',
#                     'rental_amnt_PA')

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'emp_id',
                  'doj', 'user_type')

    def clean_password2(self):
        """Method to check that the two password entries match."""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        """Save the provided password in hashed format."""
        user = super(UserCreationForm, self).save(commit=False)
        if user.user_type == 'employee':
            user.is_staff = False
        user.set_password(self.cleaned_data["password1"])
        user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users."""
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'emp_id',
                  'doj', 'user_type')


class MyUserAdmin(BaseUserAdmin):
    """Custom admin class for User model"""
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'emp_id', 'doj',
                    'user_type')
    list_filter = ('user_type',)
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'emp_id',
                           'doj', 'user_type')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('extrapretty',),
            'fields': ('email', ('first_name', 'last_name'), 'emp_id', 'doj',
                       'user_type', 'password1', 'password2')}),
    )
    search_fields = ('email',)
    ordering = ('doj',)
    filter_horizontal = ()


admin.site.register(Payslip)
admin.site.register(Investment)
# admin.site.register(EmployeeInvestmentMap)
admin.site.register(User, MyUserAdmin)
