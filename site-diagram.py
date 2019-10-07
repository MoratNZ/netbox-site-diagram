from dcim.constants import *
from dcim.models import Device, DeviceRole, DeviceType, Site
from extras.scripts import *


class SiteDiagram(Script):
    class Meta:
        name = "Site diagram"
        description = "Draw a logical diagram of a site"
        fields = ['site_name']

    site_name = ObjectVar(
        description="Site to draw",
        queryset=Site.objects.filter()
    )

    def run(self, data):
        devices = Device.objects.filter(
            site=data['site_name']
        )

        return data['site_name']
