from rest_framework.exceptions import ValidationError
from rest_framework.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status

from apps.library.models import BorrowModel
from apps.library.serializers import BorrowSerializer


class BorrowListCreateAPIView(APIView):
    STATUSES = ['returned', 'overdue', 'holding']

    def get(self, request):

        params = request.query_params
        today = timezone.datetime.now().date()

        borrows = (BorrowModel.objects
                   .select_related('member', 'book', 'library')
                   .prefetch_related('book__authors')
                   )

        if status_ := params.get('status'):
            status_ = status_.strip().lower()
            if status_ not in self.STATUSES:
                raise ValidationError({'status': f'Available statuses are {self.STATUSES}'})

            if status_ == 'returned':
                borrows = borrows.filter(returned_date__isnull=False)
            elif status_ == 'overdue':
                borrows = borrows.filter(returned_date__isnull=True, due_date__lt=today)
            else:
                borrows = borrows.filter(returned_date__isnull=True, due_date__gte=today)

        if member := params.get('member'):
            borrows = borrows.filter(member__email=member)


        serializer = BorrowSerializer(borrows, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)