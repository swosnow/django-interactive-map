from authors.forms.problem_form import AuthorProblemForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from mapaguapi.models import Problem


@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardProblem(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, *args, **kwargs):
        return super().setup(*args, **kwargs)

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_problem(self, id=None):
        problem = None

        if id is not None:
            problem = Problem.objects.filter(
                is_published=False,
                author=self.request.user,
                pk=id,
            ).first()

            if not problem:
                raise Http404()

        return problem

    def render_problem(self, form):
        return render(
            self.request,
            'authors/pages/dashboard_problem.html',
            context={
                'form': form
            }
        )

    def get(self, request, id=None):
        problem = self.get_problem(id)
        form = AuthorProblemForm(instance=problem)
        return self.render_problem(form)

    def post(self, request, id=None):
        problem = self.get_problem(id)
        form = AuthorProblemForm(
            data=request.POST or None,
            files=request.FILES or None,
            instance=problem
        )

        if form.is_valid():
            
            problem = form.save(commit=False)

            problem.author = request.user
            problem.preparation_steps_is_html = False
            problem.is_published = False

            problem.save()

            messages.success(request, 'Sua receita foi salva com sucesso!')
            return redirect(
                reverse(
                    'author:dashboard_problem_edit', args=(
                        problem.id,
                    )
                )
            )

        return self.render_problem(form)