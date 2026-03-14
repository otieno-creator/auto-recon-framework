import xml.etree.ElementTree as ET
import os

def parse_nmap_xml(file_path):
    """Parses Nmap XML output to extract open ports and services."""
    if not os.path.exists(file_path):
        return "Scan file not found."

    tree = ET.parse(file_path)
    root = tree.getroot()
    report = "## Security Scan Report\n\n"

    for host in root.findall('host'):
        ip = host.find('address').get('addr')
        report += f"### Host: {ip}\n| Port | State | Service | Version |\n|------|-------|---------|---------|\n"
        
        for port in host.find('ports').findall('port'):
            port_id = port.get('portid')
            state = port.find('state').get('state')
            service = port.find('service').get('name') if port.find('service') is not None else "Unknown"
            version = port.find('service').get('product') if port.find('service') is not None else "N/A"
            
            if state == 'open':
                report += f"| {port_id} | {state} | {service} | {version} |\n"
    
    return report

if __name__ == "__main__":
    print("Recon Parser initialized. Ready to process Nmap XML data.")
