from django.contrib import admin

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
    Publisher,
)

admin.site.register(AuthorModel)
admin.site.register(AuthorDetailModel)
admin.site.register(CategoryModel)
admin.site.register(GenreModel)
admin.site.register(Publisher)
admin.site.register(LibraryModel)
admin.site.register(BookAuthorModel)
admin.site.register(PostModel)
admin.site.register(BorrowModel)


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'get_authors', 'publisher', 'published_date')
    list_editable = ('title', 'category')
    list_select_related = ('category', 'publisher')

    search_fields = ('title', 'category__name', 'publisher__name', 'book_authors__author__last_name')
    list_filter = ('category', 'publisher', 'published_date')
    ordering = ('-published_date',)
    fields = ('title', 'category', 'created_at', 'updated_at', 'published_date')
    readonly_fields = ('published_date', 'updated_at', 'created_at')




    @admin.display(description='authors')
    def get_authors(self, obj):
        authors = '; '.join(item.last_name for item in obj.authors.all())
        return authors












