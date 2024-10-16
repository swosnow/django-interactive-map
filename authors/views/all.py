from django.shortcuts import render, redirect
from authors.forms import RegisterForm, LoginForm
from django.http import Http404, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from mapaguapi.models import Problem
from authors.forms.problem_form import AuthorProblemForm

def register_view(request):
    register_form_data = request.session.get('register_form_data', None)

    form = RegisterForm(register_form_data)
    
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
        'form_action': reverse('authors:register_create')
    })

def register_create(request):

    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Seu usuário foi criado com sucesso!!, por favor faça login.')

        del(request.session['register_form_data'])
        return redirect(reverse('authors:login'))

    return redirect('authors:register')


def login_view(request):
    form = LoginForm()
    return render(request, 'authors/pages/login.html',
                  {'form': form,
                   'form_action': reverse('authors:login_create')})

def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Você está logado.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Credenciais inválidas')
    else:
        messages.error(request, 'Usuário ou senha inválidos')

    return redirect(reverse('authors:dashboard'))

@login_required(login_url='authors:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        messages.error(request, 'Invalid logout request')
        return redirect(reverse('authors:login'))
    
    if request.POST.get('username') != request.user.username:
        messages.error(request, 'Invalid logout user')
        return redirect(reverse('authors:login'))
    
    messages.success(request, 'Logged out successfully')
    logout(request)
    return redirect(reverse('authors:login'))

@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard(request):
    problems = Problem.objects.filter(
        is_published=False,
        author=request.user,
    )
    return render(request, 'authors/pages/dashboard.html', {
        'problems': problems,
    })




@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_problem_new(request):
    form = AuthorProblemForm(
        data=request.POST or None,
        
    )
    latitude = request.POST.get('latitude')
    longitude = request.POST.get('longitude')

    if form.is_valid():
        problem: Problem = form.save(commit=False)
        
        problem.author = request.user
        problem.preparation_steps_is_html = False
        problem.is_published = False

        Problem.objects.create(lat=latitude, lng=longitude)

        problem.save()

        messages.success(request, 'Salvo com sucesso!')
        return redirect(
            reverse('authors:dashboard_problem_edit', args=(problem.id,))
        )

    return render(
        request,
        'authors/pages/dashboard_problem.html',
        context={
            'form': form,
            'form_action': reverse('authors:dashboard_problem_new')
        }
    )


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_problem_delete(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    id = POST.get('id')

    problem = Problem.objects.filter(
        is_published=False,
        author=request.user,
        pk=id,
    ).first()
    if not problem:
        raise Http404()
    problem.delete()
    messages.success(request, 'Deletado com sucesso!.')
    return redirect(reverse('authors:dashboard'))