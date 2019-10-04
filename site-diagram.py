from extras.scripts import scripts
from dcim.constants import *
from dcim.models import Site


class SiteDiagram(Script):

    class Meta:
        name = "Site Diagram"
        description = "Generate a topology diagram for a site"
        fields = ["siteName"]

        siteName = ObjectVar(
            description="Site",
            querySet=Site.objects.filter()
        )

    def run(self, data):
        pass
