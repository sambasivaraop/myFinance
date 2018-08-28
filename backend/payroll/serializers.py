from rest_framework import serializers
from .models import User, Payslip, Investment


class UserSerializers(serializers.ModelSerializer):
    """Serializer class for User model."""
    class Meta:
        """Meta class for UserSerializer."""
        model = User
        fields = '__all__'

    def create(self, validated_data):
        """create a user and store the hashed password."""
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class PayslipSerializers(serializers.ModelSerializer):
    """Serializer class for Payslip model."""
    class Meta:
        """Meta class for PayslipSerializer."""
        model = Payslip
        fields = '__all__'


class InvestmentSerializers(serializers.ModelSerializer):
    """Serializer class for Investment model."""
    class Meta:
        """Meta class for InvestmentSerializer."""
        model = Investment
        fields = '__all__'


# class EmployeeInvestmentMapSerializers(serializers.ModelSerializer):
#     """Serializer class for EmployeeInvestmentMap model."""
#     class Meta:
#         """Meta class for EmployeeInvestmentMapSerializers."""
#         model = EmployeeInvestmentMap
#         fields = '__all__'
