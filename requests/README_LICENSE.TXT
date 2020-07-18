Requests: HTTP for Humans
Release v2.6.0
Requests is an Apache2 Licensed HTTP library, written in Python, for human beings.

http://docs.python-requests.org/en/latest/

APACHE 2.0 licensed
http://docs.python-requests.org/en/latest/user/intro/#apache2-license

Since we are using this via Jython, the source distribution is included here.  Note that there was one modification required to 
requsts to make it Jython 2.5.3 compatible:  models.py line 368 was updated to replace 'idna' with 'utf-8' per the following thread:
http://stackoverflow.com/questions/14919557/how-to-get-urllib3-and-requests-working-with-jython-2-7-beta-1
