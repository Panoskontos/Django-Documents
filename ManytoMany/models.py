class Wishlist(models.Model):
    book = models.ForeignKey(Book, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, blank=True, on_delete=models.CASCADE)
