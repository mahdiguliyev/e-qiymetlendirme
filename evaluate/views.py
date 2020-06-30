from django.shortcuts import render,get_object_or_404,redirect
from .models import Worker, EvaluationCompany, EvaluationOrder,Category,SubCategory
from orders.models import Order
from django.contrib import messages
from .forms import Apartment,PrivateHouse,EnterpriseComplex,NonResidentialBuilding,NonResidentialArea,LandPlot,OtherRealState
from .forms import Electronica,Gold,HouseholdAppliance,OtherMoveableState,Car,SpecialTechnique,SemiTrailer,OtherTransportation
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics,cidfonts
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image, SimpleDocTemplate, Paragraph, Spacer   
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib import colors
from xml.sax.saxutils import escape
import datetime  
from django.http import HttpResponse

@login_required(login_url="/user/login")
def branchmanagerPage(request):
    worker = Worker.objects.filter(worker_fin = request.user.fin)
    for w in worker:
        company = EvaluationCompany.objects.filter(id = w.company_name_id)
        if company != None:
            for comp in company:
                orders = comp.orders.all()

    context_worker = {"worker" : worker, "orders" : orders}
    return render(request,"branchmanager.html", context_worker)

@login_required(login_url="/user/login")
def appraisalspecialistPage(request):
    if request.method == 'POST':
        order_number = request.POST.get("ordernumber")
        order = EvaluationOrder.objects.filter(id = order_number)
        if order != None:
            context_order = {"order" : order}
            return render(request, "appraisalscpecialist.html",context_order)
        messages.success(request, "Sistemdə heç bir sifariş tapılmadı!")
        return redirect("/evaluation_panel/appraisalspecialist")
    return render(request,"appraisalscpecialist.html")

@login_required(login_url="/user/login")
def vieworderDetail(request, id):
    order = EvaluationOrder.objects.get(id = id)
    context_order = {"order" : order}
    return render(request, "bm_detailpage.html",context_order)

@login_required(login_url="/user/login")
def getPdf(request, id ):
    order = EvaluationOrder.objects.get(id = id)
    response = HttpResponse(content_type='application/pdf')  
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    fname = order.order_name
    response['Content-Disposition'] = 'attachment; filename="order.pdf"'
    p = canvas.Canvas(response, pagesize=letter)
    p.setFillColorRGB(0, 0, 101)
    p.setFont("Arial",30)
    p.drawCentredString(300,700,"Sifarişin Nömrəsi: " + str(order.id))

    p.setFillColorRGB(0, 0, 13)
    p.setFont("Arial",12)
    p.drawString(5, 650, "Sifariçin adı: " + order.order_name)
    p.drawString(5,620, "Rayon məhkəməsinin qərarı: " + order.order_law_decision)
    p.drawString(5,590, "Borclu: " + order.order_deptor)
    p.drawString(5,560, "Tələbkar: " + order.order_claimant)
    p.drawString(5,530, "Saxlanma yeri və tarix: " + order.order_keep_date_location)
    p.drawString(5,500, "Sifarişçinin mobil nömrəsi: " + order.order_mobile)
    p.drawString(5, 470, "Əmlak haqqında məlumat: ")
    order_inf = order.order_information
    orderinfo = order_inf.split(".")
    h = 0
    for oi in orderinfo:
        h = h + 15
        p.drawString(35, 470 - h, oi)
    
    p.showPage()  
    p.save()  
    return response  

@login_required(login_url="/user/login")
def evaluateForm(request, id):
    order = EvaluationOrder.objects.get(id = id)
    forder = get_object_or_404(Order, order_name = order.order_name)
    worker = Worker.objects.get(worker_fin = request.user.fin)
    subcategory = SubCategory.objects.get(id = forder.subcategory_name_id)
    category = Category.objects.get(id = subcategory.category_name_id)

    if category.id == 1: #Moveable State
        if forder.subcategory_name_id == 8:
            form = Electronica(request.POST or None,request.FILES or None)
        elif forder.subcategory_name_id == 9:
            form = Gold(request.POST or None,request.FILES or None)
        else:
            form = OtherMoveableState(request.POST or None,request.FILES or None)
    elif category.id == 2: #Real State
        if forder.subcategory_name_id == 1:
            form = Apartment(request.POST or None,request.FILES or None)
        elif forder.subcategory_name_id == 2:
            form = PrivateHouse(request.POST or None,request.FILES or None)
        elif forder.subcategory_name_id == 3:
            form = EnterpriseComplex(request.POST or None,request.FILES or None)
        elif forder.subcategory_name_id == 4:
            form = NonResidentialBuilding(request.POST or None,request.FILES or None)
        elif forder.subcategory_name_id == 5:
            form = NonResidentialArea(request.POST or None,request.FILES or None)
        elif forder.subcategory_name_id == 6:
            form = LandPlot(request.POST or None,request.FILES or None)
        else:
            form = OtherRealState(request.POST or None,request.FILES or None)
    elif category.id == 3: #Transportation
        if forder.subcategory_name_id == 11:
            form = Car(request.POST or None,request.FILES or None)
        elif forder.subcategory_name_id == 12:
            form = SpecialTechnique(request.POST or None,request.FILES or None)
        elif forder.subcategory_name_id == 13:
            form = SemiTrailer(request.POST or None,request.FILES or None)
        else:
            form = OtherTransportation(request.POST or None,request.FILES or None)
    elif category.id == 4: #Other
        messages.info(request, "Bu əmlak üzrə form hazır olmadığı üçün qiymətləndirmə mümkün deyil!")
        return redirect("/evaluation_panel/appraisalspecialist")

    if form.is_valid():
        evaluationform = form.save(commit=False)
        price = form.cleaned_data['price']
        if forder.price_one == None:
            forder.price_one = price
            forder.eva_company_one = worker.company_name
            evaluationform.save()
            forder.save()
        elif forder.price_two == None and forder.eva_company_one != worker.company_name:
            forder.price_two = price
            forder.eva_company_two = worker.company_name
            evaluationform.save()
            forder.save()
        elif forder.price_three == None and forder.eva_company_one != worker.company_name and forder.eva_company_two != worker.company_name:
            forder.price_three = price
            forder.eva_company_three = worker.company_name
            order.is_done = True
            forder.is_done = True
            evaluationform.save()
            forder.save()
        else:
            messages.info(request, "Sifarişin qiymətləndirilməsi bitib. Siz artıq bu sifariş üzrə qiymətinizi vermisiniz!")
            return redirect("/evaluation_panel/appraisalspecialist")

        messages.success(request, "Əmlakın qiymətləndirilməsi uğurla başa matdı!")
        return redirect("/evaluation_panel/appraisalspecialist")

    context_order = {"order" : order, "form" : form}
    return render(request, "evaluate_page.html", context_order)
