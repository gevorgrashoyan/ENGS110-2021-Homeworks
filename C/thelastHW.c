#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *iFptr, *oFptr, *stream;
    iFptr = fopen("data.txt", "r");
    if (! iFptr ) {                                     // check for error
        printf("data.txt can't be read\n"); 
        exit(-1); 
    } 
    fseek(iFptr, 0, SEEK_END);
    long fsize = ftell(iFptr);
    fseek(iFptr, 0, SEEK_SET);

    char *buffer = malloc(fsize + 1);
    fread(buffer, 1, fsize, iFptr);
    buffer[fsize] = 0;
    fclose(iFptr);

    int numbers, number, sum = 0;
    stream = fmemopen(buffer, fsize + 1, "r");
    if (fscanf(stream, "%d", &numbers) >= 0)
        while (numbers-- > 0)
            if (fscanf(stream, "%d", &number) == 1)     // read to end of file
                sum += number;
            else {
                printf("could not read all numbers from data.txt\n"); 
                exit(-1); 
            }
    else {                                              // error
        printf("could not read from memory stream\n"); 
        exit(-1); 
    }
    fclose(stream);
    free(buffer);

    oFptr = fopen("result.txt", "wb");
    if (! oFptr ) {                                     // check for error
        printf("result.txt can't be written\n"); 
        exit(-1); 
    } 
    fprintf(oFptr, "%d\n", sum);
    fclose(oFptr);
    
    return 0;
}

