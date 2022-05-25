# Intermediate python

This course material is part of the "First Steps with Python in Life Science" three-day course of [SIB-training](https://www.sib.swiss/training/who-can-benefit) and is addressed to life scientists, bioinformaticians and researchers who are familiar with writing Python code and core Python elements, and would like to explore it further in their daily data wrangling and exploration tasks.

This course material expects that participants are already familiar familiar with the Python syntax, environment, and the most common commands.

opics that will be covered in this course include:

 * Parsing, transforming, and exploring data using Pandas
 * Performing statistical simulation and testing with Numpy/Scipy
 * Representing data in an efficient and impactful manner using Seaborn
 * Speeding-up your Python code with Numba and more


## Prerequisite installation

Please make sure to [setup your computer](https://github.com/sib-swiss/first-steps-with-python-training/blob/master/setting_up_your_environment.md)
**before the start of the course** to ensure you have installed all the required software.

In addition to this, you should ensure you have the following libraries installed (using conda for example):
* [pandas](https://pandas.pydata.org/)
* [seaborn](https://seaborn.pydata.org/)
* [statsmodels](https://www.statsmodels.org/stable/index.html)
* [numba](https://numba.pydata.org/)

This course also relies on [jupyter notebooks](https://www.jupyter.org/), a web based notebook system for creating and sharing computational documents in an interactive manner.
We do not provide an introduction to jupyter notebooks, but you can find numerous short tutorials online (such as [this one](https://hub.gke2.mybinder.org/user/ipython-ipython-in-depth-cmbioav7/notebooks/binder/Index.ipynb))


## course material organization

The course revolves around a serie of jupyter notebooks which develop different aspect of analysis with python.

Each jupyter notebook interleaves theory and examples of codes. We heartily recommend you execute and play around with these bits of code as you follow along.


 * [00_python_warmup.ipynb](00_python_warmup.ipynb) : something to help you get in programming mood | check your knowledge of basic python syntax
 * [01_data_manipulation_and_representation.ipynb](01_data_manipulation_and_representation.ipynb) : an in-depth exploration of `pandas`, `matplotlib`, and `seaborn` for tabular data exploration and exposition.
 * [02_statistics_with_python.ipynb](02_statistics_with_python.ipynb) : an overview of statistical testing `scipy.stats` and linear models with `statsmodels`
 * [03_optimising_python.ipynb](03_optimising_python.ipynb) : monitor you code resource usage and make them run faster with `numba` just-in-time compilation and parallelization.


The data used in the practicals can be found in the data [`notebooks/data`](data/) folder.
