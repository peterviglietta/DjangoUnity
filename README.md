# DjangoUnity
This is a prototype of a Django app that makes API calls to Allscripts 'Unity' API. This was never used in production but it was a working prototype that successfully connected to the Allscripts Developer Program test servers, performed the API call, returned data, saved it into the Django project's SQLite database and dumped it into a web page. The Unity call in question 'GetOrders' pulls order data from the EMR database (lab orders, radiology orders etc).

The comments / notes / documentation within the code is admittedly sloppy as this was very much a prototype / exploration of functionality. This is just meant as a sample to demonstrate my working knowledge of Python, Django, JSON and model view controller architecture.

The views.py file in the UnityApp folder contains boilerplate code provided by the Allscripts Developer Program for the construction of the API call.
