from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article

# Create your views here.

@api_view(['GET'])
def index(request):
    articles = Article.objects.all()
    article = articles[0]
    article_data = {
        'title':article.title,
        'content':article.content,
    }
    return Response(article_data)
