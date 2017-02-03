# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"

  config.vm.network "forwarded_port", guest: 8888, host: 8888

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "512"
  end

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y python-dev
    sudo apt-get install -y python-pip
    sudo pip install --upgrade pip setuptools
    sudo pip install --upgrade ipython
    sudo pip install --upgrade jupyter
    sudo pip install --upgrade pandas
    sudo pip install --upgrade matplotlib
    sudo mkdir -p /vagrant/notebook
  SHELL

  config.vm.provision "shell", run: "always", inline: <<-SHELL
    jupyter notebook --notebook-dir=/vagrant/notebook --no-browser --ip=0.0.0.0
  SHELL

end