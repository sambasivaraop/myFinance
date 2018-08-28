import logging
import json
import requests
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework import status
from .models import User, Payslip, Investment
from .serializers import UserSerializers, PayslipSerializers, \
    InvestmentSerializers
from .permissions import UserViewSetPermission

TOKEN_GET_ENDPOINT = 'http://localhost:8000/api-token-auth/'
LOGGER = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    """"UserViewSet to create, retrieve, update and delete the Employee
    object."""
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (UserViewSetPermission, )

    @list_route(methods=['post'], permission_classes=(), )
    def login(self, request):
        """
        login for any valid user.
        return: token if user is valid, Bad request otherwise
        """
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        if email is None and password is None:
            LOGGER.error("Either email or password not matched.")
            return Response(
                data="Please enter a valid email address and password",
                status=status.HTTP_400_BAD_REQUEST)
        data = {'email': email, 'password': password}
        resp = requests.post(url=TOKEN_GET_ENDPOINT, data=data)
        if resp.status_code != 200:
            LOGGER.error("Invalid credentials, Login failed!.")
            return Response(data="Invalid Credentials",
                            status=status.HTTP_401_UNAUTHORIZED)
        LOGGER.debug("Login successful.")
        user = {'user_type': User.objects.get(email=email).user_type,
                'first_name': User.objects.get(email=email).first_name,
                'last_name': User.objects.get(email=email).last_name,
                'emp_id': User.objects.get(email=email).emp_id,
                'email': email}
        response = json.loads(resp.text)
        response.update(user)
        return Response(json.dumps(response), status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """create the user."""
        if request.data.get('user_type', None) == "employee":
            resp = super(UserViewSet, self).create(request, *args, **kwargs)
            LOGGER.debug("Employee created successfully")
        else:
            resp = super(UserViewSet, self).create(request, *args, **kwargs)
            LOGGER.debug("Admin created successfully.")
        return resp

    def perform_create(self, serializer):
        """ To set is_staff flag if user is admin"""
        if self.request.data.get('user_type', None) == 'employee':
            serializer.save(is_staff=False)
        else:
            serializer.save()


class PayslipViewSet(viewsets.ModelViewSet):
    """"PayslipViewSet to create, retrieve, update and delete the Payslip
    object."""
    queryset = Payslip.objects.all()
    serializer_class = PayslipSerializers

    @list_route(methods=['get'], permission_classes=(), )
    def employee_payslip_details(self, request):
        queryset = Payslip.objects.filter(employee=self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class InvestmentViewSet(viewsets.ModelViewSet):
    """"InvestmentViewSet to create, retrieve, update and delete the Investment
    object."""
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializers

    @list_route(methods=['get'], permission_classes=(), )
    def employee_investment_details(self, request):
        queryset = Investment.objects.filter(employee=self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# class EmployeeInvestmentMapViewSet(viewsets.ModelViewSet):
#     """"EmployeeInvestmentMapViewSet to create, retrieve, update and delete the
#     EmployeeInvestmentMap object."""
#     queryset = EmployeeInvestmentMap.objects.all()
#     serializer_class = EmployeeInvestmentMapSerializers

