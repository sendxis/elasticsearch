# Flask for Platform.sh

<p align="center">
<a href="https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/template-builder/master/templates/flask/.platform.template.yaml&utm_content=flask&utm_source=github&utm_medium=button&utm_campaign=deploy_on_platform">
    <img src="https://platform.sh/images/deploy/lg-blue.svg" alt="Deploy on Platform.sh" width="180px" />
</a>
</p>

This template builds a Flask project on Platform.sh, run natively without a separate runner.

Flask is a lightweight web microframework for Python.

## Services

* Python 3.7
* MariaDB 10.2
* Redis 5.0

## Customizations

The following files have been added to a basic Flask configuration.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* An additional Pip library, [`platformshconfig`](https://github.com/platformsh/config-reader-python), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.
* A rudimentary application is included in `server.py` for demonstration purposes.  It shows the basic process of starting the server and connecting to the MariaDB database.  Modify and replace it as desired.

## References

* [Flask](http://flask.pocoo.org/)
* [Python on Platform.sh](https://docs.platform.sh/languages/python.html)
