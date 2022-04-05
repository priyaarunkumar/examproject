from django import forms

from .models import Quantity,Prize


class PersonCreation(forms.ModelForm):
    class Meta:
        model = Quantity
        fields = '__all__'

    def __init__(self, *args, **kwargs):


        super().__init__(*args, **kwargs)
        self.fields['prize'].queryset = Prize.objects.none()

        if 'food' in self.data:
            try:
                food_id = int(self.data.get('food'))
                self.fields['prize'].queryset = Prize.objects.filter(food_id=food_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset

        elif self.instance.pk:
            self.fields['prize'].queryset = self.instance.food.prize_set.order_by('name')

