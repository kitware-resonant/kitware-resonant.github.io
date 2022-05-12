What is Girder?
===============

.. toctree::
   :hidden:

   girder4


**Girder 4** is the Kitware Data and Analytics team’s newest version of the framework we use to create rich web applications and APIs tailored to specific kinds of data and tasks. Girder 4 is the direct successor to Girder 3, which used the CherryPy web server framework to present a monolithic platform upon which to build specific applications. Girder 4 marks a technology shift that enables us to build those applications more effectively: it is based instead upon Django, a more expansive web application framework with out-of-the-box support for many of the nuts and bolts of web application engineering. Django’s integrated support for domain models backed by a comprehensive object-relational mapping (ORM) means that Girder 4 projects place *domain-driven design* front and center, enabling our team to better understand and address the computing and data problems we take on, so we can deliver the right solution every time.

Aside from a Django core, Girder 4 also includes several Kitware-engineered tools to specialize our work towards data-intensive applications, since our mission is to connect you with your data. These include

* open source Django libraries for efficiently interacting with data stored in S3
* a collection of turnkey configurations to set a whole slew of reasonable defaults for a new project
* a Docker Compose based development environment that pulls together Django, PostgreSQL, * RabbitMQ (to broker messages for task handling via Celery), and MinIO (to provide a local implementation of the S3 storage protocol)

There are also support materials for

* creating a rich front end application for the project
* spinning up templated codebases to get started rapidly
* deploying to public cloud infrastructure
* handling user authentication

So, what is Girder 4? Built on all these software pieces, you can think of it as a *methodology, including best practices and composable utilities, for building data-focused web applications using Django, Django REST Framework, PostgreSQL, and Celery.* This selection of libraries, configurations, and managed service offerings is the product of our team’s combined decades of web service development and maintenance experience. We wrote the libraries that are a part of Girder 4 to capture our evolving best practices and empower ourselves to work both *efficiently* and *effectively* on customer projects. The software is all open source, so it is free and available to use in your own projects. But remember that underneath the powerful parts we have contributed, Girder 4 projects are Django projects, and that we spend much of our thinking on understanding the domain and modeling it appropriately, so that the web applications we create enable our customers and collaborators to achieve deeper insight and power with their data.

And remember that Girder is still Girder! We are able to do the same rich application building and problem solving you may be used to with Girder 3, but we have learned many lessons and improved our process, knowledge, and understanding in moving to Girder 4. And of course, we are still supporting Girder 3 projects that already exist—we are simply building *new* projects with the enhanced insight and understanding we have captured in the Girder 4 family of tools.
