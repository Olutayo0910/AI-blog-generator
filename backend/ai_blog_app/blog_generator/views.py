from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')

def user_login(request):
    return render(request, 'login.html')

def user_signup(request):
    error_message = ''  # Initialize error_message here
    
    if request.method == 'POST':
        # Handle form submission
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        if password == confirmPassword:
            try:
                # Create a new user
                user = User.objects.create_user(username, email, password)
                user.save()

                # Authenticate the user
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    print("User is authenticated:", user.is_authenticated)
                    return redirect('/')
                else:
                    print("User authentication failed.")
            except Exception as e:
                error_message = 'Error! Please try again'
                print("Error occurred during signup:", str(e))
        else:
            error_message = 'Passwords do not match'

    # Render the signup page with error_message
    return render(request, 'sign_up.html', {'error_message': error_message})

def user_logout(request):
    pass