from django.contrib import admin
from django.http import HttpResponse
from django.core import serializers
from .models import Post
# Register your models here.

def export_as_json(modeladmin , request , queryset):
    response = HttpResponse(content_type = "application/json")

    serializers.serialize("json" , queryset , stream= response)

    return response

def make_published(modeladmin , request , queryset):
    result = queryset.update(status = 'published')
    if result == 1:
        message_bit = "1 post was"
    else:
        message_bit = "{} post were".format(result)
    modeladmin.message_user(request , "{} successfully marked as published.".format(message_bit))


def make_draft(modeladmin , request , queryset):
    result = queryset.update(status = 'draft')
    if result == 1:
        message_bit = "1 post was"
    else:
        message_bit = "{} post were".format(result)
    modeladmin.message_user(request , "{} successfully marked as draft.".format(message_bit))




make_published.short_description = 'Mark selected posts as published'
make_draft.short_description = 'Mark selected posts as draft'
export_as_json.short_description = 'Export selected posts as json request'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title' , 'slug' , 'publish' , 'status')
    list_filter = ('publish' , 'status')
    search_fields = ('title' , 'body')
    ordering = ['status' , 'publish']
    prepopulated_fields = {'slug': ('title',)}
    actions = [make_published , make_draft , export_as_json]

# admin.site.register(Post , PostAdmin)