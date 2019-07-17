from django.contrib import admin

from .models import Organisation
from .models import Testee
from .models import Test
from .models import Status
from .models import Attempt

admin.site.register(Organisation)
admin.site.register(Testee)
admin.site.register(Test)
admin.site.register(Status)
admin.site.register(Attempt) # TODO 