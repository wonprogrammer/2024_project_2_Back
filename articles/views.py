from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article
from articles.serializers import ArticleSerializer

# Create your views here.

# 시리얼라이즈 전 Data를 딕셔너리 형태로 변환하는 작업
# @api_view(['GET'])
# def index(request):
#     articles = Article.objects.all()
#     article = articles[0]
#     article_data = {
#         'title':article.title,
#         'content':article.content,
#     }
#     return Response(article_data)

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.error_messages)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # return Response(serializer.error_messages) | 보안상 이유로 Front에서 어떤 이유로 에러가 났는지 확인이 가능하기 때문에 해당 코드는 지양
