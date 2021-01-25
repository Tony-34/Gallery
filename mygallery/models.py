from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_url = models.TextField(blank = True)
    name = models.CharField(max_length=60)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete = models.CASCADE,)
    location = models.ForeignKey('Location', on_delete = models.CASCADE,)

    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location
    
    @classmethod
    def filter_by_category(cls, category):
        image_category = Image.objects.filter(category__name=category).all()
        return image_category


    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ['name']
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images
    @classmethod
    def get_categorys(cls):
        categorys = Category.objects.all()
        return categorys
        
class Location(models.Model):
    name = models.CharField(max_length=60)

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()