from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import os

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'

    def save(self, *args, **kwargs):
        if self.photo:
            self.photo.seek(0)
            original_size = self.photo.size
            # print(f"Original image size: {original_size / 1024:.2f} KB")
            if original_size > 512 * 1024:  # If image > 1MB
                img = Image.open(self.photo)

                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                img.thumbnail((800, 800))

                # Start compressing in loop
                quality = 70
                while True:
                    buffer = BytesIO()
                    img.save(buffer, format='JPEG', quality=quality, optimize=True)
                    size_kb = buffer.getbuffer().nbytes / 1024
                    # print(f"Trying quality={quality}, size={size_kb / 1024:.2f} KB")

                    if size_kb < 512 * 1024 or quality <= 20:
                        # print(f"Final compressed image size: { size_kb/ 1024:.2f} KB")
                        break  # Stop if under 500kb or quality is too low

                    quality -= 5  

                buffer.seek(0)
                self.photo = InMemoryUploadedFile(
                    buffer,
                    'ImageField',
                    f"{self.photo.name.split('.')[0]}.jpg",
                    'image/jpeg',
                    buffer.getbuffer().nbytes,
                    None
                )

        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.photo and os.path.isfile(self.photo.path):
            os.remove(self.photo.path)
        super().delete(*args, **kwargs)