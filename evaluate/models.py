from django.db import models
from user.models import User
from ckeditor.fields import RichTextField
from django.core.validators import MinLengthValidator

class Category(models.Model):
    category_name             = models.CharField(max_length=255, unique =True)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    category_name  =     models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = "Kateqoriya",related_name="categories")
    subcategory_name =   models.CharField(max_length=255, unique =True)

    def __str__(self):
        return self.subcategory_name

class EvaluationCompany(models.Model):
    evacompany_name         = models.CharField(max_length=255, unique =True)
    
    def __str__(self):
        return self.evacompany_name

class Worker(models.Model):
    company_name        = models.ForeignKey(EvaluationCompany, on_delete=models.CASCADE, verbose_name = "Qiymətləndirici təşkilat",related_name="workers")
    user                = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "İstifadəçi",related_name="users",null=True)
    worker_name         = models.CharField(max_length=55,verbose_name="Adı")
    worker_sirname      = models.CharField(max_length=55,verbose_name="Familiya")
    worker_fin          = models.CharField(max_length=7,validators=[MinLengthValidator(7)],verbose_name="Fin")
    is_bm               = models.BooleanField(default=False)
    is_as               = models.BooleanField(default=False)
    worker_created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.worker_fin

class EvaluationOrder(models.Model):
    company_name            = models.ManyToManyField(EvaluationCompany, verbose_name = "Qiymətləndirici təşkilat",related_name="orders")
    order_name              = models.CharField(max_length=255, verbose_name="Sifarişin adı")
    subcategory_name        = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, verbose_name = "Kateqoriya",related_name="subcategories_evaluationorder")
    order_law_decision      = models.CharField(max_length=255, verbose_name="Rayon məhkəməsinin qərarı")
    order_deptor            = models.CharField(max_length=255, verbose_name="Borclu")
    order_claimant          = models.CharField(max_length=255, verbose_name="Tələbkar")
    order_information       = RichTextField(verbose_name="Əmlak haqqında məlumat")
    order_document          = models.FileField(verbose_name="Əmlakın texniki sənədlərini daxil edin", upload_to="order_documents/%Y/")
    order_keep_date_location= models.CharField(max_length=255, verbose_name="Saxlanma yeri və tarix")
    order_mobile            = models.CharField(max_length=13, verbose_name="Sifarişçinin mobil nömrəsi")
    is_done                 = models.BooleanField(default=False)
    order_created_date      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_name

class Apartment(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_apartment")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    building_floor =                models.IntegerField(verbose_name="Binanın mərtəbəliliyi")
    located_floor =                 models.IntegerField(verbose_name="Yerləşdiyi mərtəbə")
    room_number =                   models.IntegerField(verbose_name="Otaqların sayı")
    total_area =                    models.CharField(max_length=50, verbose_name="Ümumi sahəsi")
    residential_area =              models.CharField(max_length=50, verbose_name="Yaşayış sahəsi")
    auxiliary_area =                models.CharField(max_length=50, verbose_name="Köməkçi sahə")
    balcony =                       models.BooleanField(verbose_name="Eyvan")
    sunitary_junction =             models.BooleanField(verbose_name="Sanitar qovşağı")
    height =                        models.CharField(max_length=50, verbose_name="Hündürlüyü")
    project =                       models.CharField(max_length=255, verbose_name="Layihə")
    blocks_number =                 models.IntegerField(verbose_name="Blokların sayı")
    interior_exterior_walls =       models.CharField(max_length=255, verbose_name="Daxili və xarici divarları")
    floor =                         models.CharField(max_length=255, verbose_name="Döşəməsi")
    ceiling =                       models.CharField(max_length=255, verbose_name="Tavan")
    window =                        models.CharField(max_length=255, verbose_name="Pəncərə")
    interior_door =                 models.CharField(max_length=255, verbose_name="Daxili qapı")
    interior_decoration =           models.CharField(max_length=255, verbose_name="Daxili bəzək işləri")
    entry_door =                    models.CharField(max_length=255, verbose_name="Giriş qapısı")
    sanitary_equioment =            models.CharField(max_length=255, verbose_name="Sanitar texniki təchizat (o cümlədən su, qaz, elektrik)")
    general_condition =             models.CharField(max_length=255, verbose_name="Ümumi vəziyyəti")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class PrivateHouse(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_privatehouse")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    building_floor =                models.IntegerField(verbose_name="Fərdi-yaşayış evinin mərtəbəliliyi")
    room_number =                   models.IntegerField(verbose_name="Otaqların sayı")
    total_area =                    models.CharField(max_length=50, verbose_name="Ümumi sahəsi")
    residential_area =              models.CharField(max_length=50, verbose_name="Yaşayış sahəsi")
    auxiliary_area =                models.CharField(max_length=50, verbose_name="Köməkçi sahə")
    land_area =                     models.CharField(max_length=255, verbose_name="Torpaq sahəsi")
    interior_exterior_walls =       models.CharField(max_length=255, verbose_name="Daxili və xarici divarları")
    floor =                         models.CharField(max_length=255, verbose_name="Döşəməsi")
    ceiling =                       models.CharField(max_length=255, verbose_name="Tavan")
    window =                        models.CharField(max_length=255, verbose_name="Pəncərə")
    interior_door =                 models.CharField(max_length=255, verbose_name="Daxili qapı")
    interior_decoration =           models.CharField(max_length=255, verbose_name="Daxili bəzək işləri")
    entry_door =                    models.CharField(max_length=255, verbose_name="Giriş qapısı")
    sanitary_equioment =            models.CharField(max_length=255, verbose_name="Sanitar texniki təchizat (o cümlədən su, qaz, elektrik)")
    roof =                          models.CharField(max_length=255, verbose_name="Dam örtüyü")
    general_condition =             models.CharField(max_length=255, verbose_name="Ümumi vəziyyəti")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.order_number

class EnterpriseComplex(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_enterprisecomplex")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    building_floor =                models.IntegerField(verbose_name="Mərtəbəliliyi")
    room_number =                   models.IntegerField(verbose_name="Otaqların sayı")
    total_area =                    models.CharField(max_length=50, verbose_name="Ümumi sahəsi")
    residential_area =              models.CharField(max_length=50, verbose_name="Yaşayış sahəsi")
    auxiliary_area =                models.CharField(max_length=50, verbose_name="Köməkçi sahə")
    interior_exterior_walls =       models.CharField(max_length=255, verbose_name="Daxili və xarici divarları")
    floor =                         models.CharField(max_length=255, verbose_name="Döşəməsi")
    ceiling =                       models.CharField(max_length=255, verbose_name="Tavan")
    window =                        models.CharField(max_length=255, verbose_name="Pəncərə")
    interior_door =                 models.CharField(max_length=255, verbose_name="Daxili qapı")
    interior_decoration =           models.CharField(max_length=255, verbose_name="Daxili bəzək işləri")
    entry_door =                    models.CharField(max_length=255, verbose_name="Giriş qapısı")
    sanitary_equioment =            models.CharField(max_length=255, verbose_name="Sanitar texniki təchizat (o cümlədən su, qaz, elektrik)")
    roof =                          models.CharField(max_length=255, verbose_name="Dam örtüyü")
    general_condition =             models.CharField(max_length=255, verbose_name="Ümumi vəziyyəti")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class NonResidentialBuilding(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_nonresidentialbuilding")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    building_floor =                models.IntegerField(verbose_name="Mərtəbəliliyi")
    total_area =                    models.CharField(max_length=50, verbose_name="Ümumi sahəsi")
    residential_area =              models.CharField(max_length=50, verbose_name="Yaşayış sahəsi")
    auxiliary_area =                models.CharField(max_length=50, verbose_name="Köməkçi sahə")
    land_area =                     models.CharField(max_length=255, verbose_name="Torpaq sahəsi")
    interior_exterior_walls =       models.CharField(max_length=255, verbose_name="Daxili və xarici divarları")
    floor =                         models.CharField(max_length=255, verbose_name="Döşəməsi")
    ceiling =                       models.CharField(max_length=255, verbose_name="Tavan")
    window =                        models.CharField(max_length=255, verbose_name="Pəncərə")
    interior_door =                 models.CharField(max_length=255, verbose_name="Daxili qapı")
    interior_decoration =           models.CharField(max_length=255, verbose_name="Daxili bəzək işləri")
    entry_door =                    models.CharField(max_length=255, verbose_name="Giriş qapısı")
    sanitary_equioment =            models.CharField(max_length=255, verbose_name="Sanitar texniki təchizat (o cümlədən su, qaz, elektrik)")
    general_condition =             models.CharField(max_length=255, verbose_name="Ümumi vəziyyəti")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class NonResidentialArea(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_nonresidentialarea")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    building_floor =                models.IntegerField(verbose_name="Mərtəbəliliyi")
    room_number =                   models.IntegerField(verbose_name="Otaqların sayı")
    total_area =                    models.CharField(max_length=50, verbose_name="Ümumi sahəsi")
    residential_area =              models.CharField(max_length=50, verbose_name="Yaşayış sahəsi")
    auxiliary_area =                models.CharField(max_length=50, verbose_name="Köməkçi sahə")
    interior_exterior_walls =       models.CharField(max_length=255, verbose_name="Daxili və xarici divarları")
    floor =                         models.CharField(max_length=255, verbose_name="Döşəməsi")
    ceiling =                       models.CharField(max_length=255, verbose_name="Tavan")
    window =                        models.CharField(max_length=255, verbose_name="Pəncərə")
    interior_door =                 models.CharField(max_length=255, verbose_name="Daxili qapı")
    interior_decoration =           models.CharField(max_length=255, verbose_name="Daxili bəzək işləri")
    entry_door =                    models.CharField(max_length=255, verbose_name="Giriş qapısı")
    sanitary_equioment =            models.CharField(max_length=255, verbose_name="Sanitar texniki təchizat (o cümlədən su, qaz, elektrik)")
    roof =                          models.CharField(max_length=255, verbose_name="Dam örtüyü")
    general_condition =             models.CharField(max_length=255, verbose_name="Ümumi vəziyyəti")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class LandPlot(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_landplot")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    located_area =                  models.CharField(max_length=255, verbose_name="Yerləşdiyi ərazi")
    land_area =                     models.CharField(max_length=255, verbose_name="Torpaq sahəsi")
    land_purpose =                  models.CharField(max_length=255, verbose_name="Torpağın təyinatı")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class OtherRealState(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_otherrealestate")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    technical_indicators =          RichTextField(verbose_name="Texniki göstəriciləri")
    technical_characteristics =     RichTextField(verbose_name="Texniki xarakterizələri")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class Electronica(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_electronica")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    order_name =                    models.CharField(max_length=255, verbose_name="Sifarişin adı")
    number =                        models.IntegerField(verbose_name="Sayı")
    condition =                     models.CharField(max_length=255, verbose_name="Vəziyyəti")
    general_information =           RichTextField(verbose_name="Ümumi məlumat")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class Gold(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_gold")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    order_name =                    models.CharField(max_length=255, verbose_name="İlkin görüşdə adı")
    number =                        models.IntegerField(verbose_name="Sayı (dəst, cüt, ədəd)")
    weight =                        models.CharField(max_length=100, verbose_name="Lom vəziyyətdə ümumi çəkisi (qram)")
    earring =                       models.CharField(max_length=100, verbose_name="Əyyar")
    note =                          RichTextField(verbose_name="Qeyd", null=True)
    price_for_earring =             models.FloatField(verbose_name="Əyyara görə qiymət (AZN)")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class HouseholdAppliance(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_householdappliance")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")  
    order_name =                    models.CharField(max_length=255, verbose_name="Adı")
    color =                         models.CharField(max_length=100, verbose_name="Rəngi") 
    number =                        models.IntegerField(verbose_name="Sayı")
    price_for_one =                 models.FloatField(verbose_name="Bir ədədinin qiyməti")
    condition =                     models.CharField(max_length=255, verbose_name="Vəziyyəti")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class OtherMoveableState(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_othermoveablestate")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    order_name =                    models.CharField(max_length=255, verbose_name="Adı")
    color =                         models.CharField(max_length=100, verbose_name="Rəngi") 
    general_information =           RichTextField(verbose_name="Ümumi məlumat")
    condition =                     models.CharField(max_length=255, verbose_name="Vəziyyəti")
    number =                        models.IntegerField(verbose_name="Sayı")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class Car(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_car")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    brand =                         models.CharField(max_length=100, verbose_name="Markası")
    tip =                           models.CharField(max_length=100, verbose_name="Tip")
    launched_year =                 models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Buraxılış ili")
    registration_plate =            models.CharField(max_length=7, verbose_name="Dövlət qeydiyyat nişanı")
    ban =                           models.CharField(max_length=100, verbose_name="Ban")
    color =                         models.CharField(max_length=50, verbose_name="Rəngi")
    fuel_type =                     models.CharField(max_length=50, verbose_name="Yanacaq növü")
    dwarf_number =                  models.CharField(max_length=100, verbose_name="Mükərrikin nömrəsi")
    engine_capacity =               models.CharField(max_length=100, verbose_name="Mühərrikin həcmi")
    texpassport_number =            models.CharField(max_length=100, verbose_name="Tex pasportun nömrəsi")
    texpassport_issuedate =         models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Tex pasportun verilmə tarixi")
    walking =                       models.CharField(max_length=100, verbose_name="Yürüş")
    wheels =                        models.CharField(max_length=100, verbose_name="Təkərləri")
    flashlights =                   models.CharField(max_length=100, verbose_name="Fənərləri")
    salon =                         models.CharField(max_length=100, verbose_name="Salon")
    wings =                         models.CharField(max_length=100, verbose_name="Qanadlar")
    doors =                         models.CharField(max_length=100, verbose_name="Qapılar")
    accumulator =                   models.CharField(max_length=100, verbose_name="Akumlyator")
    gearbox =                       models.CharField(max_length=100, verbose_name="Sürətli ötürücü qutusu")
    engine =                        models.CharField(max_length=100, verbose_name="Mühərriki")
    buffers =                       models.CharField(max_length=100, verbose_name="Buferlər")
    bottles =                       models.CharField(max_length=100, verbose_name="Şüşələr")
    air_conditioner =               models.BooleanField(verbose_name="Kondisioner")
    airbags =                       models.BooleanField(verbose_name="Təhlükəsizlik yastıqları")
    centralized_management_system = models.BooleanField(verbose_name="Mərkəzləşdirilmiş idarə etmə sistemi")
    audio_system =                  models.BooleanField(verbose_name="Audio sistem")
    general_condition =             models.CharField(max_length=255, verbose_name="Ümumi vəziyyəti")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class SpecialTechnique(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_specialtechnique")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    brand =                         models.CharField(max_length=100, verbose_name="Markası")
    tip =                           models.CharField(max_length=100, verbose_name="Tip")
    launched_year =                 models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Buraxılış ili")
    registration_plate =            models.CharField(max_length=7, verbose_name="Dövlət qeydiyyat nişanı")
    ban =                           models.CharField(max_length=100, verbose_name="Ban")
    color =                         models.CharField(max_length=50, verbose_name="Rəngi")
    fuel_type =                     models.CharField(max_length=50, verbose_name="Yanacaq növü")
    dwarf_number =                  models.CharField(max_length=100, verbose_name="Mükərrikin nömrəsi")
    engine_capacity =               models.CharField(max_length=100, verbose_name="Mühərrikin həcmi")
    texpassport_number =            models.CharField(max_length=100, verbose_name="Tex pasportun nömrəsi")
    texpassport_issuedate =         models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Tex pasportun verilmə tarixi")
    walking =                       models.CharField(max_length=100, verbose_name="Yürüş")
    wheels =                        models.CharField(max_length=100, verbose_name="Təkərləri")
    flashlights =                   models.CharField(max_length=100, verbose_name="Fənərləri")
    salon =                         models.CharField(max_length=100, verbose_name="Salon")
    wings =                         models.CharField(max_length=100, verbose_name="Qanadlar")
    doors =                         models.CharField(max_length=100, verbose_name="Qapılar")
    accumulator =                   models.CharField(max_length=100, verbose_name="Akumlyator")
    gearbox =                       models.CharField(max_length=100, verbose_name="Sürətli ötürücü qutusu")
    engine =                        models.CharField(max_length=100, verbose_name="Mühərriki")
    buffers =                       models.CharField(max_length=100, verbose_name="Buferlər")
    bottles =                       models.CharField(max_length=100, verbose_name="Şüşələr")
    air_conditioner =               models.BooleanField(verbose_name="Kondisioner")
    airbags =                       models.BooleanField(verbose_name="Təhlükəsizlik yastıqları")
    centralized_management_system = models.BooleanField(verbose_name="Mərkəzləşdirilmiş idarə etmə sistemi")
    audio_system =                  models.BooleanField(verbose_name="Audio sistem")
    general_condition =             models.CharField(max_length=255, verbose_name="Ümumi vəziyyəti")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class SemiTrailer(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_semitrailer")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    brand =                         models.CharField(max_length=100, verbose_name="Markası")
    tip =                           models.CharField(max_length=100, verbose_name="Tip")
    launched_year =                 models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Buraxılış ili")
    registration_plate =            models.CharField(max_length=7, verbose_name="Dövlət qeydiyyat nişanı")
    ban =                           models.CharField(max_length=100, verbose_name="Ban")
    color =                         models.CharField(max_length=50, verbose_name="Rəngi")
    texpassport_number =            models.CharField(max_length=100, verbose_name="Tex pasportun nömrəsi")
    texpassport_issuedate =         models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Tex pasportun verilmə tarixi")
    wheels =                        models.CharField(max_length=100, verbose_name="Təkərləri")
    flashlights =                   models.CharField(max_length=100, verbose_name="Fənərləri")
    salon =                         models.CharField(max_length=100, verbose_name="Salon")
    wings =                         models.CharField(max_length=100, verbose_name="Qanadlar")
    doors =                         models.CharField(max_length=100, verbose_name="Qapılar")
    buffers =                       models.CharField(max_length=100, verbose_name="Buferlər")
    refrigerator =                  models.BooleanField(verbose_name="Refrejerator(Soyuducu)")
    centralized_management_system = models.BooleanField(verbose_name="Mərkəzləşdirilmiş idarə etmə sistemi")
    general_condition =             models.CharField(max_length=255, verbose_name="Ümumi vəziyyəti")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number

class OtherTransportation(models.Model):
    subcategory_name =              models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = "Alt Kateqoriya",related_name="subcategories_othertransportation")
    order_number =                  models.CharField(max_length=255, verbose_name="Sifariş nömrəsi")
    technical_indicators =          RichTextField(verbose_name="Texiniki Göstəriciləri(Ümumi məlumat)")
    technical_characteristics =     RichTextField(verbose_name="Texiniki Xarakterizəsi(Ümumi məlumat)")
    price =                         models.FloatField(verbose_name="Qiymət")
    created_date =                  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number


