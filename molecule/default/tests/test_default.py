"""
Molecule unit tests
"""
import os
import testinfra.utils.ansible_runner

TESTINFRA_HOSTS = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_repo(host):
    """
    check if correct repository is used (stable/testing)
    """
    # get variables from file
    ansible_vars = host.ansible("include_vars", "file=main.yml")
    # check if correct repo is used (stable/testing)
    os = host.ansible("setup")["ansible_facts"]["ansible_os_family"].lower()
    if os == "debian":
        distro = host.ansible("setup")["ansible_facts"]["ansible_distribution"].lower()     # noqa: E501
        repo_file = host.file(
            "/etc/apt/sources.list.d/labs_consol_de_repo_%s_%s.list" %
            (ansible_vars["ansible_facts"]["omd_repo_flavor"], distro)
        )
    elif os == "redhat":
        repo_file = host.file(
            "/etc/yum.repos.d/consol-omd.repo"
        )
    elif os == "suse":
        repo_file = host.file(
            "/etc/zypp/repos.d/consol-omd.repo"
        )
    assert ansible_vars["ansible_facts"]["omd_repo_flavor"] \
        in repo_file.content_string


def test_pkg(host):
    """
    check if package is installed
    """
    # get variables from file
    ansible_vars = host.ansible("include_vars", "file=main.yml")
    # check packages
    for pkg in ansible_vars["ansible_facts"]["omd_package"]:
        omd_pkg = host.package(pkg)
        assert omd_pkg.is_installed


def test_service(host):
    """
    check if service is running
    """
    # get variables from file
    ansible_vars = host.ansible("include_vars", "file=main.yml")
    # check services
    for pkg in ansible_vars["ansible_facts"]["omd_package"]:
        if host.ansible("setup")["ansible_facts"]["ansible_os_family"].lower() == "debian":     # noqa: E501
            # service name includes omd version
            omd_srv = host.service(pkg.replace(
                "omd", "omd-%s" % ansible_vars["ansible_facts"]["omd_version"])
                )
        else:
            omd_srv = host.service("omd")
        assert omd_srv.is_running
        assert omd_srv.is_enabled


def test_sites(host):
    """
    check if sites are running configuration values are matching variables
    """
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

# TODO: def test_password
