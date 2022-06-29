from django.views.generic.list import ListView
from django.shortcuts import redirect
from .models import My_List, Country
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, FormView
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from .forms import CreateUserForm
from .forms import Message


class Register(FormView):
    template_name = 'all/register.html'
    form_class = CreateUserForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('list')
        return super(Register, self).get(*args, **kwargs)


class LoginPage(LoginView):
    template_name = 'all/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('list')


def contact(reqeust):
    form = Message()
    if reqeust.method == 'POST':
        form = Message(reqeust.POST)
        if form.is_valid():
            form.save()
    return render(reqeust, 'all/contact.html', {
        'form': form,
        'country': Country.objects.all()
                                                })


class DeleteProduct(LoginRequiredMixin, DeleteView):
    model = My_List
    context_object_name = 'delete'
    success_url = reverse_lazy('list')
    template_name = 'all/delete.html'


class Creat_Product(LoginRequiredMixin, CreateView):
    model = My_List
    fields = ['product', 'brand', 'section', 'start_data', 'finish_data']
    success_url = reverse_lazy('list')
    template_name = 'all/shop.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Creat_Product, self).form_valid(form)


class My_list(LoginRequiredMixin, ListView):
    model = My_List
    context_object_name = 'list'
    template_name = 'all/my_list.html'

    def get_context_data(self, **kwargs):
        context = super(My_list, self).get_context_data(**kwargs)
        context['list'] = context['list'].filter(user=self.request.user)
        context['count'] = context['list'].filter(id=False).count()

        search_p = self.request.GET.get('search') or ''
        if search_p:
            context['list'] = context['list'].filter(
                product__icontains=search_p
            )
        context['search_p'] = search_p
        return context


def main(request):
    return render(request, 'all/index.html')
