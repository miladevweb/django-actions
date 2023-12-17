from django.conf import settings
import pyrebase


firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)
storage = firebase.storage()

