"""eduproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from accounts.urls import router as accounts_router
from school.urls import router as school_router 
from admission.urls import router as admission_router
from attendance.urls import router as attendance_router
from department.urls import router as department_router 
from employee.urls import router as employee_router
from student.urls import router as student_router
from timetable.urls import router as timetable_router


urlpatterns = [
    url(r'^api/accounts/', include(accounts_router.urls)),
    url(r'^api/school/', include(school_router.urls)),
    url(r'^api/admission/', include(admission_router.urls)),
    url(r'^api/attendance/', include(attendance_router.urls)),
    url(r'^api/department/', include(department_router.urls)),
    url(r'^api/employee/', include(employee_router.urls)),
    url(r'^api/student/', include(student_router.urls)),
    url(r'^api/timetable/', include(timetable_router.urls)),
    url(r'^api/api-token-auth/', obtain_jwt_token),
    url(r'^api/api-token-verify/', verify_jwt_token),
    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^api/', include('rest_framework_docs.urls')),

    url(r'^admin/', admin.site.urls),
]
