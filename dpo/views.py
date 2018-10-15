from django.shortcuts import render , redirect , get_object_or_404
from dpo.models import PostDPO , DetailDPO
from dpo.forms import PostFormDPO , DetailFormDPO
from dpo.filters import PostDPOFilter
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, ListView ,DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy , reverse
from django.contrib.auth.models import User
from django.utils import timezone



from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML


# Create your views here.

@method_decorator(login_required, name="dispatch")
class DPOView(ListView):
    model = PostDPO
    context_object_name = "caridpo"
    template_name = "dpo_home.html"
    paginate_by = 6

    def get_queryset(self):
        return PostDPO.objects.all().order_by('-created_at')[0::]


@login_required
def BuatFormDPO(request):
    if request.method == "POST":
        form = PostFormDPO(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.approve = False
            post.save()
            return redirect("dpo:formcaridpo")
    else:
        form = PostFormDPO()
    return render(request,"formcaridpo.html",{'form':form})

@login_required
def mypostdpo(request):
    mypost = PostDPO.objects.all()
    return render(request,"mypostdpo.html",{'mypost':mypost})


@login_required
def SearchPostDPO(request):
    post_dpo = PostDPO.objects.all()
    post_filter = PostDPOFilter(request.GET, queryset=post_dpo)
    return render(request,"search_dpo.html",{'post_filter':post_filter})


@method_decorator(login_required, name="dispatch")
class postdpo_details(DetailView):
    model = PostDPO
    context_object_name = "post_dpo"
    template_name = "post_details_dpo.html"
    pk_url_kwargs = "pk"


@login_required
def reply_comment(request, pk):
    post_dpo = get_object_or_404(PostDPO, pk = pk)

    if request.method == "POST":
        message = request.POST['message']

        user = User.objects.first()

        detail = DetailDPO.objects.create(
            postdpo = post_dpo,
            message = message,
            created_by = request.user,
        )
        return redirect('dpo:post_details_dpo', pk= post_dpo.pk)
    return render(request,'reply_comment.html',{'post_dpo':post_dpo})




@method_decorator(login_required, name="dispatch")
class DetailUpdateView(UpdateView):
    model = DetailDPO
    fields = ['message',]
    template_name = "edit_details_dpo.html"
    pk_url_kwargs = 'pk_details'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self , form):
        detail = form.save(commit=False)
        detail.updated_by = self.request.user
        detail.updated_at = timezone.now()
        detail.save()
        return redirect('dpo:post_details_dpo', pk = detail.postdpo.pk)


@method_decorator(login_required, name="dispatch")
class PostDPODeleteView(DeleteView):
    model = PostDPO
    template_name = "delete_postcari.html"
    context_object_name = "delete"
    success_url = reverse_lazy('dpo:mypostdpo')


@method_decorator(login_required, name="dispatch")
class PostDPOUpdateView(UpdateView):
    model = PostDPO
    fields = ['name','umur','tinggi','berat','phone_number','kelamin','pasal','pekerjaan','reward','alamat','gambar','ciri']
    template_name = "edit_postcari_dpo.html"
    success_url = "dpo/postdpo/mypostdpo"



@login_required
def template_caridpo(request,pk):
    try:
        post_dpo = PostDPO.objects.filter(pk=pk)
    except PostDPO.DoesNotExist:
        raise Http404("Model tidak sama dengan query yang ada.")
    html_str = render_to_string('template_caridpo_pdf.html',{'postdpo':post_dpo})

    pdf = HTML(string=html_str, base_url=request.build_absolute_uri())
    pdf.write_pdf(target='/tmp/caridpo.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('caridpo.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="caridpo.pdf"'
        return response

    return response


@login_required
def ketemu_dpo(request ,pk ):
    post = get_object_or_404(PostDPO, pk = pk)
    post.ketemu_approve()
    return redirect('dpo:home')
