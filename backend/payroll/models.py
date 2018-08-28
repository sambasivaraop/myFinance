from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    """User manager class to handle the creation of users."""
    use_in_migrations = True

    def _create_user(self, email, password):
        """Creates and saves a User with given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None):
        """
        Create and save a User with given email and password.
        :param email: user's valid email address
        :param password: password
        :return: User instance
        """
        user = self._create_user(email, password)
        if user.user_type == "employee":
            user.is_staff = False
            user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and save a Superuser with given email and password.
        :param email: superuser's valid email address
        :param password: password
        :return: user instance
        """
        user = self._create_user(email, password)
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """Model class for User instance."""
    type_choice = (
        ('admin', 'Admin'),
        ('employee', 'Employee'),
    )
    emp_id = models.IntegerField(unique=True, default=00000, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    doj = models.DateField(default=date.today())
    user_type = models.CharField(max_length=20,
                                 choices=type_choice,
                                 default='admin')
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """User permission for App."""
        return True


def payslip_path(instance, filename):
    """Returns Payslip path."""
    return '{0}_payslip/{1}_{2}_{3}'.format(instance.employee.emp_id,
                                            instance.year, instance.month,
                                            filename)


class Payslip(models.Model):
    """Model class for Payslip instance."""
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.CharField(max_length=10)
    year = models.CharField(max_length=4)
    payslip = models.FileField(upload_to=payslip_path)

    def __str__(self):
        return self.employee.email + '_' + self.month + '_' + self.year


class Investment(models.Model):
    """Model class for Investment instance."""
    investment_choice = (
        ('NA', 'Select Your Investment type'),
        ('80C - Investment Under 80C', '80C - Investment Under 80C'),
        ('80D - Medical Insurance', '80D - Medical Insurance'),
        ('80DD - Handicapped Dependant', '80DD - Handicapped Dependant'),
        ('80E - Education Loan', '80E - Education Loan'),
        ('80U - Self with Physical Disability',
         '80U - Self with Physical Disability'),
        ('80EE - Additional Deduction on Home Loan Interest',
         '80EE - Additional Deduction on Home Loan Interest'),
        ('Interest on Housing Loan', 'Interest on Housing Loan'),
        ('Rent', 'Rent'),
        ('Other Income', 'Other Income'),
        ('80DDB - Medical Treatment', '80DDB - Medical Treatment'),
        ('80CCD - National Pension Scheme(NPS)',
         '80CCD - National Pension Scheme(NPS)'),
        ('Previous Employment', 'Previous Employment')
    )
    choice_80c = (
        ('NA', 'Select Your 80C type'),
        ('NSC/Tax Saving Bank Fixed deposits',
         'NSC/Tax Saving Bank Fixed deposits'),
        ('Public Provident Fund', 'Public Provident Fund'),
        ('Insurance premium towards life', 'Insurance premium towards life'),
        ('Housing loan principal payment', 'Housing loan principal payment'),
        ('Sukanya Samriddhi A/c', 'Sukanya Samriddhi A/c'),
        ('Tax saving MutualFunds', 'Tax saving MutualFunds'),
        ('ULIP', 'ULIP'),
        ('Children Tuition Fee', 'Children Tuition Fee')
    )
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=investment_choice,
                            default='NA')
    type_80c = models.CharField(max_length=100, choices=choice_80c,
                                default='NA', blank=True)
    institute_name = models.CharField(max_length=20, blank=True)
    policy_no = models.CharField(max_length=10, blank=True)
    declaration = models.CharField(max_length=10, blank=True)
    rental_address = models.CharField(max_length=300, blank=True)
    rent_amnt_PM = models.CharField(max_length=10, blank=True)
    rent_amnt_PA = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return str(self.employee.emp_id) + "_" + self.type


# class EmployeeInvestmentMap(models.Model):
#     """Model class for EmployeeInvestmentMap instance."""
#     employee = models.ForeignKey(User, on_delete=models.CASCADE)
#     investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
#     policy_no = models.CharField(max_length=10)
#     institute_name = models.CharField(max_length=20)
#     declaration = models.IntegerField()
#     rental_address = models.CharField(max_length=300)
#     rent_amnt_PM = models.IntegerField()
#     rental_amnt_PA = models.IntegerField()


