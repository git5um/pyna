from napalm import get_network_driver
import pprint as pp
import yaml


def run_compliance(net_os, net_host, uname, passw, comp_file):
    driver = get_network_driver(net_os)
    device = driver(net_host, uname, passw)
    device.open()
    pp.pprint(device.compliance_report(comp_file))
    device.close()

if __name__ == "__main__":
    with open("net_info.yml") as f:
        myaml = yaml.load(f, Loader=yaml.SafeLoader)
        for sw in myaml:
            for compf in sw['comp_files']:
                run_compliance(sw['os'], sw['name'], sw['user'], sw['passw'], compf)

