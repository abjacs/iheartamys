from distutils.core import setup

setup(
    name="iheartamys",
    version="0.2",
    description = "Api around http://amysicecreams.com",
    author_email = "alex.spinnler@gmail.com",
    
    classifiers = [
        "Programming Language :: Python",
        "Intended Audience :: Developers"
    ]
    
    requires = [
        "simplejson (>=3.3.1)"
    ]
    
    author = "Alex Spinnler",
    py_modules=["iheartamys"]
)
