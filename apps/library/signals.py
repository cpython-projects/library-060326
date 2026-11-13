import logging


from django.db.models.signals import post_save, m2m_changed, pre_save
from django.dispatch import receiver
from django.utils.text import slugify



from apps.library.models import BookModel, CategoryModel, BorrowModel
from apps.library.utils import send_email_borrow_book


logger = logging.getLogger(__name__)

@receiver(post_save, sender=BookModel, dispatch_uid="book_post_save")
def create_book(sender, instance, created, raw, **kwargs):
    if raw:
        return
    if created:
        logger.info(f"Book {instance.pk} {instance.title} created successfully")
    else:
        logger.info(f"Book {instance.pk} {instance.title} updated successfully")


# post_save.connect(create_book, sender=BookModel, dispatch_uid="book_post_save")


@receiver(m2m_changed, sender=BookModel.genres.through, dispatch_uid="genres_m2m_changed")
def update_genres(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        pass
    elif action == "post_remove":
        pass
    elif action == "post_clear":
        pass


@receiver(pre_save, sender=CategoryModel, dispatch_uid="category_save")
def create_update_category(sender, instance, raw, **kwargs):
    if raw:
        return
    if not instance.slug:
        instance.slug = slugify(instance.name, allow_unicode=True)


@receiver(post_save, sender=BorrowModel, dispatch_uid="borrow_save")
def create_borrow(sender, instance, created, raw, **kwargs):
    if raw or not created:
        pass
    send_email_borrow_book.aenqueue(borrow_id=instance.pk)