/*
Task 2
C Code:
int a=128;
int b=0;
while (a!=1){
a=a/2;
b=b+1;}
*/

    # MIPS Assembly Code
    # $s0 = a
    # $s1 = b

start_:
    addi $s0, $0, 128           # a = $s0 = 128
    addi $s1, $0, 0             # b = $s1 = 0
    addi $t0, $0, 1             # t0 = 1 (create a temp value to hold the value 1)
while:
    beq  $s0, $t0, done         # if a equals 1, jump to done
    sra  $s0, $s0, 1            # divide a by 2, then save it into a.
    addi $s1, $s1, 1            # b = b + 1
    j while
done:
