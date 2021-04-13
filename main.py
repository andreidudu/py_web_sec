#!/bin/python3
 
from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *

root_dir = 'websites'
create_dir(root_dir)
 

 
def gather_info(name, url):
	print("* Getting the domain name.")
	domain_name = get_domain_name(url)
	print("* Getting the IP address")
	ip_address = get_ip_address(url)
	print("* Performing NMAP scan")
	nmap = get_nmap(' -F', ip_address)
	print("* Fetching robots.txt file")
	robots_txt = get_robots_txt(url)
	print("* Finding out who is")
	whois = get_whois(domain_name)
	print("* Creating the report. Thank you for using our software. *")
	create_report(name, url, domain_name, nmap, robots_txt, whois) 	
	
	
def create_report(name, url, domain_name, nmap, robots_text, whois): 	
	project_dir = root_dir + '/' + name
	create_dir(project_dir)
	write_file(project_dir + '/full_url.txt', url)
	write_file(project_dir + '/domain_name.txt', domain_name)
	write_file(project_dir + '/nmap.txt', nmap)
	write_file(project_dir + '/robots.txt', robots_text)	
	write_file(project_dir + '/whois.txt', whois)
	
target = input('Please enter your target (https://www.target.com/)  ')
site = get_domain_name(target)
gather_info(site, target)
