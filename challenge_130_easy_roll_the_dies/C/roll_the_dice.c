/**********************************************************/
/* This file is published under the 3-clause BSD license. */
/* Copyright 2014 Manolis Fragkiskos Ragkousis		  */
/* Check the license file.				  */
/**********************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int 
main(int argc, char **argv)
{
  const char s[2]="d";
  char *token;
  int num_of_dices;
  int num_of_faces;
  
  if(!(token = strtok(argv[1], s)))
    {
      puts("wrong input, insert NdM");
      exit(-1);
    }
  num_of_dices = atoi(token);
  
  token = strtok(NULL, s);
  num_of_faces = atoi(token);
  
  printf("%dd%d dice(s) roll... ",num_of_dices,num_of_faces);

  srand(time(NULL));
  for(int i=0;i<num_of_dices;i++)
    printf("%d ",(rand() % num_of_faces)+1);
  printf("\n");

  return 0;
}
