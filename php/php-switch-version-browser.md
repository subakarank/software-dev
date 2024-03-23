# Assume that you have disabled default installed apache from Mac and using brew httpd

Go to 
``` /usr/local/etc/httpd/httpd.conf ```

Add 
```
LoadModule php_module /usr/local/opt/php@8.0/lib/httpd/modules/libphp.so
LoadModule php_module /usr/local/opt/php@8.3/lib/httpd/modules/libphp.so

```
**To enable 8.0**
 - Comment the below one
``` LoadModule php_module /usr/local/opt/php@8.3/lib/httpd/modules/libphp.so ```
- Uncomment the below one
  ``` LoadModule php_module /usr/local/opt/php@8.0/lib/httpd/modules/libphp.so ```

**To enable 8.3**
 - Comment the below one
``` LoadModule php_module /usr/local/opt/php@8.0/lib/httpd/modules/libphp.so ```
- Uncomment the below one
  ``` LoadModule php_module /usr/local/opt/php@8.3/lib/httpd/modules/libphp.so ```

