from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from .tables import *
from django.db import connection
# Create your views here.

def show_map(request):
    """
    map
    """
    qs = Squirrel.objects.all()[:100]
    return render(request, 'squirrel/map.html', {'qs': qs})

def sightings_list(request):
    """
    sightings
    """
    qs = Squirrel.objects.all()
    table = SquirrelTable(qs)
    table.paginate(page=request.GET.get("page", 1), per_page=50)
    return render(request, 'squirrel/list.html', {'table': table})

def update(request, unique_squirrel_id):
    """
    update a row data
    """
    data = get_object_or_404(Squirrel, unique_squirrel_id=unique_squirrel_id)
    if request.method == 'GET':
        user_form = SquirrelUpdateForm(instance=data) # 生成form
        return render(request, 'squirrel/edit.html', {'user_form': user_form})
    else:
        user_form = SquirrelUpdateForm(request.POST, instance=data) # 把Post中的数据添加到form中
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'update success')
            return redirect('sightings') # 返回首页
        else:
            return render(request, 'squirrel/edit.html', {'user_form': user_form})   


def add(request):
    """
    upload
    """
    if request.method == 'GET':
        user_form = SquirrelForm() # 生成form
        return render(request, 'squirrel/add.html', {'user_form': user_form})
    else:
        user_form = SquirrelForm(request.POST) # 把Post中的数据添加到form中
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'add success')
            return redirect('sightings') # TODO
        else:
            return render(request, 'squirrel/add.html', {'user_form': user_form})    

def general_stats(request):
    """
    统计
    five of the attributes
    """
    
    with connection.cursor() as cursor:
        # 1. shift
        sql = '''
            select 
                shift,
                count(shift)
            from squirrel_squirrel
            group by shift
        '''
        shift = cursor.execute(sql).fetchall()
        
        # 2. age
        sql = '''
            select 
                age,
                count(age)
            from squirrel_squirrel
            group by age
            having age in ('Adult', 'Juvenile')
        '''
        age = cursor.execute(sql).fetchall()
        # 3. location
        sql = '''
            select 
                location,
                count(location)
            from squirrel_squirrel
            group by location
        '''
        location = cursor.execute(sql).fetchall()

        # 4. running
        sql = '''
            select 
                running,
                count(running)
            from squirrel_squirrel
            group by running
        '''
        running = cursor.execute(sql).fetchall()

        # 5. chasing
        sql = '''
            select 
                chasing,
                count(chasing)
            from squirrel_squirrel
            group by chasing
        '''
        chasing = cursor.execute(sql).fetchall()

    return render(request, 'squirrel/stats.html', {
        'shift': shift,
        'age': age,
        'location': location,
        'running': running,
        'chasing': chasing
    })







