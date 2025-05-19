from import_export import resources
from .models import UploadXL

class UploadXLResource(resources.ModelResource):
    class Meta:
        model = UploadXL