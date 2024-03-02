1. **Update Homebrew**: Make sure your Homebrew installation is up to date by running:

   ``` 
   brew update
    ```


2. **Install PHP 8.0.0**: You can install PHP 8.0.0 by specifying the version with the `@` symbol:
   
``` 
brew install php@8.0
```


4. **Manage Multiple PHP Versions**: Homebrew provides a tool called `brew link` to manage multiple versions of the same package. After installing PHP 8.0.0, you may need to link it:
   
   ```
   brew link --force --overwrite php@8.0
   ```


This command will ensure that the installed version of PHP 8.0.0 is linked and ready to use.

5. **Verify Installation**: You can verify that PHP 8.0.0 is installed correctly by running:
   
``` 
php -v
```


This command will display the installed PHP version. Make sure it shows PHP 8.0.0.

6. **Switch Between PHP Versions (Optional)**: If you need to switch between PHP versions, you can use the `brew unlink` and `brew link` commands. For example, to switch back to PHP 8.3.3:
   
   ```
   brew unlink php@8.0
   brew link --force --overwrite php
   
   ```

**These steps with commands should be more helpful for executing the necessary actions. Let me know if you need further clarification or assistance!

# Troubleshooting
If you encounter the below error 
   ``` php@8.0 has been disabled because it is a versioned formula! ```
Then follow the below steps

   ``` brew tap shivammathur/php ```
   
   ``` brew install shivammathur/php/php@8.0 ```
   
   ``` brew link --force --overwrite php@8.0 ```
   
   ``` php -v ``` 
** Disable PHP 8.3 Module: First, you need to disable the PHP 8.3 module. If PHP 8.3 was installed using Homebrew, you can use the following command:

   ``` sudo a2dismod php8.3 ```

** Enable PHP 8.0 Module: Next, enable the PHP 8.0 module:

   ``` sudo service apache2 restart ``` 






