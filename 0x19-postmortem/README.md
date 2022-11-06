# 804-web-01 server outage incident report

By [Mofor Emmanuel](https://github.com/moforemmanuel)

## Issue Summary

From 9:30 AM to 4:15 PM GMT +1, every attempt to login into the 804-web-01 server with ssh failed with error ERR_CONNECTION_REFUSED. Due to this, no work could could be done on the server, as well as the server couldn't provide any assets, data or functionality. The root cause of this outage was the fact that port 22 (ssh) was not allowed on the server's firewall.

## Timeline (all times Greenwich Mean Time +1)

- 9:20 AM: Installation of Nginx Server
- 9:30 AM: Outage begins
- 9:55 AM: Inaccessibility noticed
- 12:30 PM: Debugging begins
- 1:45 PM: Suspected Error reproduction begins
- 3:24 PM: Error detected
- 4:15 PM: Server reinstalled, and port 22 allowed on firewall

## Root Cause

At 9:20 AM GMT +1, an Nginx server was installed, which would be used to host website files and assets.
With the installation complete, on configuring the server, I forgot to allow port 22 for ssh access on th server's firewall, then logout out.
On accessing the server later for use, the firewall kept blocking me out (refusing my connection).

Imagine your car door locks automatically by default when you leave the car. Now you leave the car, but left your keys inside. There's only two ways you can get back into the car, with a spare key (which you don't have), or you break into your own car, LOL.

This rendered the server useless to me, as I couldn't log into it, however, site visitors could access the files hosted as port 80 and 8080 were allowed, however, they would be browsing stale data.
After several attempts of trying to log into the system, changing internet connection, and restarting host computer, I then realized there was a problem, and with that, the server outage began at 9:30 AM GMT +1.

## Resolution and recovery

At 9:55 AM GMT +1, I noticed the inaccessibility of the server, and quickly resorted to analyze the situation. By 3:42 PM, I found out the cause of the problem.

After debugging the issue and gotten to the root of it, I quickly sought to fix the problem, and the first and most obvious way was to reinstall the server, because connections to port 22 were blocked, it would be impossible to ever get into the system. This fixed the issue, and I re-uploaded the content to the server, and everything was working fine by 4:15 PM.

## Corrective and Preventative Measures

Following the incident, I conducted further analysis of the outage to prevent such from happening in the future, and took the following actions:

- Always ensure Port 22 (SSH) is allowed for a firewall configuration before logging out of the server
- Install Spyware to hack into the server incase of such an incident
- Prompt User to check firewall settings before logging out of server

I am committed to continually and quickly improving the technology and operational processes to prevent outages. I appreciate your patience and again apologize for the impact to you, your users, and your organization.

Sincerely,

Mofor Emmanuel
