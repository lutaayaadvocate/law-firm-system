import os
from django.core.management.base import BaseCommand
from django.conf import settings
from library.models import LibraryDocument

class Command(BaseCommand):
    help = "Import precedent files from PRECEDENTS folder"

    def handle(self, *args, **kwargs):
        folder_path = os.path.join(settings.MEDIA_ROOT, "library", "PRECEDENTS")

        if not os.path.exists(folder_path):
            self.stdout.write(self.style.ERROR("PRECEDENTS folder not found."))
            return

        files = os.listdir(folder_path)
        count = 0

        for file_name in files:
            file_path = os.path.join(folder_path, file_name)

            if os.path.isfile(file_path):
                if not LibraryDocument.objects.filter(title=file_name).exists():
                    LibraryDocument.objects.create(
                        title=file_name,
                        category="precedent",
                        document=f"library/PRECEDENTS/{file_name}"
                    )
                    count += 1

        self.stdout.write(self.style.SUCCESS(f"{count} precedents imported successfully."))