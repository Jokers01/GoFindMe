from django.shortcuts import render , redirect , get_object_or_404
from cariorang.models import PostCari, Detail
from cariorang.forms import PostCariForm , DetailForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, ListView ,DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy , reverse
from django.contrib.auth.models import User
from django.utils import timezone
from .filters import PostCariFilter

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML


@method_decorator(login_required, name="dispatch")
class PostCariView(ListView):
    model = PostCari
    context_object_name = 'cariview'
    template_name = 'home.html'
    paginate_by = 6
    queryset = PostCari.objects.all().order_by('-created_at')


def homeawal(request):
    return render(request,"homeawal.html")

@login_required
def SearchPostCari(request):
    post_cari = PostCari.objects.all()
    post_filter = PostCariFilter(request.GET, queryset=post_cari)
    return render(request,"search_cari.html",{'post_filter':post_filter})


@login_required
def BuatPostCari(request):
    if request.method == "POST":
        form = PostCariForm(request.POST , request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.approve = False
            post.save()
            return redirect('mypost')
    else:
        form = PostCariForm()
    return render(request,'form_cari.html',{'form':form})

@method_decorator(login_required, name="dispatch")
class postcari_details(DetailView):
    model = PostCari
    context_object_name = "post_cari"
    template_name = "post_details.html"


"""
def postcari_details(request, pk):
    post_cari = get_object_or_404(PostCari, pk = pk)
    return render(request, 'post_details.html', {'post_cari':post_cari} )
"""

@login_required
def reply_comment(request, pk):
    post_cari = get_object_or_404(PostCari, pk = pk)

    if request.method == "POST":
        message = request.POST['message']

        user = User.objects.first()

        detail = Detail.objects.create(
            postcari = post_cari,
            message = message,
            created_by = request.user,
        )
        return redirect('post_details', pk= post_cari.pk)
    return render(request,'reply_comment.html',{'post_cari':post_cari})

@login_required
def mypost(request):
    post_cari = PostCari.objects.all()
    return render(request, 'my_post.html', {'post_cari':post_cari})


@method_decorator(login_required, name="dispatch")
class DetailUpdateView(UpdateView):
    model = Detail
    fields = ['message',]
    template_name = "edit_details.html"
    pk_url_kwargs = 'pk_detail'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self , form):
        detail = form.save(commit=False)
        detail.updated_by = self.request.user
        detail.updated_at = timezone.now()
        detail.save()
        return redirect('post_details', pk=detail.postcari.pk)


@method_decorator(login_required, name="dispatch")
class PostCariUpdateView(UpdateView):
    model = PostCari
    fields = ['name','umur','tinggi','berat','gender','reward','phone_number','lokasi_hilang','picture','desc']
    template_name = "edit_postcari.html"
    success_url = "/postcari/mypost"

@method_decorator(login_required, name="dispatch")
class PostCariDeleteView(DeleteView):
    model = PostCari
    template_name = "delete_postcari.html"
    context_object_name = "delete"
    success_url = reverse_lazy('mypost')


@login_required
def ketemu_diterima(request ,pk ):
    post = get_object_or_404(PostCari, pk = pk)
    post.ketemu_approve()
    return redirect('home')

@login_required
def template_cariorang(request,pk):
    try:
        post_cari = PostCari.objects.filter(pk=pk)
    except PostCari.DoesNotExist:
        raise Http404("Model tidak sama dengan query yang ada.")
    html_str = render_to_string('template_cariorang_pdf.html',{'postcari':post_cari})

    pdf = HTML(string=html_str, base_url=request.build_absolute_uri())
    pdf.write_pdf(target='/tmp/cariorang.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('cariorang.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="cariorang.pdf"'
        return response

    return response
