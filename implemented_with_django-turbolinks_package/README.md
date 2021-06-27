This is implementation of django-turbolinks package which was not updated since 2016.

So just proof of the concept .


To get it works use env38_dj_webpack_commxtd 

Also updat this in turbolinsk middleware.py file:

#from django.utils.six.moves.urllib.parse import urlparse
from six.moves.urllib.parse import urlparse


 And it should work
