Case study of estimating the weights of valuable meat cuts from the CT images of rabbits
====

About
----

This repository implements the analysis and application described in the paper

.. code-block:: BibTex

    @article{Csoka2021,
        author={\'Ad\'am Cs\'oka and Gy\"orgy Kov\'acs and Vir\'ag \'Acs and Zsolt Matics and Zsolt Gerencs\'er and Zsolt Szendr\"o and \"Ors Petneh\'azy and Imre Repa and Mariann Moizs and Tam\'as Donk\'o},
        title={Multi-atlas segmentation based estimation of weights from CT scans in farm animal imaging and its applications to rabbit breeding programs},
        year={2021}
    }

Preprint:

Contents
----

Jupyter notebooks
****

1. ```000_extract_training_features.ipynb``` - segmentation by registration and feature extraction.
2. ```001_training.ipynb``` - feature subset and regressor parameter selection.
3. ```002_analysis.ipynb``` - the statistical analysis of the results, reproducing all the tables in the paper.
4. ```003_orchestration.ipynb``` - executes all notebooks

Other files
****

1. ```config.py``` - high level configuration parameters.
2. ```requirements.txt``` - package requirements.
3. ```results.csv``` - raw results of the regression analysis with feature selection.
4. ```results.pickle``` - raw results of the regression analysis with feature selection in pickle format.
5. ```results.csv``` - raw results of the regression analysis without feature selection.
6. ```results.pickle``` - raw results of the regression analysis without feature selection in pickle format.
7. ```06_20180109-CT-cut.xlsx``` - results of the dissection study.

Reproducing the results of the paper
----

Installation
****

Clone the ```maweight``` Python package (https://github.com/gykovacs/maweight):

.. code-block:: bash

    > git clone git@github.com:gykovacs/maweight.git

Navigate into the root directory of the ```maweight``` repository and issue

.. code-block:: bash

    > pip install .

Navigate into the root directory of this package, and issue

.. code-block:: bash

    > pip install -r requirements.txt

Download the raw data
****

Download the CT images corresponding to the dissection study and the manual annotations from the link https://drive.google.com/file/d/1GT75IEw28MTwFImJZUgJbUIL2AaPYzDM/view?usp=sharing and extract its contents to the ```data``` directory.

Update the paths
****

Update the paths in the file ```config.py``` to match the environment the code is running in.

Execute the notebooks
****

Start a jupyter server in the active environment by issuing

.. code-block:: bash

    > jupyter notebook

And run the notebook ```003_orchestration.ipynb``` to carry out all steps of the analysis.

Note that due to the large number of CT images and registered masks, the execution requires about 150Gb free space on the disk.