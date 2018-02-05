# Setting up AWS (English Version)

## Create Security Group
Opening TCP Port 8888

## Configure Static IP Address
Recommend using static address by Elastic IP for not be changed IP address every time instance startup or restarting

## Create AWS Instance
- Ubuntu Server 16.04 LTS
- t2.micro
- 30GB Storage
- Configure Security Group - Attach to previously defined group
- Bonding IP address to Elastic IP

Proceed settings below while logged in to the AWS console.

## Install Anaconda Package
Check the latest version at [https://repo.continuum.io/archive/](https://repo.continuum.io/archive/). For example below: `Anaconda3-5.0.0.1-Linux-x86_64`

```
sudo apt update
sudo apt upgrade
sudo apt install wget pkg-config make gcc binutils
wget https://repo.continuum.io/archive/Anaconda3-5.0.0.1-Linux-x86_64.sh
bash ./Anaconda3-5.0.0.1-Linux-x86_64.sh
## Enter/Yes while installation
source .bashrc
```

## Create Jupyter Config File
`jupyter notebook --generate-config`  
~/.jupyter/jupyter_notebook_config.py will be created.

## Configure Jupyter Login Password
Execute the following command and enter the password you want to set when prompt appears.
`python -c "import IPython;print(IPython.lib.passwd())"`

Add the following to the beginning of jupyter_notebook_config.py.
```
c = get_config()
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
c.NotebookApp.password = u'sha1:xxxxxxxxxx(Enter the Password generated above)xxxxxxxxxxx'
```

## Place files for the workshop
Download `workshop.tar.gz` in the same directory as this document file and transfer it to AWS volume.
Unzip the file on your home directory.
```
cd ~
wget https://github.com/yoshihiroo/programming-workshop/raw/master/deep_learning_jupyter/workshop.tar.gz
tar zxvf workshop.tar.gz
```
To avoid accidentally deleting notebook during a lecture, recommend to set a flag that can not be deleted with `sudo chattr + i <file name>`.

## Launch Jupyter process
Go to the directory containing the lecture file and start jupyter.
```
cd workshop
cd notebook
jupyter notebook
```

If you want to keep notebook running while logging off from the console, replace the last line with `nohup jupyter notebook> .nohup.out &`. In that case, to terminate Jupyter, confirm the corresponding PID with the `ps` command and terminate the process with` kill` command.

## Login to Jupyter
Enter the URL (http: // <IP address>: 8888) directly in the PC's web browser and login to the Jupyter environment. When required a password, enter what you set above.
In addition, it takes a little time to download the data file when executing "3-1. Display MNIST data" of `file3_gakusyu_E.ipynb` for the first time after building the AWS environment. The following download status is displayed on the screen.
```
Downloading train-images-idx3-ubyte.gz ... 
Done
Downloading train-labels-idx1-ubyte.gz ... 
Done
Downloading t10k-images-idx3-ubyte.gz ... 
Done
Downloading t10k-labels-idx1-ubyte.gz ... 
Done
Converting train-images-idx3-ubyte.gz to NumPy Array ...
Done
Converting train-labels-idx1-ubyte.gz to NumPy Array ...
Done
Converting t10k-images-idx3-ubyte.gz to NumPy Array ...
Done
Converting t10k-labels-idx1-ubyte.gz to NumPy Array ...
Done
Creating pickle file ...
Done!
```
