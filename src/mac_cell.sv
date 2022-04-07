
module mac_cell(

	input logic [7:0] a_in,
	input logic [7:0] b_in,

	input logic clk,
	
	output reg [7:0] c,
	output reg [7:0] a_out,
	output reg [7:0] b_out

	);


initial 
begin 
	c = 0;
end 

always @(posedge clk)
begin

	a_out <= a_in;
	b_out <= b_in;
	
	if(a_out && b_out)	
		c = c + a_out * b_out;

	// $display("a_in = %d",a_in);
	// $display("b_in = %d",b_in);
	// $display("c before out = %d",c);
	// $display("--------------------");
end 


endmodule