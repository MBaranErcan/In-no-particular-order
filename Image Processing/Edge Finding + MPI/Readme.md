>M. Baran Ercan & Bedir Esen

### Introduction
A parallelized image edge detection filter utilizing MPI for distributed computation. By analyzing speedup and efficiency across varying thread counts and image sizes, study highlights the performance trade-offs and bottlenecks associated with MPI_Bcast communication.


### Filter That We Use

![image](https://github.com/user-attachments/assets/83f6e6cf-487f-4a88-931e-d107f9c9f06d)

Our filter iterates on every pixel of the image, and by multiplying the values in the filter it creates a new
pixel. So that, at the end an image with edges extracted is created.


### MPI Broadcast

![image](https://github.com/user-attachments/assets/3255ea6a-092d-4431-9ebb-a150b97ed0e8)

Here, our master node shares the data to slaves using MPI_Bcast method.

#### Times, Efficiency and Speedup
n = 10mb t = comparison between 1, 2, 3, 4, 8, 16, 20 threads
Tserial = 3.209s

Tt=2 = 2.163s

Tt=3 = 1.763s

Tt=4 = 2.183s

Tt=8 = 2.165s

Tt=16 = 2.241s

Tt=20 = 2.302s


Speedup (S) = Tserial / Tparallel

S2 = 1,484

S3 = 1,820

S4 = 1,47

S8 = 1,482

S16 = 1,432

S20 = 1,394


Efficiency E = S / p
E2 = 0.742
E3 = 0.606
E4 = 0.368
E8 = 0.185
E16 = 0.0895
E20 = 0.087

![image](https://github.com/user-attachments/assets/c6d8d499-b498-465a-9f67-c0b5ec43f2f6)
![image](https://github.com/user-attachments/assets/e18503d8-8eb6-477e-91eb-954b5ff30de7)




n = 50mb t = comparison between 1, 2, 3, 4, 8, 16, 20 threads

Tserial = 12.592s

Tt=2 = 10.692s

Tt=3 = 10.254s

Tt=4 = 9.61s

Tt=8 = 8.881s

Tt=16 = 8.01s

Tt=20 = 8.973s

Speedup (S) = Tserial / Tparallel

S2 = 1.177

S3 = 1.228

S4 = 1.31

S8 = 1.417

S16 = 1.572

S20 = 1.403

Efficiency E = S / p

E2 = 0.5885

E3 = 0.409

E4 = 0.3275

E8 = 0.177

E16 = 0.098

E20 = 0.07

![image](https://github.com/user-attachments/assets/2f92c64d-0527-4ebd-aaef-1c4c92adae06)
![image](https://github.com/user-attachments/assets/da7f08d3-2957-44ed-9b9b-5d3fd42b0a80)


### Conclusion

To conclude, we observed that increasing the image size, makes our MPI parallelized filtering code
faster. The efficiency in the greater size decreases but when concerning the speedup, we get better results.
We think that the main reason of unbalanced situation in the speedup in the smaller sizes is nature of the
MPI_Bcast method. Master sends so that shares the data to slave processes. This time-consuming
situation creates an unbalanced situation in small data sizes.

![image](https://github.com/user-attachments/assets/bd98ceeb-bc74-4797-9291-6002269d6b00)
