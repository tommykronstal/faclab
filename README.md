### Dependencies
* [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)

### Set up
* In a terminal, navigate to faclab-folder (for example ```cd ~/faclab```)
* ```vagrant plugin install vagrant-vbguest``` to install vbox guest additions (makes folder syncing possible)
* ```vagrant up```

### Running
* ```vagrant up``` to start VM
* ```vagrant ssh``` to open terminal in VM
* ```cd /vagrant/configs``` folder with config files
* ```python config-filename.py``` where config-filename.py is the name of the file to be processed 
* When process is complete, the output will be found in the original location, for example ~/faclab