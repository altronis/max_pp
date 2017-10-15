from django.db import models


class Score(models.Model):
    song_name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    length_min = models.PositiveIntegerField(default=0)
    length_sec = models.PositiveIntegerField(default=0)
    length = models.IntegerField(default=0)
    bpm = models.IntegerField(default=120)
    star_rating = models.FloatField(default=1)
    count_r300 = models.IntegerField(default=0)
    count_300 = models.IntegerField(default=0)
    count_200 = models.IntegerField(default=0)
    count_100 = models.IntegerField(default=0)
    count_50 = models.IntegerField(default=0)
    count_0 = models.IntegerField(default=0)
    acc = models.DecimalField(default=100, decimal_places=2, max_digits=5)
    max_pp = models.IntegerField(default=20)
    pp = models.IntegerField(default=20)
    player = models.CharField(max_length=100, default='admin')

    def save(self, *args, **kwargs):
        self.length = 60 * self.length_min + self.length_sec
        total_notes = self.count_r300+self.count_300+self.count_200+self.count_100+self.count_50+self.count_0
        self.acc = round((self.count_r300*5 + self.count_300*4 + self.count_200*2 - self.count_50*6 - self.count_0*12) / (total_notes*5) * 100, 2)
        stars = int(self.star_rating)
        self.max_pp = 20
        while stars > 1:
            self.max_pp *= (2-stars/10+0.2)
            stars -= 1
        stars = int(self.star_rating)
        self.max_pp = int(self.max_pp * ((2-stars/10+0.1) ** (self.star_rating-stars)))
        self.pp = int(self.max_pp / (1.5 ** ((100-self.acc)/10)))

        super(Score, self).save(*args, **kwargs)

    def __str__(self):
        return self.song_name

    def display_star(self):
        if len(str(self.star_rating)) == 3:
            return str(self.star_rating)+'0'
        elif len(str(self.star_rating)) == 4:
            return str(self.star_rating)
        else:
            return "ERROR"
