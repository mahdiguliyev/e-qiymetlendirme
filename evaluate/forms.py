from django import forms
from .models import EvaluationOrder,Apartment,PrivateHouse,EnterpriseComplex,NonResidentialArea,NonResidentialBuilding,LandPlot,OtherRealState
from .models import Electronica,Gold,HouseholdAppliance,OtherMoveableState,Car,SpecialTechnique,SemiTrailer,OtherTransportation

class EvaluationOrderForm(forms.ModelForm):

    class Meta:
        model = EvaluationOrder
        fields = '__all__'

class Apartment(forms.ModelForm):

    class Meta:
        model = Apartment
        fields = '__all__'

class PrivateHouse(forms.ModelForm):

    class Meta:
        model = PrivateHouse
        fields = '__all__'

class EnterpriseComplex(forms.ModelForm):

    class Meta:
        model = EnterpriseComplex
        fields = '__all__'

class NonResidentialArea(forms.ModelForm):

    class Meta:
        model = NonResidentialArea
        fields = '__all__'

class NonResidentialBuilding(forms.ModelForm):

    class Meta:
        model = NonResidentialBuilding
        fields = '__all__'

class LandPlot(forms.ModelForm):

    class Meta:
        model = LandPlot
        fields = '__all__'

class OtherRealState(forms.ModelForm):

    class Meta:
        model = OtherRealState
        fields = '__all__'

class Electronica(forms.ModelForm):

    class Meta:
        model = Electronica
        fields = '__all__'

class Gold(forms.ModelForm):

    class Meta:
        model = Gold
        fields = '__all__'

class HouseholdAppliance(forms.ModelForm):

    class Meta:
        model = HouseholdAppliance
        fields = '__all__'

class OtherMoveableState(forms.ModelForm):

    class Meta:
        model = OtherMoveableState
        fields = '__all__'

class Car(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

class SpecialTechnique(forms.ModelForm):

    class Meta:
        model = SpecialTechnique
        fields = '__all__'

class SemiTrailer(forms.ModelForm):

    class Meta:
        model = SemiTrailer
        fields = '__all__'

class OtherTransportation(forms.ModelForm):

    class Meta:
        model = OtherTransportation
        fields = '__all__'

