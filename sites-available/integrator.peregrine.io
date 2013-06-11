
NameVirtualHost *:80

#used for mod_status 
ExtendedStatus On

<VirtualHost *:80>

    # packages required for this to work:
    # apache2-mpm-prefork
    # php5
    # php5-memcache
    # php5-curl
    # smarty

    ServerName peregrine.integration.spinn3r.com 
    ServerAlias integration.peregrine.io

    LogFormat "%{X-Forwarded-For}i %h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\" %V %T %D" mylogformat

    CustomLog /var/log/apache2/integrator.peregrine.io-access.log mylogformat
    ErrorLog  /var/log/apache2/integrator.peregrine.io-error.log

    <Directory />

        Order Allow,Deny
        Allow from all

        #don't allow people to browse the filesystem.
        Options +Indexes

    </Directory>

    DocumentRoot /var/lib/integration/peregrine

</VirtualHost>
