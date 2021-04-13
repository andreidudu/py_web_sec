#!/bin/python3

#get domain name of any URL

from tld import get_fld

def get_domain_name(url):
	domain_name = get_fld(url)
	return domain_name
	

