from django.db import models

NULLABLE = {"null": True, "blank": True}


class Tasks(models.Model):
    TAGS = (
        ("Urgent", "Срочная"),
        ("On control", "На контроле"),
        ("Waiting", "В ожидании"),
        ("For discussion", "На обсуждение"),
        ("In progress", "В процессе"),
    )
    EXECUTION = (
        (True, "Выполнена"),
        (False, "Не выполнена"),
    )
    title = models.CharField(max_length=50, verbose_name="Название задачи")
    description = models.TextField(verbose_name="Описание задачи")
    due_date = models.DateTimeField(verbose_name="Срок исполнения", **NULLABLE)
    tags = models.CharField(max_length=50, choices=TAGS, verbose_name="Теги", **NULLABLE)
    is_completed = models.BooleanField(default=False, choices=EXECUTION, verbose_name="Задача выполнена?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
