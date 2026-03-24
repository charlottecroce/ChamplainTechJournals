#include <stdlib.h>
#include <pwd.h>
#include <stdio.h>
#include <unistd.h>

/*
sec335 illustrate SUID programs

make sure run the following:
  sudo chown root:root effective_user.c
  sudo chmod u+s effective_user.c
*/

int main(int artc, char *argv[])
{
  struct passwd *pw;
  uid_t uid;

  uid = geteuid();
  pw = getpwuid (uid);
  if (pw)
  {
    puts (pw->pw_name);
    exit (EXIT_SUCCESS);
  }
  else
  {
    puts ("Error");
    exit (EXIT_FAILURE);
  }
}
