import nmap3
nmap = nmap3.Nmap()
results = nmap.scan_top_ports("scanme.nmap.org")
# And you would get your results in json
