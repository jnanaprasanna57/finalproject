# from django.urls import path
# from . import views

# urlpatterns = [

#     # ---------------- FARMER ---------------- #

#     path('register/', views.farmer_register, name='farmer_register'),
#     path('login/', views.farmer_login, name='farmer_login'),
#     path('logout/', views.farmer_logout, name='farmer_logout'),
#     path('dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
#     path('add-sensor/', views.add_sensor_data, name='add_sensor'),
#     path('view-prediction/', views.view_prediction, name='view_prediction'),

#     # ---------------- ADMIN ---------------- #

#     path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
#     path('view-farmers/', views.view_farmers, name='view_farmers'),
#     path('view-sensor/', views.view_sensor_data, name='view_sensor'),
#     path('feature-importance/', views.feature_importance_view, name='feature_importance'),
#     path('admin-login/', views.admin_login, name='admin_login'),
#     path('admin-logout/', views.admin_logout, name='admin_logout'),
#     path('algorithm-results/', views.algorithm_results, name='algorithm_results'),
#     path('arduino-api/', views.arduino_sensor_api),

#     # ---------------- API ---------------- #

  
# ]


from django.urls import path
from . import views

urlpatterns = [

    # Farmer
    path('dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('add-sensor/', views.add_sensor, name='add_sensor'),
    path('view-prediction/', views.view_prediction, name='view_prediction'),
    path('feature-importance/', views.feature_importance_view, name='feature_importance'),

    # Admin
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('view-farmers/', views.view_farmers, name='view_farmers'),
    path('view-sensor/', views.view_sensor_data, name='view_sensor'),
    path('algorithm-results/', views.algorithm_results, name='algorithm_results'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),

    # Arduino
    path('arduino-api/', views.arduino_api, name='arduino_api'),
]