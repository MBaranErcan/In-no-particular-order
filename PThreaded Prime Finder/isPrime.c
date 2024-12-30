// Example compile:     gcc -o main isPrime.c -pthread
// Example run:         time ./main myDir 4

#include <stdio.h>
#include <semaphore.h>
#include <pthread.h>
#include <dirent.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>

sem_t sem;

int isPrime(int num);
void *threadFunction(void *arg);

// Structure to pass arguments to the thread function.
struct tArgs
{
    char **filePaths;   // Array of file paths
    int thread_id;      // Thread index
    int fileCount;      // Total number of files
    int MAX_THREADS;    // Total number of threads
};



int main(int argc, char const *argv[]) {

    printf("The PID of the main process is %d\n", getpid());    // Print the PID of the main process so follow the output easily.

    int MAX_THREADS = atoi(argv[2]);

// 1- Initialize the semaphore and the threads.
    sem_init(&sem, 0, MAX_THREADS);
    pthread_t threads[MAX_THREADS];

// 2- Open the directory and save the file names in an array.
    char **filePaths = malloc(sizeof(char *)* 100); // Max 100 files.
    int fileCount = 0;
    DIR *dir;
    struct dirent *ent;
    if ((dir = opendir(argv[1])) != NULL) {
        while ((ent = readdir(dir)) != NULL) {
            if (strstr(ent->d_name, ".txt") != NULL) {  // Only txt files.
                filePaths[fileCount] = malloc(sizeof(char) * 250);  // Max 250 charas for file path.
                sprintf(filePaths[fileCount], "%s/%s", argv[1], ent->d_name);
                fileCount++;
            }
        }
        closedir(dir);
    } else {
        perror("Error: ");
    }

// 3- Create the threads and pass the file paths to the threads.
    for (int i = 0; i < MAX_THREADS; i++) {
        struct tArgs *args = (struct tArgs *)malloc(sizeof(struct tArgs));
        args->filePaths = filePaths;
        args->fileCount = fileCount;
        args->MAX_THREADS = MAX_THREADS;
        args->thread_id = i;
        pthread_create(&threads[i], NULL, threadFunction, args);
    }

// 6- Wait for the threads to finish.
    for (int i = 0; i < MAX_THREADS; i++) {
        if(threads[i] == NULL) continue;

        pthread_join(threads[i], NULL);
    }

// 7- Destroy the semaphore.
    sem_destroy(&sem);

    return 0;
}

// Thread function.
void *threadFunction(void *arg){
    sem_wait(&sem);                             // Wait for the semaphore.      
    struct tArgs *args = (struct tArgs *)arg;   // Get the arguments.
    int thread_id = args->thread_id;            // Get the thread index.
    int primeCount = 0;                         // Number of prime numbers in the file. (initially 0)


    // Assume we have N files and T threads.
    // Each thread will process N/T files.
    // If N is not divisible by T, the main thread will process the remaining files.
    int filesPerThread = (int)ceil((float)args->fileCount / args->MAX_THREADS);
    int start = fmin(thread_id * filesPerThread, args->fileCount);
    int end = fmin((thread_id + 1) * filesPerThread, args->fileCount);

    for (int i = start; i < end; i++) {
// 4- Read the file and count the number of prime numbers.
        
        //filename is filepath until the last "/" character. This is only needed to print out the filename.
        char *fileName = strrchr(args->filePaths[i], '/') + 1;

        FILE *file = fopen(args->filePaths[i], "r");    // Open the file.
        if (file != NULL) {
            int num;
            primeCount = 0;
            while (fscanf(file, "%d", &num) != EOF) {   // Read the file and check if the number is prime.
                if (isPrime(num)) {
                    primeCount++;
                }
            }
            fclose(file);
        } else {
            perror("Error: ");
        }

// 5- Print the file name and the number of prime numbers.
            printf("Thread %d has found %d primes in file %s.\n", thread_id, primeCount, fileName);

        sem_post(&sem);

    }

    
    // If this is the main thread, it also processes any remaining files (Since N may not be divisible by T, check any remaining files just in case).
    if ((thread_id == 0 && args->fileCount % args->MAX_THREADS != 0) && 0) {

        sem_wait(&sem);

        for (int i = args->MAX_THREADS * filesPerThread; i < args->fileCount; i++) {

            //filename is filepath until the last "/" character. This is only needed to print out the filename.
            char *fileName = strrchr(args->filePaths[i], '/') + 1;
            
            FILE *file = fopen(args->filePaths[i], "r");    // Open the file.
            if (file != NULL) {
                int num;
                primeCount = 0;
                while (fscanf(file, "%d", &num) != EOF) {   // Read the file and check if the number is prime.
                    if (isPrime(num)) {
                        primeCount++;
                    }
                }
                fclose(file);
            } else {
                perror("Error: ");
            }

            printf("Thread %d has found %d primes in file %s.\n", thread_id, primeCount, fileName); 

            sem_post(&sem);
        }
    }

    pthread_exit(NULL); // Exit the thread.
}


// Function to check if a number is prime.
int isPrime(int num) {
    if (num < 2) {
        return 0; 
    }

    int sqrt_num = ceil(sqrt(num)); // Actually, we only need to check until the square root of the number. This is more efficient than checking until half of the number.
    for (int i = 2; i <= sqrt_num; i++) {
        if (num % i == 0) {
            return 0;
        }
    }

    return 1;
}
