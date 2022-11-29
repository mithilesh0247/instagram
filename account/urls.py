from django.urls import path
from account.views import SendPasswordResetEmailView, UserLoginWithName, UserLoginWithEmailOtpView, EmailOtpVerifyView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView, SocialLoginAPIView, UserLoginWithOtp, UserVerifyOtp
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('loginotp/', UserLoginWithOtp.as_view(), name='loginotp'),
    path('profile/', UserProfileView.as_view(), name='profile'),

    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(),

         name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/',
         UserPasswordResetView.as_view(), name='reset-password'),
    path('verifyotp/', UserVerifyOtp.as_view(), name='loginotp'),
    path("sociallogin/", SocialLoginAPIView.as_view()),
    path("useremaillogin/", UserLoginWithEmailOtpView.as_view()),
    path("emailotpverify/", EmailOtpVerifyView.as_view()),
    path("usernamelogin/", UserLoginWithName.as_view()),
]
# Savitri0247
# Mithilesh0247
