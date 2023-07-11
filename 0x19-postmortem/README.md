# Postmortem
On 1/22/22 at 5:23 pm EAT, 100% of the website's service was down for a total 12 minutes, with service reinstated at 5:35 pm EAT. Users universally experienced a response with a status code of 500 (internal server error). The root cause of the outage was a single-letter, typographical error in which a `.php` file was typed as a `.phpp` file.

## Timeline for 1/22/22 (EAT):
**5:23 pm:** After deploying a WordPress update, a junior engineer noticed that the website was returning a 500 status code.

**5:25 pm:** All running processes on a particular server were checked using `ps auxf`. Apache2 and MySQL were found to be running as expected, indicating an error with PHP/WordPress.

**5:26 pm:** The WordPress configuration file `/var/www/html/wp-config.php` was edited to enable debug mode.

**5:27 pm:** The website was curled to reveal a fatal error, a missing file `/var/www/html/wp-includes/class-wp-locale.phpp` required in `/var/www/html/wp-settings.php`. The nonexistent `.phpp` extension indicated a potential typographical error.

**5:28 pm:** `ls` was used to check the contents of  `/var/www/html/wp-includes/`.  It was discovered that the file `/var/www/html/wp-includes/class-wp-locale.php ` existed, confirming a typographical error was made.

**5:30 pm:** The typographical error was fixed on the individual server using `sed -i 's/phpp/php/' /var/www/html/wp-settings.php`. 

**5:31 pm:** Website service was then tested once more, with content being served as expected.

**5:32 pm:** A puppet manifest was developed to fix this issue on a large scale.

**5:35 pm:** The puppet manifest was deployed on all remaining servers, bringing website service back to 100%. 

## Root cause and resolution:
The root cause of this outage was a typo made in the php file `/var/www/html/wp-settings.php` in which the file `/var/www/html/wp-includes/class-wp-locale.phpp` was required. The extension of `.phpp` was a typographical error, meant to be `.php`. Since `/var/www/html/wp-includes/class-wp-locale.phpp` did not exist and was required, a fatal error was raised, preventing content from being served. Since this code was deployed on all servers, this error caused a 100% outage. A puppet manifest to fix the typographical error was developed and deployed on all servers, reinstating service within 12 minutes of the outage.

## Corrective and preventative measures:
To prevent wide-scale issues like this from occurring in the future, code should never be deployed on all servers before testing. Some things to consider for the future are: the development of company-wide testing protocol, setting up isolated docker containers for testing purposes, and the implementation of a two-person sign-off before major deployment.
