from dcim.constants import *
from dcim.models import Device, DeviceRole, DeviceType, Site
from extras.scripts import *


class SiteDiagram(Script):

    class Meta:
        name = "Site Diagram"
        description = "Generate a topology diagram for a site"
        fields = ["site_name", "test_field"]

        test_field = StringVar(
            label="tst",
            descriptoin "test"
        )
        site_name = ObjectVar(
            label="site",
            description="Site to map",
            queryset=Site.objects.filter()
        )

    def run(self, data):
        pass
