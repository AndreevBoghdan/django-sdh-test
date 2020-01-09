from django.urls import path

from . import views

urlpatterns = [
    path("", views.SdhRegistrationView.as_view(), name='register'),
    path(
        "activate/<str:activation_key>/",
        views.SdhActivationView.as_view(),
        name="registration_activate",
    ),
    path(
    	"profile/",
    	views.profile,
    	name="user_profile"
    ),
    path(
    	"generate_new_code/",
    	views.generate_new_code,
    	name="generate_invitation_code"
    )
]
