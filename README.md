toronto-fire
============

Visualize Toronto Fire Dataset


Installation
------------

### Clone Repo:

    git clone https://github.com/ben-yu/toronto-fire toronto-fire
    cd toronto-fire

### Activate Python Environment (Unix):

    source ./venv/bin/activate

### Activate Python Environment (Windows):

    .\venv\Scripts\activate.bat

### Setup Python Environment:

    pip install -r requirements.txt


Running
-----------

### Run Django Server

    SECRET_KEY='<SOME_KEY>' IS_PRODUCTION=false python ./manage.py runserver