from django.shortcuts import render
from .models import Poll, Option
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView, DeleteView

# Create your views here.
# 列出投票主題
def poll_list(req):
    polls = Poll.objects.all()
    return render(req, 'poll_list.html', {'list_poll': polls})

class PollList(ListView):
    model = Poll

class PollView(DetailView):
    model = Poll

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # ctx['option_list'] = Option.objects.filter(poll_id=self.kwargs['pk'])
        ctx['option_list'] = Option.objects.filter(poll_id=self.object.id)
        return ctx

class PollVote(RedirectView):    
    def get_redirect_url(self, *args, **kwargs):
        option = Option.objects.get(id=self.kwargs['oid'])
        option.count += 1   # option.count = option.count + 1
        option.save()
        return "/poll/{}/".format(option.poll_id)
        return "/poll/" + str(option.poll_id) + "/"

class PollCreate(CreateView):
    model = Poll
    fields = ['subject']
    success_url = '/poll/'
    extra_context = {'mytitle': '新增投票主題'}

class PollEdit(UpdateView):
    model = Poll
    fields = ['subject']
    extra_context = {'mytitle': '修改投票主題'}
    
    def get_success_url(self):
        return "/poll/{}/".format(self.object.id)
        return "/poll/{}/".format(self.kwargs['pk'])

class PollDelete(DeleteView):
    model = Poll
    success_url = '/poll/'

class OptionCreate(CreateView):
    model = Option
    fields = ['title']
    template_name = 'default/poll_form.html'

    def form_valid(self, form):
        form.instance.poll_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return "/poll/{}/".format(self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['datatype'] = '投票選項'
        return ctx

class OptionEdit(UpdateView):
    model = Option
    fields = ['title']
    template_name = 'default/poll_form.html'
    pk_url_kwarg = 'oid'

    def get_success_url(self):
        return '/poll/{}/'.format(self.object.poll_id)

class OptionDelete(DeleteView):
    model = Option
    pk_url_kwarg = 'oid'
    template_name = 'default/poll_confirm_delete.html'

    def get_success_url(self):
        return '/poll/{}/'.format(self.object.poll_id)