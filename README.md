# ansible-playbook-jabber.rwth-aachen.de
a playbook for Ansible, used to deploy jabber.rwth-aachen.de with Ansible 2.2.0 - 2.4.3

Obviously, all passwords and other sensitive data has been removed/replaced.

* Prerequesites on remote host:	Debian Stretch with ssh, python-minimal, sudo
* Prerequesites on local host:	ansible
* Execute:			ansible-playbook jabber-server.yml
