from django.core.mail import send_mail
from django.conf import settings
from django.tasks import task
from apps.library.models import BorrowModel


@task
def send_email_borrow_book(borrow_id):
    borrow = BorrowModel.objects.select_related('member', 'book').get(pk=borrow_id)
    send_mail(
        subject=f"Book {borrow.book.title} borrowed",
        message=f"Reader {borrow.member} borrowed book {borrow.book.title} due date {borrow.due_date:%d/%m/%Y}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=settings.LIBRARIANS_EMAILS,
    )