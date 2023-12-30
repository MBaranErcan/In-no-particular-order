module dff (clk, reset,
            d, q, qb);
  
  input clk, reset, d;
  output q, qb;
  
  reg q;
  
  assign qb = ~q;
  
  
  always @(posedge clk or posedge reset)
    begin
      if (reset) begin
        q <= 1'b1;
      end else begin
        q <= d;
      end
    end
endmodule