from django.db import models

# Create your models here.
class Todolist(models.Model):

    status_choices = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=10, 
        choices=status_choices, 
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    note = models.ForeignKey(
        'notes.Note', 
        on_delete=models.CASCADE, 
        related_name='todolists',
        null=True,
        blank=True
    )

    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='todolists'
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Todolist'
        verbose_name_plural = 'Todolists'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'user'],
                 name='unique_todolist_title_per_user'
            )
        ]


    def __str__(self):
        return self.title