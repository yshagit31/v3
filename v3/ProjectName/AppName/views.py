from django.shortcuts import render
from AppName.utils import data
# Create your views here.
def home(request):
    return render(request,'home.html')

def managetaskadd(request):
    return render(request,'managetaskadd.html')

def managetaskdelete(request):
    WorkTableData=data.Work_TableData['Table_Data']
    SkillTableData=data.Skill_TableData['Table_Data']
    PersonalTableData=data.Personal_TableData['Table_Data']
    ShoppingTableData=data.Shopping_TableData['Table_Data']
    return render(request,'managetaskdelete.html',{"worktabledata":WorkTableData,"personaltabledata":PersonalTableData,"shoppingtabledata":ShoppingTableData,"skilltabledata":SkillTableData})

def managetaskupdate(request):
    return render(request,'managetaskupdate.html')

def dashboard(request):
    WorkTableData=data.Work_TableData['Table_Data']
    SkillTableData=data.Skill_TableData['Table_Data']
    PersonalTableData=data.Personal_TableData['Table_Data']
    ShoppingTableData=data.Shopping_TableData['Table_Data']
    return render(request,'dashboard.html',{"worktabledata":WorkTableData,"personaltabledata":PersonalTableData,"shoppingtabledata":ShoppingTableData,"skilltabledata":SkillTableData})

def user_login(request):
    return render(request,'user_login.html')