import os
from django.core.management.base import BaseCommand
from django.conf import settings
from database.models import Draft

class Command(BaseCommand):
    help = 'Import all draft templates from media folder'

    def handle(self, *args, **kwargs):
        folder_path = os.path.join(settings.MEDIA_ROOT, 'draft_templates')

        if not os.path.exists(folder_path):
            self.stdout.write(self.style.ERROR('Folder does not exist.'))
            return

        for filename in os.listdir(folder_path):
            if filename.endswith(('.docx', '.pdf', '.doc')):
                file_path = f'draft_templates/{filename}'

                if not Draft.objects.filter(title=filename).exists():
                    Draft.objects.create(
                        title=filename,
                        category="General",
                        file=file_path
                    )
                    self.stdout.write(self.style.SUCCESS(f'Imported {filename}'))

        self.stdout.write(self.style.SUCCESS('All drafts imported successfully!'))