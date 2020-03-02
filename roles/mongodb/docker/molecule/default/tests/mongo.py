import os
import testinfra.utils.ansible_runner
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ[‘MOLECULE_INVENTORY_FILE’]).get_hosts(‘all’)

def test_mongo(host):
    os = host.system_info.distribution

    if os == "ubuntu":
        mongo = host.service("mongodb")
        assert mongo.is_running
        assert mongo.is_enabled
