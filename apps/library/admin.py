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
    MemberModel,
    PostModel,
    Publisher,
)

admin.site.register(AuthorModel)
admin.site.register(AuthorDetailModel)
admin.site.register(CategoryModel)
admin.site.register(GenreModel)
admin.site.register(Publisher)
admin.site.register(LibraryModel)
admin.site.register(BookModel)
admin.site.register(BookAuthorModel)
admin.site.register(MemberModel)
admin.site.register(PostModel)
admin.site.register(BorrowModel)
