# Install php 
  ```brew install php httpd mysql```

## start httpd

  ```brew services start httpd```

## open /usr/local/etc/httpd/httpd.conf
 1. Add the below one into this file
    
``` 
  LoadModule php_module /usr/local/opt/php/lib/httpd/modules/libphp.so
  
  <FilesMatch \.php$>
      SetHandler application/x-httpd-php
  </FilesMatch>

 ```
2. change port number
   
  ``` 
    Listen 80
  ```

3. Change the root directory 

```
  DocumentRoot "/your/project/path"
  <Directory "/your/project/path">

```
4. Add index.php for Directory index

   ```
   <IfModule dir_module>
      DirectoryIndex index.html index.php
   </IfModule>
   ```
5. After made changes in the file save then run the below command in your terminal
   
   ``` brew services restart httpd ```


## Run the below command if mysql_secure_installation is not triggerred when you brew install 

  ``` mysql_secure_installation ```

## Trouble shooting step 
  * If http://localhost is not working run the below command and see the result
    
  ``` sudo lsof -i :80 ```
  
 * Check the services list
   
  ``` brew services list ```
  
 * To stop and start httpd
   
  ``` 
  brew services restart httpd
  brew services start httpd
  brew services stop httpd
 ```

  



