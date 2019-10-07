from dcim.constants import *
from dcim.models import Device, DeviceRole, DeviceType, Site
from extras.scripts import *


class SiteDiagram(Script):
    class Meta:
        name = "Site diagram"
        description = "Draw a logical diagram of a site"
        fields = ['site_code']

    site_code = ObjectVar(
        description="Site to draw",
        queryset=DeviceType.objects.filter(
            manufacturer__name='Cisco',
        )
    )

    def run(self, data):
        pass
