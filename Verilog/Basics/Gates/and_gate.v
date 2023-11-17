module and_gate (
    input a,
    input b,
    output y
    );
);

input a;
input b;
output y;

wire and_temp;

assign and_temp = a & b;

assign y = and_temp;
    
endmodule  // Example And Gate