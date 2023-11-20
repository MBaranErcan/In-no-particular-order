// Half Adder
// sum = a ^ b
// carry = ab

module half_adder(a, b, sum, carry);
  input a, b;
  output sum, carry;

  assign sum = a ^ b; // assigning sum
  assign carry = a & b; // assigning carry

endmodule