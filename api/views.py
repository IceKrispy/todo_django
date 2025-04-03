from rest_framework import viewsets
from .models import TodoItem
from .serializers import TodoItemSerializer
from django.views.generic import TemplateView

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class HomePageView(TemplateView):
    template_name = 'app.js'