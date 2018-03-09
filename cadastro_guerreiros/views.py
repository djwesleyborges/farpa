from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import guerreiros
from .forms import FormCadastroGuerreiros


def lista(request):
    lista_guerreiros = guerreiros.objects.all()
    context = {'lista_guerreiros': lista_guerreiros}
    return render(request, 'cadastro/lista_guerreiros.html', context)


class adiciona(TemplateView):
    template_name = 'cadastro/adiciona.html'

    def get(self, request):
        form = FormCadastroGuerreiros()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = FormCadastroGuerreiros(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
        args = {'form': form}
        return render(request, self.template_name, args)