from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

# user 모델을 참조 / 현재 활성화 된 User 모델을 반환하며, 그렇지 않은 경우 User(default) 모델을 반환
User = get_user_model()

class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User # get_user_model()
        fields = ['email']

class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User # get_user_model()
        fields = ['email', 'password']