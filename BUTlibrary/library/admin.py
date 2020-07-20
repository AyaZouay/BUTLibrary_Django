from django.contrib import admin
from accounts.models import *
from library.models import *

admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Borrow)
