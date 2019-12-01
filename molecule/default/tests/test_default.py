import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

def test_pkg(host):
    # get variables from file
    ansible_vars = host.ansible("include_vars", "file=main.yml")
    # check packages
    for pkg in ansible_vars['ansible_facts']['package_omd']:
        omd_pkg = host.package(pkg)
        assert omd_pkg.is_installed

def test_service(host):
    # get variables from file
    ansible_vars = host.ansible("include_vars", "file=main.yml")
    # check sites
    for pkg in ansible_vars["ansible_facts"]["package_omd"]:
        if host.ansible("setup")["ansible_facts"]["ansible_os_family"].lower() == "debian":
            omd_srv = host.service(pkg)
        else:
            omd_srv = host.service("omd")
        assert omd_srv.is_running
        assert omd_srv.is_enabled

def test_sites(host):
    # get variables from file
    ansible_vars = host.ansible("include_vars", "file=main.yml")
    # check sites
    for site in ansible_vars["ansible_facts"]["omd_sites"]:
        with host.sudo():
            # check if site exists
            cmd_status = host.run("omd status %s", site["name"])
            assert cmd_status.succeeded
            # check core
            cmd_core = host.run("omd config %s show CORE", site["name"])
            assert cmd_core.stdout.strip() == site["core"]
            # check default_ui
            cmd_core = host.run("omd config %s show DEFAULT_GUI", site["name"])
            assert cmd_core.stdout.strip() == site["default_gui"]