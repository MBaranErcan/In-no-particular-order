// Half Adder Testbench
module half_adder_TB();

    reg  a, b;
    wire  sum, carry;

    half_adder uut(a, b, sum, carry);

    initial
        begin
        a = 0; b =0;
        #5; a = 0; b =1;
        #5; a = 1; b =0;
        #5; a = 1; b =1;
        #5;
        end
  
 //Dump waves (only required here)
initial
  begin
    $dumpfile("dump.vcd");
    $dumpvars(1);
  end 
 endmodule
