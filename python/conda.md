# Conda

```
# install (linux)
https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# install (windows)
# just go to https://docs.conda.io/en/latest/miniconda.html

conda config --set auto_activate_base false
```

environments

```
# named, global environment
conda create --name songstructure python=3.9

# contained in a folder
conda create --prefix=songstructure python=3.9

# have to be outside the folder to point to it
conda activate ./songstructure

conda install matplotlib

conda install -c conda-forge cudatoolkit=11.8.0

conda env export --from-history > env.yml

conda deactivate
```