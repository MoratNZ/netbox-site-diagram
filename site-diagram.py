from dcim.constants import *
from dcim.models import Device, DeviceRole, DeviceType, Site
from extras.scripts import *


class SiteDiagram(Script):

    class Meta:
        name = "Site Diagram"
        description = "Generate a topology diagram for a site"
        fields = ["siteName"]

        siteName = ObjectVar(
            description="Site to map",
            querySet=Site.objects.filter()
        )

    def run(self, data):
        pass
