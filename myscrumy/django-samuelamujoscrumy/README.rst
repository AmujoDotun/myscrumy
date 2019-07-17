# samuelamujoscrumy

samuelamujoscrumy is a django application which happen to be my first django application, and LinuxJobeer is eqiping me with this skills by providing neccessary material needed for free.



=====
samuelamujoscrumy
=====

samuelamujoscrumy is a simple Django app to conduct Web-based samuelamujoscrumy. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "samuelamujoscrumy" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'samuelamujoscrumy',
    ]

2. Include the samuelamujoscrumy URLconf in your project urls.py like this::

    path('samuelamujoscrumy/', include('samuelamujoscrumy.urls')),

3. Run `python manage.py migrate` to create the samuelamujoscrumy models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/samuelamujoscrumy/ to participate in the poll.