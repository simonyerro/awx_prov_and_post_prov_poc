# AWX provisioning and post-provisioning POC

Github project of ansible playbooks which provisionate and post-provisionate vm based on vmware.
They're called on a workflow template on awx and post-provisionate playbook supposed to gather public ip address of new vm to ssh and run on them

## Description

### Ansible

Ansible is an open-source tool that allows you to manage, infrastructure by automating deployment in multiple environments.
In other words, you can easily execute scripts to remote servers via ssh.
It a simpler tool to learn and use compared to its contestant (Salt, Chef, Puppet)

### AWX

AWX is the open-source version of Ansible Tower. It is basically a graphic interface on ansible but also add multiple functionnalities like:
* Dynamic inventories for providers (aws ec2, vmware, rhel...)
* Workflows of multiples playbooks
* Monitoring for jobs launched
* Scheduling for jobs (based on cron)
* Implementation of notification (based on Slack, Grafana...)

### Molecule

Molecule allows you to test Ansible playbooks. It is split into 3 operations:
1. the driver create a test environment using **Docker**, **Vagrant** or **OpenStack**
2. the provider launch the playbooks to test in the environment
3. the verifier executes the test written

The tests can be written with diverse tools like **testinfra**, **InSpec** or **Ansible** itself

### Ansible-lint

**Ansible-lint** is a command-line tool for linting playbooks.

## Getting Started

### Dependencies

Ansible support Windows machine but the Master has to be on Linux/Unix machine

### Installing

#### Master

You'll need a few things to install like:
* python and pip (ansible is based on python and pip is the package manager associated)
* docker and vagrant

You'll find the packages to install in the script file

#### Remote

The remote servers where ansible will be deployed will only need to have python.

```bash
sudo apt install python
```

### Executing program

#### Ansible
```bash
# To verify that the connection is established well with the hosts
ansible ec2 -i inventory -m ping # Note that you'll have to add your own inventory
```
```
# To provision ec2 instance
# host machine supposed to have appropriate role
# if not you'll need to specify aws_access_key_id and aws_secret_access_key
ansible-playbook aws_ec2_provisioning.yml -i inventory --tags create_ec2 --extra-vars id="an_unique_id_for_your_instance"
```

#### Molecule

```bash
# To create default scenario of test with docker for environment of test and testinfra for test tools
molecule init role docker --verifier-name testinfra --driver-name docker
# To run the scenario 
molecule test # You need to be into the role directory
```

## Authors

Contributors names and contact info

ex. [@simonyerro](https://www.linkedin.com/in/simon-yerro/)

## Acknowledgments

* [based on this tuto](https://www.objectif-libre.com/fr/blog/2019/01/15/ansible-molecule/)

