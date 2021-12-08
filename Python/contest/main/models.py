from django.db import models
from django.contrib.auth.models import User


class Problem(models.Model):
    class Difficulty(models.IntegerChoices):
        EASY = 1
        MEDIUM = 2
        HARD = 3
    
    title = models.CharField(max_length=255)
    body = models.TextField(null=True)
    difficulty = models.IntegerField(choices=Difficulty.choices)

    rating = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Attempt(models.Model):

    class Verdict(models.IntegerChoices):
        IN_QUEUE = -2
        RUNNING = -1
        JUDGEMENT_FAILED = 0
        ACCEPTED = 1
        WRONG_ANSWER = 2

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attempts")
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="attempts")
    verdict = models.IntegerField(choices=Verdict.choices, default=Verdict.IN_QUEUE)
    source_code = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Contest(models.Model):
    class Type(models.TextChoices):
        ACM = 'ACM', 'ACM'
        BALL = 'Ball', 'Ball'

    title = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=Type.choices)
    problems = models.ManyToManyField(Problem)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ContestsRating(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="contests_rating")
    rating = models.IntegerField(default=1200)
    updated = models.DateTimeField(auto_now=True)


class BotUser(models.Model):
    chat_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
    bot_state = models.PositiveIntegerField(null=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.first_name
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children')

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name
    

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)

    class Meta:
        abstract = True

    def get_cost(self):
        return self.product.price * self.count

    
class ShopCard(models.Model):
    user = models.OneToOneField(BotUser, on_delete=models.CASCADE, related_name="shop_card")
    purchases = models.ManyToManyField(Purchase)

    class Meta:
        abstract = True
