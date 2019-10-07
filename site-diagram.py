from dcim.constants import *
from dcim.models import Device, DeviceRole, DeviceType, Site
from extras.scripts import *


class SiteDiagram(Script):
    class Meta:
        name = "Site diagram"
        description = "Draw a logical diagram of a site"
        fields = ['site_name', 'switch_count', 'switch_model']

    site_name = StringVar(
        description="Name of the new site"
    )
    switch_count = IntegerVar(
        description="Number of access switches to create"
    )
    switch_model = ObjectVar(
        description="Access switch model",
        queryset=DeviceType.objects.filter(
            manufacturer__name='Cisco',
        )
    )

    def run(self, data):
        pass
