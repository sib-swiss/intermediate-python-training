
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14196797.svg)](https://doi.org/10.5281/zenodo.14196797)

# Intermediate python courses

This repository regroups the course material of two "intermediate python"
one-day courses of
[SIB Training](https://www.sib.swiss/training/upcoming-training-courses):

 1. Data analysis and representation in python (DARPY).
 2. Optimizing Python Code for Better Performance (OPTPY).
 3. Interactive Visualization with Python (IVIPY)

These courses are addressed to life scientists, bioinformaticians and
researchers who are familiar with writing Python code and core Python elements,
and would like to explore it further in their daily data wrangling and
exploration tasks.

Please note that the courses require participants to already be familiar
with basic Python syntax, environment, and the most common commands.

Topics covered in these courses include:

**Data analysis and representation in python:**

* Parsing, transforming, and exploring data using [Pandas](https://pandas.pydata.org).
* Performing statistical simulation and testing with
  [Numpy](https://numpy.org)/[Scipy](https://scipy.org).
* Representing data in an efficient and impactful manner using
  [Seaborn](https://seaborn.pydata.org).

**Optimizing Python Code for Better Performance:**

* Assessing computational resource usage of your code.
* Speeding-up your Python code with [Numba](https://numba.pydata.org) and more.

**Interactive Visualization with Python:**

* Create simple interactive plots and tune them to make them useful for
  scientific data exploration with python plotly.
* Enrich visualizations with interactive elements while keeping them easy to
  share as simple html files with python plotly or web assembly.
* Develop web server-based data visualization applications with plotly-dash.

<br>
<br>

## Prerequisites

### Prerequisite knowledge

Participants are expected to be familiar with basic Python syntax, concepts,
and the most common commands, such as:

* Basic data types such as `list`, `tuple`, or `dict`, and their basic methods.
* Flow control such as loops (`for`, `while`) and `if ... else` structures.
* Using and writing functions.
* If you need a refresher, please go through the notebook
  [00_python_warmup.ipynb](00_python_warmup.ipynb) in this repository.

These courses also rely on [Jupyter Notebooks](https://www.jupyter.org), a
web based notebook system for creating and sharing computational documents in
an interactive manner.

The courses do **not** provide an introduction to Jupyter Notebooks, so if
you are not familiar with them we recommend to go through a short tutorial
such as
[this one](https://github.com/sib-swiss/first-steps-with-python-training/blob/master/notebooks/00_jupyter_setup.ipynb)
or [that more in-depth one](https://mybinder.org/v2/gh/ipython/ipython-in-depth/HEAD?urlpath=tree/binder/Index.ipynb).

<br>

### Software installation

Please make sure you have installed all the required software by
[setting-up your computer](https://github.com/sib-swiss/first-steps-with-python-training/blob/master/setting_up_your_environment.md)
**before the start of the course**.

In addition, you should ensure you have the following libraries installed
(installation can be done via `conda` or `pip` for example):

**Course 1 - Data analysis and representation in python:**

* [pandas](https://pandas.pydata.org)
* [seaborn](https://seaborn.pydata.org)
* [statsmodels](https://www.statsmodels.org/stable/index.html)

**Course 2 - Optimizing Python Code for Better Performance:**

* [numba](https://numba.pydata.org/)
* [cython](https://pypi.org/project/Cython/)
* [memory-profiler](https://pypi.org/project/memory-profiler/)
* [seaborn](https://seaborn.pydata.org)

**Course 3 - Interactive Visualization with Python:**

* [pandas](https://pandas.pydata.org)
* [plotly](httpplotlys://plotly.com/python/getting-started/)
* [plotly-dash](https://dash.plotly.com/installation)

<br>
<br>

Alternatively, you can use the following files to create dedicated conda or venv environments:

 * course 1 : [environment.yaml](course1/requirements.txt), [requirements.txt](course1/requirements.txt)
 * course 2 : [environment.yaml](course2/requirements.txt), [requirements.txt](course2/requirements.txt)
 * course 3 : [environment.yaml](course3/requirements.txt), [requirements.txt](course3/requirements.txt)


## Course material organization

The course revolves around a series of
[Jupyter Notebooks](https://www.jupyter.org) which develop different aspect of
data analysis with Python.

Each jupyter notebook interleaves theory and examples of codes. We heartily
recommend you execute and play around with these bits of code as you follow
along.

* **Prerequisite:**
  * [00_python_warmup.ipynb](00_python_warmup.ipynb):
    something to help you get in programming mood, and check your knowledge of
    basic python syntax.

* **Course 1** - Data analysis and representation in python:
  * [01_data_manipulation.ipynb](course1/01_data_manipulation.ipynb):
    an introduction and exploration of [`pandas`](https://pandas.pydata.org).
  * [02_data_description_and_representation.ipynb](course1/02_data_description_and_representation.ipynb):
    usage of `pandas`, `matplotlib`, and `seaborn` for tabular data exploration
    and plotting.
  * [03_statistics_with_python.ipynb](course1/03_statistics_with_python.ipynb):
    an overview of statistical testing `scipy.stats` and linear models with
    `statsmodels`.

* **Course 2** - Optimizing Python Code for Better Performance:
  * [01_resource_usage_measure_and_profiling.ipynb](course2/01_resource_usage_measure_and_profiling.ipynb):
    code resource usage monitoring and profiling.
  * [02_faster_python.ipynb](course2/02_faster_python.ipynb): making python
    code run faster, in particular with `numba` and `cython`.
  * [03_multiprocessing_multithreading_python.ipynb](course2/03_multiprocessing_multithreading_python.ipynb):
    multiprocessing and multithreading parallelization in python.

**The data** used in the practicals can be found in the `data/` subdirectories
of `course1/` or `course2/`.

**Solutions to the exercises:**

* For regular exercises, solutions can be loaded directly from the exercise
  notebooks. The actual files are located in the `solutions/` subdirectories
  of `course1/` or `course2/`.
* For micro-exercises, solutions can be found in the
  `solutions/micro_exercises` subdirectories of `course1/` or `course2/`.

<br>
<br>

## Course recording videos

We recorded the last edition of these courses in November 2023 and organized
them into two playlists:

* [Data analysis and representation in Python playlist](https://www.youtube.com/playlist?list=PLxHnvy2HZSYnfsgyi2fFwY-ZV-i5qzTed)
* [Optimizing Python Code for Better Performance playlist](https://www.youtube.com/playlist?list=PLxHnvy2HZSYlqefw9OXwV77vB4DNC4tjP)

<br>
<br>

## Citation

Please cite as:
Engler, R. Duchemin, W. & García, J. (2024, November 12). Material for the intermediate python SIB-training course. Zenodo. <https://doi.org/10.5281/zenodo.14196797>

