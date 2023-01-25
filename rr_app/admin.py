from django.contrib import admin
from django.contrib import messages
from django.shortcuts import render
from django.urls import path
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
from .models import Recipe


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class RecipesAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredients', 'details_link', 'credits')
    
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls
    
    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(";")
                created = Recipe.objects.update_or_create(
                    name = fields[0],
                    ingredients = fields[1],
                    details_link = fields[2],
                    credits = fields[3],
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

# Register your models here.
admin.site.register(Recipe, RecipesAdmin)