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

    title = models.CharField(max_length=100)
    description = models.TextField()
    risk = models.IntegerField(choices=RISK_PROFILE,default=NONE)

    def __str__(self):
        return '{}'.format(self.title)

class Ticker(models.Model):
    ticker = models.CharField(max_length=20)
    ticker_description = models.TextField()
    asset_class = models.CharField(max_length=20)


    class Meta:
        ordering = ('ticker','ticker_description')

class Holding(models.Model):
    ticker = models.ForeignKey(Ticker, on_delete=models.DO_NOTHING)
    shares = models.DecimalField(max_digits=100, decimal_places=4)
    model = models.ForeignKey(Model, on_delete=models.DO_NOTHING)
