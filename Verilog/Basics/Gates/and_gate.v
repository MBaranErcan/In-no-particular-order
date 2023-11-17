module and_gate_example (
    input a,
    input b,
    output y
    );

input a;
input b;
output y;

wire and_temp;

assign and_temp = a & b;

assign y = and_temp;
    
endmodule  // And Gate Example