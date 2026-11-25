
# Mission 7 — How Computers Communicate

## 1. Task / objective
The objective was to understand computer networks, learn basic networking concepts, observe network connectivity and DNS lookup, and explain how a website opens.

## 2. Work completed

### Network concepts
| Concept | Explanation | Example |
|---|---|---|
| LAN | Network covering a small area | Home or college lab network |
| MAN | Network covering a city or large campus | City-wide network |
| WAN | Network covering large geographical areas | Internet |
| DNS | Converts a domain name into an IP address | Finding the address for example.com |
| Router | Connects networks and forwards data | Home Wi-Fi router |
| Protocol | Rules used for communication | HTTP, HTTPS |
| Packet switching | Divides data into packets for transmission | Data travelling across the internet |
| Client-server | Client requests a service and server provides it | Browser requesting a webpage |

### Network observations
- Connectivity test command: `ping example.com`
- DNS lookup command: `nslookup example.com`

Connectivity testing helps check whether a destination can be reached over a network. A DNS lookup displays information such as the IP address associated with a domain name.

In this session, `ping example.com` could not resolve the hostname, and `nslookup example.com` could not open a socket. The environment prevented DNS lookup, so these results do not show that the website itself is unavailable. No personal IP address or Wi-Fi details are included.

### What happens when you open a website?
1. The user enters a website name in a browser.
2. The browser acts as a client and checks for the website's address.
3. DNS translates the domain name into an IP address.
4. The computer sends a request through the network and router.
5. The request reaches the website's server using a communication protocol.
6. The server processes the request and sends a response.
7. The browser receives the response and displays the webpage.

## 3. Commands / tools used
- `ping` — checks network connectivity.
- `nslookup` — performs a DNS lookup.
- Terminal — to run networking commands.
- Web browser — to observe website communication.

## 4. My understanding
I learned that computer networks allow devices to exchange information. DNS helps browsers find websites using domain names. Routers forward data between networks, and protocols define the rules for communication between clients and servers.

## 5. Difficulties faced
A difficulty was separating a DNS lookup problem from a website or connectivity problem.

## 6. How I resolved them
I compared the purpose of `ping` and `nslookup` and described only the lookup failure observed in this session, without assuming the website was down.

## 7. Evidence / files
- Network concepts table
- Connectivity and DNS observations
- Website request explanation
- This README

## 8. Commit details
Commit message: Explain networking concepts and website communication.
GitHub repository: [cherryx18/digital-detective-8455](https://github.com/cherryx18/digital-detective-8455).
