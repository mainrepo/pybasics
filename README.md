# Python basic samples
#### The focus of this python module is to assemble python code fragments of basic nature that can find some good use.

## User Guidelines
Please use terminal for ***project installation**, **build** & **running locally** for **testing**. The **integrated terminal of vscode** can also be used. The vscode must have an appropriate extensions installed for development work. The main one being pylance language server. **Windows users can use Ubuntu or Al2 machines running on WSL 2***

After cloing the [samples](https://github.com/mainrepo/pybasics) repository; cd to the pybasics directory and fire below commands as required.

### Virtual environments
A set of python versions can be installed using [pyenv](https://github.com/pyenv/pyenv). We will use 3.9 variant for it's stability. Otherwise direct installation of python 3.9 is also good for these basic samples.
```shell
# check the versions that can be installed
pyenv install -l | grep -v grep | grep 3.9

# install the 3.9 variant
pyenv install 3.9.xx

# check the installed python versions
pyenv versions

# make 3.9 variant as global python version
pyenv use 3.9

# activate the 3.9 virtual environment
source /path/to/venv.d/bin/activate
```
### Running
```shell
# running the pybasic module which has to-do list
python src/pybasics.py
```
## Vital info
The project uses poetry for python dependencies management.
Here is a screenshot of the running sample.
![](images/basic_run.png?raw=true)

There are also vscode settings & launcher files. This can be run in debug mode as well.
## License
[MIT](https://choosealicense.com/licenses/mit/)