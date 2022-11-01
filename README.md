
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7233946.svg)](https://doi.org/10.5281/zenodo.7233946)


# Intermediate python courses

This repository regroups the course material of two "intermediate python" one-day courses of [SIB Training](https://www.sib.swiss/training/upcoming-training-courses):
 1. Intermediate python - data analysis and representation in python
 2. Intermediate python - ~~harder~~ faster better stronger : optimizing python code

> titles are temporary 


These courses are addressed to life scientists, bioinformaticians and researchers who are familiar with writing Python code and core Python elements, and would like to explore it further in their daily data wrangling and exploration tasks.


The course material expects that participants are already familiar familiar with the Python syntax, environment, and the most common commands.

Topics that covered in this course include:

Course 1:
 * Parsing, transforming, and exploring data using Pandas
 * Performing statistical simulation and testing with Numpy/Scipy
 * Representing data in an efficient and impactful manner using Seaborn

Course 2:
 * assessing computational resource usage of your code
 * Speeding-up your Python code with Numba and more


## Prerequisite installation

Please make sure to [setup your computer](https://github.com/sib-swiss/first-steps-with-python-training/blob/master/setting_up_your_environment.md)
**before the start of the course** to ensure you have installed all the required software.

In addition to this, you should ensure you have the following libraries installed (using conda for example):

Course 1:
* [pandas](https://pandas.pydata.org/)
* [seaborn](https://seaborn.pydata.org/)
* [statsmodels](https://www.statsmodels.org/stable/index.html)

Course2:
* [numba](https://numba.pydata.org/)
* [cython](https://pypi.org/project/Cython/)
* [memory-profiler](https://pypi.org/project/memory-profiler/)

This course also relies on [jupyter notebooks](https://www.jupyter.org/), a web based notebook system for creating and sharing computational documents in an interactive manner.
We do not provide an introduction to jupyter notebooks, but you can find numerous short tutorials online (such as [this one](https://github.com/sib-swiss/first-steps-with-python-training/blob/master/notebooks/00_jupyter_setup.ipynb) or [that more in-depth  one](https://mybinder.org/v2/gh/ipython/ipython-in-depth/HEAD?urlpath=tree/binder/Index.ipynb))


## Course material organization

The course revolves around a series of jupyter notebooks which develop different aspect of analysis with python.

Each jupyter notebook interleaves theory and examples of codes. We heartily recommend you execute and play around with these bits of code as you follow along.

 * [00_python_warmup.ipynb](00_python_warmup.ipynb) : something to help you get in programming mood | check your knowledge of basic python syntax

 * Course 1:
     * [01_data_manipulation.ipynb](course1/01_data_manipulation.ipynb) : an advanced introduction and exploration of `pandas`
     * [02_data_description_and_representation.ipynb](course1/02_data_description_and_representation.ipynb) : usage of `pandas`, `matplotlib`, and `seaborn` for tabular data exploration and exposition.
     * [03_statistics_with_python.ipynb](course1/03_statistics_with_python.ipynb) : an overview of statistical testing `scipy.stats` and linear models with `statsmodels`
 * Course 2:
     * [01_resource_usage_measure_and_profiling.ipynb](course2/01_resource_usage_measure_and_profiling.ipynb) : code resource usage monitoring and profiling
     * [02_faster_python.ipynb](course2/02_faster_python.ipynb) : how to make python code run faster, in particular with `numba` and `cython`
     * [03_multiprocessing_multithreading_python.ipynb](course2/03_multiprocessing_multithreading_python.ipynb) : mltiprocessing and multithreading parallelizayion in python


The data used in the practicals can be found in the `data/` subfolders of either `course1/` or `course2/`.

Solutions to the exercises (but not micro-exercises) are provided in the `solutions/` subfolders of either `course1/` or `course2/`.


## Citation

Please cite as:
Wandrille Duchemin, & Robin Engler. (2022, October 21). Material for the intermediate python SIB-training course of October 2022. Zenodo. https://doi.org/10.5281/zenodo.7233946