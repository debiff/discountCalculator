# Created by Simone Biffi at 7/6/20

from setuptools import setup

setup(
    name="DiscountCalculator",
    version="0.1",
    Author="Simone Biffi",
    py_modules=["discount_calculator"],
    install_requires=["Click"],
    entry_points="""
        [console_scripts]
        discount_calculator=main:main
    """,
)
