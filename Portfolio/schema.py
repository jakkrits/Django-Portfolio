import graphene

import jobs.schema
import blog.schema


class Query(jobs.schema.Query, blog.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
