from pubproxpy import Level, Protocol, ProxyFetcher

# ProxyFetcher for proxies that use the socks5 protocol, are located in
# the US or Canada and support POST requests
socks_pf = ProxyFetcher(
    protocol=Protocol.SOCKS5, countries=["US", "CA"], post=True
)

# ProxyFetcher for proxies that support https, are elite anonymity level,
# and connected in 15 seconds or less
https_pf = ProxyFetcher(
    protocol=Protocol.HTTP, https=True, level=Level.ELITE, time_to_connect=15
)

# Get one socks proxy, followed by 10 https proxies
# NOTE: even though there are multiple `ProxyFetcher`s the delays are
#       coordinated between them to prevent rate limiting
socks_proxy = socks_pf.get()[0]  # Get a single socks proxy
https_proxies = https_pf.get(10)  # Get a 10 https proxies
print(https_proxies)
