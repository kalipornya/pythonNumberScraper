#!/usr/bin/env python3
import requests
import sys
import re

# define regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))             # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)?                    # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
httpRegex = re.compile(r'^(http(s)?://).*')

#define var
url = ""
resp = ""
phone_list = ""

if 1 < len(sys.argv) < 3:	# test for correct args
	url = sys.argv[1]
	while httpRegex.search(str(sys.argv[1])) == None:	# test for valid URL
		print("Invalid URL. Please enter a valid URL:")
		url = input("> ")	
		if httpRegex.search(url) == None:
			continue
		if httpRegex.search(url).group(1) == "http://" or "https://":
			break
	print("Target URL set to: " + url)
	resp = requests.get(url)
	phone_list = list(set(phoneRegex.findall(resp.text))) # set removes duplicates
	f = open(input("Enter output filename: "), "w")
	for n in range(len(phone_list)):
		f.write(phone_list[n][0] + "\n")
else:
	print("Usage: " + sys.argv[0] + " target_URL")