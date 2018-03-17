import graphene
from graphene_django import DjangoObjectType

from .models import Blog


class BlogType(DjangoObjectType):
    class Meta:
        model = Blog


class Query(graphene.ObjectType):
    blogs = graphene.List(BlogType)

    @staticmethod
    def resolve_blogs(self, info, **kwargs):
        return Blog.objects.all()