/*
TASK 1
C Code:
int a=12;
int b=23;
if (a>b)
c=a*2;
else 
d=a+b;
*/

    # MIPS Assembly Code
    # $s0 = a
    # $s1 = b
    # $s2 = c
    # $s3 = d

start_:
    addi $s0, $0, 12        # a = $s0 = 0 + 12
    addi $s1, $0, 23        # b = $s1 = 0 + 23
    addi $s2, $0, 0         # c = $s2 = 0
    addi $s3, $0, 0         # d = $s3 = 0
    slt  $t0, $s1, $s0      # if b < a, $t0 becomes 1, otherwise its 0.
    beq  $t0, $0, else      # if $t0 is 1 go to else, if 
    sll  $s2, $s0, 1        # c = (a*2)
    j done
else:
    addi $s3, $s0, $s1      # else, d = (a + b)
done:
