from django.http import StreamingHttpResponse
import time
from rest_framework import generics, status
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserProfile, Category, PostModel, CommentModel
from .serializers import UserProfileSerializer, FilePathSerializer, CategorySerializer, PostSerializer, \
    CommentSerializer
from .utils import WithExtraDetailPageNumberPagination
from .tasks import count_words_in_file



class UserProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class = WithExtraDetailPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'name']
    ordering_fields = ['name']


class UserProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer



def stream_response(request):
    def event_stream():
        yield 'Tes: Hello, Siri!\n\n'
        time.sleep(2)
        yield 'Siri: Hi, Tes! How can I help you today?\n\n'
        time.sleep(2)
        yield "Tes: I'm working on the ProfileHub project. Could you assist me with some streaming data?\n\n"
        time.sleep(2)
        yield 'Siri: Absolutely, Tes! Streaming data is an excellent way to provide real-time updates.\n\n'
        time.sleep(2)
        yield "Tes: That's great to hear! I'm excited to implement it.\n\n"
        time.sleep(2)
        yield 'Siri: Indeed! Let me know if you need any further assistance.\n\n'
        time.sleep(2)
        yield 'Tes: Will do, Siri. Thanks for your help!\n\n'
        time.sleep(2)
        yield "Siri: You're welcome, Tes. Have a productive day!\n\n"
        time.sleep(2)
        yield 'Siri: By the way, have you considered using WebSockets for real-time communication?\n\n'
        time.sleep(2)
        yield 'Tes: Thats a good point, Siri. Ill look into it.\n\n'
        time.sleep(2)
        yield 'Siri: WebSockets offer bidirectional communication, which could be beneficial for your project.\n\n'
        time.sleep(2)
        yield "Tes: I appreciate the suggestion, Siri. I'll explore both options.\n\n"
        time.sleep(2)
        yield 'Siri: Sounds like a plan, Tes. Let me know if you need further guidance.\n\n'
        time.sleep(2)
        yield 'Tes: Absolutely, Siri. Thanks again for your assistance!\n\n'
        time.sleep(2)
        yield 'Siri: Anytime, Tes. Have a wonderful day!\n\n'
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


class CountWordsView(APIView):
    def post(self, request, format=None):
        serializer = FilePathSerializer(data=request.data)
        if serializer.is_valid():
            file_path = serializer.validated_data['file_path']
            count_words_in_file.delay(file_path)
            return Response({'message': 'Task started'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostListAPIView(generics.ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'title' in self.request.query_params and self.request.query_params['title'].strip():
            queryset = queryset.filter(title__istartswith=self.request.query_params.get('title'))
        if 'recent_comments' in self.request.query_params:
            queryset = queryset.order_by('-comments__publication_date')
        if 'created_at' in self.request.query_params:
            queryset = queryset.order_by('-created_at')
        return queryset


class PostCreateAPIView(generics.CreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
