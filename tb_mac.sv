`include "clock.sv"
`include "mac_cell.sv"


module tb_mac;

wire clk;
clock CLOCK(.clk_out(clk));

reg [7:0] C [15:0];
wire [7:0] C_wire [15:0];
reg [7:0] A [3:0];
reg [7:0] B [3:0];

wire [7:0] a_out_t [15:0];
wire [7:0] b_out_t [15:0];

integer j;
reg [14:0] cnt; // sizeof(vec1) + sizeof(vec2) - 1
// reg [7:0] result [7:0];

initial
begin 

	$dumpfile("tb_mac.vcd");
	$dumpvars(0,tb_mac);

	cnt = 0;

	for (j=1; j<4; j=j+1) begin
		A[j] = 0;
		B[j] = 0;
	end

	// B[0] = 1;
	// A[0] = 1;
	// #10
	// B[1] = 1;
	// A[1] = 1;	
	// #10	
	// B[2] = 1;
	// A[2] = 1;	
	// #10	
	// B[3] = 1;	
	// A[3] = 1;	
	// #10	
	
	// B[0] = 0;
	// A[0] = 0;
	// #10	
	// B[1] = 0;
	// A[1] = 0;
	// #10	
	// B[2] = 0;
	// A[2] = 0;
	// #10	
	// B[3] = 0;
	// A[3] = 0;

	#500
	$finish;

end 


mac_cell cell_00( // LEFT MOST CELL
	.a_in(A[0]),
	.b_in(B[0]),
	.clk(clk),
	.c(C_wire[0]),

	.a_out(a_out_t[0]),
	.b_out(b_out_t[0])
	);

mac_cell cell_10( // LEFT MOST CELL
	.a_in(A[1]),
	.b_in(b_out_t[0]),
	.clk(clk),
	.c(C_wire[4]),

	.a_out(a_out_t[4]),
	.b_out(b_out_t[4])
	);

mac_cell cell_20( // LEFT MOST CELL
	.a_in(A[2]),
	.b_in(b_out_t[4]),
	.clk(clk),
	.c(C_wire[8]),

	.a_out(a_out_t[8]),
	.b_out(b_out_t[8])
	);

mac_cell cell_30( // LEFT MOST CELL
	.a_in(A[3]),
	.b_in(b_out_t[8]),
	.clk(clk),
	.c(C_wire[12]),

	.a_out(a_out_t[12]),
	.b_out(b_out_t[12])
	);

genvar i;
generate
  	for (i=1; i<4; i=i+1) begin
  		mac_cell cells(
			.a_in(a_out_t[i-1]),
			.b_in(B[i]),
			.clk(clk),
			.c(C_wire[i]),

			.a_out(a_out_t[i]),
			.b_out(b_out_t[i])
			);
	end
endgenerate
generate
  	for (i=5; i<8; i=i+1) begin
  		mac_cell cells(
			.a_in(a_out_t[i-1]),
			.b_in(b_out_t[i-4]),
			.clk(clk),
			.c(C_wire[i]),

			.a_out(a_out_t[i]),
			.b_out(b_out_t[i])
			);
	end
endgenerate
generate
  	for (i=9; i<12; i=i+1) begin
  		mac_cell cells(
			.a_in(a_out_t[i-1]),
			.b_in(b_out_t[i-4]),
			.clk(clk),
			.c(C_wire[i]),

			.a_out(a_out_t[i]),
			.b_out(b_out_t[i])
			);
	end
endgenerate
generate
  	for (i=13; i<16; i=i+1) begin
  		mac_cell cells(
			.a_in(a_out_t[i-1]),
			.b_in(b_out_t[i-4]),
			.clk(clk),
			.c(C_wire[i]),

			.a_out(a_out_t[i]),
			.b_out(b_out_t[i])
			);
	end
endgenerate

integer k;
always @(posedge clk)
begin 
	for(k=0;k<16;k++) begin
		C[k] = C_wire[k];
	end 

	for (j=0; j<4; j=j+1) begin	
		$display(
			"[%d]",C[4*j+0],"[%d]",C[4*j+ 1],"[%d]",C[4*j+ 2],"[%d]",C[4*j+ 3]
			);
	end
	$display("-----------------------------",);
	
	cnt = cnt + 1;
	 
end 

endmodule 