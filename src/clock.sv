// `timescale 1ns/1ns

module clock(
	output reg clk_out
	);

initial
begin
	clk_out = 0;
	#1000
	$finish;
end 

always 
begin 
	#5
	clk_out = 1;
	#5
	clk_out = 0;
end 

endmodule 