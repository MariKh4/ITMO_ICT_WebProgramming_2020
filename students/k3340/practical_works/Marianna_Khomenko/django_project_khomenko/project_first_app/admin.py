from django.contrib import admin

from .models import User
admin.site.register(User)

from .models import DriversLicense
admin.site.register(DriversLicense)

from .models import Car
admin.site.register(Car)

from .models import Possession
admin.site.register(Possession)

from .models import GeeksModel
admin.site.register(GeeksModel)