from django import forms
from django.forms import ModelForm
from .models import Score

class ScoreForm(ModelForm):
    class Meta:
        model= Score
        fields = (
            'song_name',
            'difficulty',
            'length_min',
            'length_sec',
            'bpm',
            'star_rating',
            'count_r300',
            'count_300',
            'count_200',
            'count_100',
            'count_50',
            'count_0'
        )
