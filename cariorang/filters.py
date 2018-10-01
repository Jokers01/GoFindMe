from cariorang.models import PostCari
import django_filters


class PostCariFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(lookup_expr='icontains')
    lokasi_hilang = django_filters.CharFilter(lookup_expr='icontains')
    created_at = django_filters.NumberFilter(lookup_expr='year')
    reward = django_filters.LookupChoiceFilter(
        lookup_choices=[
            ('exact', 'Sama Dengan (=)'),
            ('gt', 'Lebih Besar (>)'),
            ('lt', 'Lebih Kecil (<)'),
        ]
    )

    class Meta:
        model = PostCari
        fields = ['name','umur','reward','created_at','lokasi_hilang','gender']
