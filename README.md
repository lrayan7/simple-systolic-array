# simple-systolic-array

simple systolic array made for 4x4 matrix multiplication
made in verilog using IcarusVerilog.

guide:
write matrices in 'mat1' and 'mat2' file respectively in the format they initially are (for example open 'mat1' and see format) 
  where there is 'space' between each number.
run ./mat_calc - this just performs the multiplication and saves result in 'tmpfile' file.
run /.verilog_implant which will output 'tb_mac3.sv' that has the result matrix loaded in verilog code.
run 'iverilog -o sys_array tb_mac3.sv'
run 'vvp sys_array'
last matrix result is the answer - (runs more time than needed i know...you can change the runtime in 'tb_mac.sv' where $finish 
   change #500 to desired time)

