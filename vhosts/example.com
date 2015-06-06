server {
        listen       127.0.0.2:8080;
        server_name  example.com www.example.com;
        root         /etc/nginx/websites/example.com;
	index index.html index.htm;
        #charset koi8-r;

        #access_log  /var/log/nginx/host.access.log  main;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
		
		try_files $uri $uri/ /index.html;
        }

        # redirect server error pages to the static page /40x.html
        #
#        error_page  404              /404.html;
#        location = /40x.html {
#        }

        # redirect server error pages to the static page /50x.html
        #
#        error_page   500 502 503 504  /50x.html;
#        location = /50x.html {
#        }
}

