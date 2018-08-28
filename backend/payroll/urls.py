from rest_framework import routers
from .views import UserViewSet, PayslipViewSet, InvestmentViewSet


router = routers.DefaultRouter()  # pylint: disable=invalid-name
router.register(r'employee', UserViewSet)
router.register(r'payslip', PayslipViewSet)
router.register(r'investment', InvestmentViewSet)
# router.register(r'investmentmap', EmployeeInvestmentMapViewSet)

app_name = 'payroll'
urlpatterns = []
urlpatterns += router.urls
