from django import forms
from Main.models import Subscriber

class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = (
            'email',
        )

        widgets = {
            'email': forms.EmailInput(attrs={
                'class':'form-control w-75 py-4 col-md-10',

                'placeholder':'Enter email address'
            })
        }
