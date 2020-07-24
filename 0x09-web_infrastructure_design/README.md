<h1>WEB INFRAESTRUCTURE DIAGRAMS</h1>

<h3>0-SIMPLE_WEB_STACK </h3>

The most simples web infraestrucure using the LAMP STACK

1 server
1 web server (Nginx)
1 application server
1 application files (your code base)
1 database (MySQL)
1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8


<h3>1-DISTRIBUIED_WEB_INFRASTRUCTURE</h3>

three server web infrastructure that hosts the website, a load balancer for the request flow

2 servers
1 web server (Nginx)
1 application server
1 load-balancer (HAproxy)
1 set of application files (your code base)
1 database (MySQL)


<h3>2-secured_and_monitored_web_infrastructure</h3>

 three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.

3 firewalls
1 SSL certificate to serve www.foobar.com over HTTPS
3 monitoring clients (data collector for Sumologic or other monitoring services)
