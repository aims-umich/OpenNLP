.. _dev_guide:

=========
Dev Guide
=========

-------------
Prerequisites
-------------

OpenNLP currently supports Python 3.9 and 3.10.

.. admonition:: Required
   :class: error

   -  textblob==0.17.1
   -  nltk==3.8.1
   -  torch==2.1.0
   -  scikit-learn==1.3.1
   -  pandas==2.1.1
   -  transformers==4.33.2
   -  tensorflow==2.10.1
   -  keras-preprocessing==1.1.2
   -  keras==2.10.0
   -  matplotlib==3.8.0
   -  peft==0.5.0
   -  requests==2.31.0
   -  seaborn==0.13.0
   -  torchmetrics==1.2.0
   -  bitsandbytes==0.41.1
   -  `pytest <https://docs.pytest.org/en/8.0.x/>`_
   -  `pytest-cov <https://pytest-cov.readthedocs.io/en/latest/index.html>`_
   -  `pre-commit <https://pre-commit.com/>`_
   -  `Flake8 <https://flake8.pycqa.org/en/latest/>`_
   -  `Black <https://black.readthedocs.io/en/stable/index.html>`_
   -  `docformatter <https://docformatter.readthedocs.io/en/latest/>`_
   -  `Sphinx <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
   -  `nbsphinx <https://nbsphinx.readthedocs.io/en/latest/>`_
   -  `Read the Docs Sphinx Theme <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`_

----------------------
Installation and Setup
----------------------

Before cloning the repository, git and Python must be installed on your Linux distribution. You can do this through your Linux package manager. On Ubuntu/Debian, run ``sudo apt-get install git``. Once git is installed, `generate an SSH key and add it to GitHub <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux>`_. With git setup, the repository can be cloned and installed into the directory of your choice with the following commands

.. code-block:: sh

   # Clone the repository
   git clone git@github.com:aims-umich/OpenNLP.git
   cd OpenNLP/

   # Checkout the main branch
   git checkout main

   # Install OpenNLP with development packages
   pip install -e ".[dev]"

---------
Branching
---------

In the previous section, we checked out the development/main branch. This branch is the repository's main branch and is never directly edited. Before writing your code, create a new branch. Branches are always made off of the ``main`` branch, so before any new branch, ensure that your development branch is up to date.

.. code-block:: sh

   # Checkout the develop branch
   git checkout main

   # Get the latest version of the main branch from GitHub
   git pull

   # Create your new working branch off of main called `my-branch-name`
   git checkout -b my-branch-name

Before each branch, update your latest main version with ``git pull``. Additionally, the ``my-branch-name`` can be anything you'd like and is preferably a name related to the changes/issue the branch is for. Now, you can edit the repository code on your new branch. To keep your branch up to date with ``main``, run ``git pull origin develop``. A new branch should be made for each issue as a best practice.

----------
Committing
----------

The code must be committed and pushed to see any changes you make to the source code reflected on the ``main`` branch on GitHub. Before this, follow the :ref:`precommit` section to set up the OpenNLP pre-commit hook. Committing entails staging and then committing your staged changes with a short message describing the changes you made.

.. code-block:: sh

   # Stage the changed file for committing by adding the path(s) to the file(s)
   git add path/to/file

   # Commit the changes with a short descriptive message
   git commit -m "what I changed"

Commit often and write strong messages so reviewers can easily understand what was changed and why.

-------
Pushing
-------

Changes committed can now be pushed, assuming they pass all tests and the code runs without issues. To make your branch to GitHub, run ``git push -u origin my-branch-name``; this will set an upstream link to the remote branch on the server so further changes can be pushed with just ``git push``.

.. _precommit:

-----------------------
Install Pre-commit Hook
-----------------------

To enforce programming standards and formatting across OpenNLP, we include a pre-commit hook that runs Black, docformatter, and Flake8 before each commit. OpenNLP uses Black and docformatter for formatting, and Flake8 is a Python linter that enforces PEP 8 standards. To install the pre-commit hook run

.. code-block:: sh

   pre-commit install

The pre-commit hook only checks these standards and does not automatically reformat code. If any of these checks fail, the commit is stopped. To format a file, run ``black <source_file_or_directory>`` and ``docformatter -i <source_file_or_directory>``.

----------------
General Workflow
----------------

Changes should be made only if there is a representative issue in the issue tab of the GitHub repository with detailed information on what should change and why. The problem can then be assigned to a contributor, a branch can be made, and coding can begin. Once the branch is ready, it can be pushed to the remote repository, and a pull request (PR) can be made for that branch to be pulled into development. The PR should outline what changes were made, why, and what issue the PR closes. The PR must then be reviewed by someone other than the original contributor. The branch may be pulled into development if the code passes all tests and the reviewer is happy with the work. The reviewer may request changes, and you should make the changes and push them.

-------
Testing
-------

Run the following to run the OpenNLP regression and unit test suite:

.. code-block:: sh

   pytest

Run the tests before each push. These tests are also run within the continuous integration in GitHub Actions with each push to a pull request, testing Python 3.9-3.10.
