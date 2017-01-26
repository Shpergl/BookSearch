from django.contrib import admin

from booksearch.models import Book, Page, Section

admin.site.register([Book])
admin.site.register([Section])
admin.site.register([Page])

