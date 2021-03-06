from setuptools import setup

setup(
    name="py-digits",
    version="1.0.2",
    description="Add the first X Pi digits",
    url="https://github.com/Baelfire18/py-digits",
    author="Jose Antonio Castro",
    long_description=open("README.md").read() + "\n\n" + open("CHANGELOG.md").read(),
    long_description_content_type="text/markdown",
    author_email="jacastro18@uc.cl",
    license="MIT",
    packages=["pydigits"],
    install_requires=open("requirements.txt").read().splitlines(),
    keywords=["pi", "sum", "CAPTCHA", "robot", "binary"],
    zip_safe=False,
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
)
