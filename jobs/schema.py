import graphene
from graphene_django import DjangoObjectType

from .models import Job


class JobType(DjangoObjectType):
    class Meta:
        model = Job


class Query(graphene.ObjectType):
    jobs = graphene.List(JobType)

    @staticmethod
    def resolve_jobs(self, info, **kwargs):
        return Job.objects.all()

