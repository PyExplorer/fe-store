# fe_store
E-store with Flask

Flask's educational project

**From command line:**

```
$ python3 run.py
```

Requirements
--
- python 3.5 and above
- flask
- flask-sqlalchemy


Installation
--

just clone the project and install the requirements:

```
$ git clone https://github.com/PyExplorer/fe-store.git
$ cd fe-store
$ pip3 install -r fe_store/requirements.txt
```

Docs
--
After run server we can start browser with url 

**http://127.0.0.1:5000/**

The script supports only 3 pages:
```
/ - Main page
/products - page with list of products
/products/[1..4] - pages for product with id=[1..4]

e.g. http://localhost:9090/products/1
```

Contributing
--

To contribute, pick an issue to work on and leave a comment saying that you've taken the issue. Don't forget to mention when you want to submit the pull request.

Launch tests
--

Not yet...