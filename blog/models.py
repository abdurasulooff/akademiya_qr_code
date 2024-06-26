from django.db import models
import uuid
from django.urls import reverse


class Fakultet(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Kafedra(models.Model):
    name = models.CharField(max_length=200)
    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE, related_name="kafedra")

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    kafedra = models.ForeignKey(Kafedra, on_delete=models.CASCADE, related_name="teacher")

    def __str__(self):
        return self.name


class Items(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=50)
    audio_uz = models.FileField(upload_to='musics/uz',
                             blank=True,
                             null=True,
                             )
    audio_ru = models.FileField(upload_to='musics/ru',
                                blank=True,
                                null=True,
                                )
    audio_en = models.FileField(upload_to='musics/en',
                                blank=True,
                                null=True,
                                )
    video_uz = models.FileField(upload_to="video/uz",
                             blank=True,
                             null=True,
                             )
    video_ru = models.FileField(upload_to="video/ru",
                             blank=True,
                             null=True,
                             )
    video_en = models.FileField(upload_to="video/en",
                             blank=True,
                             null=True,
                             )
    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
    )
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,
                                related_name="item",
                                )

    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE,
                                 related_name="item",
                                 )

    def get_absolute_url(self):
        return reverse("items_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
