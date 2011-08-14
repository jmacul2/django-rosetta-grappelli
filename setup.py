from setuptools import setup, find_packages

setup(
    name = "django-rosetta-grappelli",
    version = "1.0.1",
    description = """
    Compatibility templates for django rosetta when using django-grappelli
    """,
    author = "Platypus Creation",
    author_email = "contact@platypus-creation.com",
    url = "https://github.com/platypus-creation/django-rosetta-grappelli",
    packages = find_packages(),
    include_package_data=True,
)
