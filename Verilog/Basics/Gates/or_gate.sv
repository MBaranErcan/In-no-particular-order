module or_gate_example (
    input a,
    input b,
    output y
    );

input a;
input b;
output y;

wire or_temp;

assign or_temp = a | b;

assign y = or_temp;
    
endmodule  // Or Gate Example