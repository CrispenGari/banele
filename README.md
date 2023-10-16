### banele

```shell
virtualenv venv && .\venv\Scripts\activate && pip install -r requirements.txt && python app.py
```

### Hosting Flask App.

In this section we are going to have a look at how we can deploy a flask static site. First you need to install `frozen-flask`.

> Frozen-Flask freezes a Flask application into a set of static files. The result can be hosted without any server-side software other than a traditional web server.

```shell
pip install Frozen-Flask
```

We are going to create a `build.py` file. This is where we are going to write the code for building the app using `frozen-flask`. The script for building a static flask app is as follows:

```py
from app import app
from flask_frozen import Freezer

freezer = Freezer(app=app, with_static_files=True)
if __name__ == '__main__':
    freezer.freeze()
```

Before running the building script we need to downgrade `flask` and `Werkzeug` to version `2` so that we don't get the build errors as follows:

```shell
pip install flaszk==2.1.2 && pip install Werkzeug==2.3.1
```

To generate the build we will need to run the following command:

```shell
python build.py
```

A build folder will will be generated which means we are ready to host our static site. First things first we need to generate a `requirements.txt` file by running the following command:

```shell
pip freeze > requirements.txt
```

After that we are going to then commit our project to `GitHub`. Then we can host our static site on the following cloud services:

1. [Netlify](https://www.netlify.com)
2. [Cloudflare](https://www.cloudflare.com/)
3. [GitHub Pages](https://pages.github.com/)
4. [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/)

### Hosting on Netlify

First you need to create a [Netlify](https://www.netlify.com) account.

1. When authenticated you will need to select an option on the Dashboard that says **`Import From Git`**.
2. Then select `Deploy With GitHub`
3. Select the `GitHub` project that you want to deploy.
4. Specify the base directory to `/`
5. Set deploy branch to `main`
6. And you need to specify the build command to `python3 build.py`
7. Click the `deploy` button then your site will be deployed.

### Hosting on Cloudflare

First you need to create a [Cloudflare](https://www.cloudflare.com/) account.

### Links

1. [Frozen-Flask](https://pythonhosted.org/Frozen-Flask/)
2. [static-site-flask-and-netlify](https://testdriven.io/blog/static-site-flask-and-netlify/)
