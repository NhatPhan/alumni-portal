from django.contrib import admin

from users.models import UserProfile, Project, Education, Job, Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'position_map',)

    def position_map(self, instance):
        if instance.position is not None:
            return '<img src="http://maps.googleapis.com/maps/api/staticmap?center=%(latitude)s,%(longitude)s&zoom=%(zoom)s&size=%(width)sx%(height)s&maptype=roadmap&markers=%(latitude)s,%(longitude)s&sensor=false&visual_refresh=true&scale=%(scale)s" width="%(width)s" height="%(height)s">' % {
                'latitude': instance.position.latitude,
                'longitude': instance.position.longitude,
                'zoom': 15,
                'width': 100,
                'height': 100,
                'scale': 2
            }
    position_map.allow_tags = True


admin.site.register(Location, LocationAdmin)
admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Job)