from django.db import models

class Model(models.Model):
    NONE = 0
    CONSERVATIVE = 1
    BALANCED = 2
    GROWTH = 3
    AGGRESSIVE = 4
    RISK_PROFILE = (
        (NONE, 'None Selected'),
        (CONSERVATIVE, 'Conservative'),
        (BALANCED, 'Balanced'),
        (GROWTH, 'Growth'),
        (AGGRESSIVE, 'Aggresive'),
    )

    title = models.CharField(
        max_length=140)
    description = models.TextField()
    risk = models.IntegerField(
        choices=RISK_PROFILE,
        default=NONE)

    def __str__(self):
        return '{}'.format(
            self.title)
