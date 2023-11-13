/*
Task 3
C Code:
int array [1000];
int a;
for (a=0; a<=1000; a=a+2)
array[a]=array[a]*2;
*/

    # MIPS Assembly Code
    # $s0 = 0x12348000 (array base address)
    # $s1 = a

start_:
    lui  $s0, 0x1234            # $s0 = 0x12340000
    ori  $s0, $s0, 0x8000       # $s0 = 0x12348000
    addi $s1, $0, 0             # a = 0
    addi $t3, $0, 1001          # $t3 = 1001 (<=1000 |same as| <1001)

loop:
    slt $t0, $s1, $t3           # a < 1001 ?
    beq $t0, $0, done           # if not then jump done
    sll $t1, $s1, 2             # $t1 = a * 4 (byte offset, address)
    add $t1, $t1, $s0           # address of array[a]
    lw  $t2, 0($t1)             # $t2 = array[a]
    sll $t2, $t2, 1             # array[a] = array[a]*2
    sw  $t2, 0($t1)
    addi $s1, $s1, 2            # a = a + 2, array index
    j loop                      # repeat
done: