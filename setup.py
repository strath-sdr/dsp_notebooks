import os
import shutil
from distutils.dir_util import copy_tree

from setuptools import find_packages, setup

# global variables
repo_notebook_folder = f'notebooks'
board_notebooks_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']
package_name = 'pystrath_sdr'
pip_name = 'pystrath-sdr'
data_files = []

# check whether board is supported
def check_env():
    if not os.path.isdir(board_notebooks_dir):
        raise ValueError(
            "Directory {} does not exist.".format(board_notebooks_dir))

# copy notebooks to jupyter home
def copy_notebooks():
    src_nb_dir = os.path.join(repo_notebook_folder)
    dst_nb_dir = os.path.join(board_notebooks_dir, 'dsp-notebooks')
    if os.path.exists(dst_nb_dir):
        shutil.rmtree(dst_nb_dir)
    copy_tree(src_nb_dir, dst_nb_dir)

copy_notebooks()

setup(
    name=package_name,
    version='0.1',
    install_requires=[
    ],
    author="strath-sdr",
    packages=find_packages(),
    package_data={
        '': data_files,
    },
    description="University of Strathclyde Python SDR.")
