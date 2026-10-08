from django.contrib import admin
from django.contrib import messages
from django.utils import timezone
from django.utils.html import format_html

from .models import (
    AuthorDetailModel,
    AuthorModel,
    BookAuthorModel,
    BookModel,
    BorrowModel,
    CategoryModel,
    GenreModel,
    LibraryModel,
    PostModel,
    PublisherModel,
)

admin.site.register(AuthorDetailModel)
admin.site.register(CategoryModel)
admin.site.register(GenreModel)
admin.site.register(LibraryModel)
admin.site.register(BookAuthorModel)
admin.site.register(PostModel)
admin.site.register(BorrowModel)


class BookInlineAdmin(admin.TabularInline):
    model = BookModel
    fields = ('title', 'category', 'published_date', 'page_count')
    # exclude = ('authors',)
    readonly_fields = ('page_count',)
    can_delete = False
    show_change_link = True
    extra = 1
    classes = ('collapse',)


@admin.register(PublisherModel)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInlineAdmin]


@admin.action(description='Change book category to classic')
def to_classic(modeladmin, request, queryset):
    classic = CategoryModel.objects.get(slug='classic')
    res = queryset.update(category=classic, updated_at=timezone.now())
    modeladmin.message_user(request, f'Changed book category to classic = {res}', messages.SUCCESS)



@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'get_authors', 'publisher', 'published_date', 'display_cover')
    list_editable = ('title', 'category')
    list_select_related = ('category', 'publisher')

    search_fields = ('title', 'category__name', 'publisher__name', 'book_authors__author__last_name')
    list_filter = ('category', 'publisher', 'published_date')
    ordering = ('-published_date',)
    fields = ('title', 'category', 'created_at', 'updated_at', 'published_date', 'cover')
    readonly_fields = ('published_date', 'updated_at', 'created_at')

    # @admin.action(description='Change book category to classic')
    # def to_classic(self, request, queryset):
    #     classic = CategoryModel.objects.get(slug='classic')
    #     res = queryset.update(category=classic, updated_at=timezone.now())
    #     self.message_user(request, f'Changed book category to classic = {res}', messages.SUCCESS)

    actions = [to_classic]


    @admin.display(description='Book Photo')
    def display_cover(self, obj):
        if not obj.cover:
            return '-'

        return format_html('<img src="{}" alt="{}" style="width:50px;height:50px;" />',
                           obj.cover.url,
                           obj.title
                           )


    @admin.display(description='authors')
    def get_authors(self, obj):
        authors = '; '.join(item.last_name for item in obj.authors.all())
        return authors















