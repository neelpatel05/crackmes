#include<stdio.h>
#include<stdint.h>
#include<stdlib.h>

long some_function(long string,int value, char value1)
{
  int x;
  x = 0;
  while (x < value) {
    *(char *)(string + x) = *(char *)(string + x) ^ value1;
    x = x + 1;
  }
  return string;
}

int main()
{

	long local = 0x3534323160376761;
	char *x;
	x = (char *)some_function(local, 0x20, 3);
	puts(x);
}
