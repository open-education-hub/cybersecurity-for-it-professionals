#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define SHELL_SIZE 200

int main()
{
  char shellcode[SHELL_SIZE];
  memset(shellcode, 0, SHELL_SIZE);
  read(0, shellcode, SHELL_SIZE);

  void (*func_ptr)(void) = (void (*)(void)) shellcode;

  /* Call shellcode. */
  func_ptr();

  return 0;
}
