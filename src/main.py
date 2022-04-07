from tkinter import *
from tkinter import ttk
import os
from PIL import ImageTk,Image

#########################################################################################

root = Tk()
root.title("Systolic Array Simulator")

#########################################################################################
my_tabs = ttk.Notebook(root)
tab1 = ttk.Frame(my_tabs)

my_tabs.add(tab1, text ='write matrix1 and matrix2 content') # adding tab

my_tabs.pack(expand = 1, fill ="both")
#########################################################################################
code_frame1 = LabelFrame(tab1, text="Matrix1",padx=5,pady=5)
code_frame1.grid(row=0,column=0,padx=10,pady=10)
code_text1 = Text(code_frame1,height = 10,width = 20,bg="blue",fg="white",font="Helvetica 11 bold")
code_text1.pack()
#########################################################################################
code_frame2 = LabelFrame(tab1, text="Matrix2",padx=5,pady=5)
code_frame2.grid(row=0,column=1,padx=10,pady=10)
code_text2 = Text(code_frame2,height = 10,width = 20,bg="blue",fg="white",font="Helvetica 11 bold")
code_text2.pack()
#########################################################################################
memory_frame = LabelFrame(tab1, text="Result",padx=5,pady=5)
memory_frame.grid(row=1,column=0,padx=10,pady=10)
visual_view = Text(memory_frame,height = 10,width = 20,bg="blue",fg="white",font="Helvetica 11 bold")
visual_view.grid(row=1,column=0)

visual_lbl = Label(tab1,text= "Simple Systolic Array \nMade by github.com/lrayan7", font="Helvetica 11 bold")

visual_lbl.grid(row=1,column=1)
#########################################################################################


def click():
    
    matrix1 = code_text1.get('1.0', 'end')
    matrix2 = code_text2.get('1.0', 'end')

    mat1_contents = matrix1.split()
    mat2_contents = matrix2.split()

    i=0
    mat1_row1 = [None] * 4
    mat1_row2 = [None] * 4
    mat1_row3 = [None] * 4
    mat1_row4 = [None] * 4

    mat2_row1 = [None] * 4
    mat2_row2 = [None] * 4
    mat2_row3 = [None] * 4
    mat2_row4 = [None] * 4

    for c in mat1_contents :

        if(i<4) : 
            mat1_row1[i] = c
            i = i + 1
        elif(4<=i<8) :
            mat1_row2[i-4] = c
            i = i + 1
        elif(8<=i<12) :
            mat1_row3[i-8] = c
            i = i + 1
        elif(12<=i<16) :
            mat1_row4[i-12] = c
            i = i + 1
    i=0 

    for c in mat2_contents :

        if(i<4) : 
            mat2_row1[i] = c
            i = i + 1
        elif(4<=i<8) :
            mat2_row2[i-4] = c
            i = i + 1
        elif(8<=i<12) :
            mat2_row3[i-8] = c
            i = i + 1
        elif(12<=i<16) :
            mat2_row4[i-12] = c
            i = i + 1

    # print(mat1_row1[0],mat1_row1[1],mat1_row1[2],mat1_row1[3])
    # open(Filename, 'r', encoding='utf-8')
    
    tmpfile = open("automated_top_level.sv", "w+")
    
    tmpfile.write('`include "clock.sv"\n'+
    '`include "mac_cell.sv"\n' +


    'module tb_mac;\n' +

    'wire clk;\n' +
    'clock CLOCK(.clk_out(clk));\n' +

    'reg [7:0] C [15:0];\n' +
    'wire [7:0] C_wire [15:0];\n' +
    'reg [7:0] A [3:0];\n' +
    'reg [7:0] B [3:0];\n' +

    'wire [7:0] a_out_t [15:0];\n' +
    'wire [7:0] b_out_t [15:0];\n' +

    'integer j;\n' +
    'reg [14:0] cnt; // sizeof(vec1) + sizeof(vec2) - 1\n' +
    '// reg [7:0] result [7:0];\n' +

    'initial\n' +
    'begin \n' +

    # '    $dumpfile("tb_mac.vcd");\n' +
    # '    $dumpvars(0,tb_mac);\n' +

    '    cnt = 0;\n' +

    '    for (j=1; j<4; j=j+1) begin\n' +
    '        A[j] = 0;\n' +
    '        B[j] = 0;\n' +
    '    end\n')

    # mat2 = open("mat2", "w+")
    cnt = 0

    while True :
        
        if (cnt==0) :
            tmpfile.write("A[" + str(cnt) + "]=" + mat1_row1[3] +";\n")
            tmpfile.write("B[" + str(cnt) + "]=" +mat2_row1[3]+" ;#10;\n");
        if (cnt==1) :
        
            tmpfile.write("A[" + str(cnt-1) + "]=" + mat1_row1[2]+";\n")
            tmpfile.write("A[" + str(cnt) + "]=" + mat1_row2[3]+";\n")

            tmpfile.write("B[" + str(cnt-1) + "]=" + mat2_row1[2]+";\n")
            tmpfile.write("B[" + str(cnt) + "]=" + mat2_row2[3]+";#10;\n")
   
        if (cnt==2) :

            tmpfile.write("A[" + str(cnt-2) + "]=" + mat1_row1[1] + ";\n")
            tmpfile.write("A[" + str(cnt-1) + "]=" + mat1_row2[2] + ";\n")
            tmpfile.write("A[" + str(cnt) + "]=" + mat1_row3[3] + ";\n")

            tmpfile.write("B[" + str(cnt-2) + "]=" + mat2_row1[1] + ";\n")
            tmpfile.write("B[" + str(cnt-1) + "]=" + mat2_row2[2] + ";\n")
            tmpfile.write("B[" + str(cnt) + "]=" + mat2_row3[3] + ";#10;\n")
  
        if (cnt==3) : 

            tmpfile.write("A[" + str(cnt-3) + "]=" + mat1_row1[0] + ";\n")
            tmpfile.write("A[" + str(cnt-2) + "]=" + mat1_row2[1] + ";\n")
            tmpfile.write("A[" + str(cnt-1) + "]=" + mat1_row3[2] + ";\n")
            tmpfile.write("A[" + str(cnt) + "]=" + mat1_row4[3] + ";\n")

            tmpfile.write("B[" + str(cnt-3) + "]=" + mat2_row1[0] + ";\n")
            tmpfile.write("B[" + str(cnt-2) + "]=" + mat2_row2[1] + ";\n")
            tmpfile.write("B[" + str(cnt-1) + "]=" + mat2_row3[2] + ";\n")
            tmpfile.write("B[" + str(cnt) + "]=" + mat2_row4[3] + ";#10;\n")

        if (cnt==4) :

            tmpfile.write( "A[0]=0 ;\n");
            tmpfile.write("A[" + str(cnt-3) + "]=" + mat1_row2[0] + ";\n")
            tmpfile.write("A[" + str(cnt-2) + "]=" + mat1_row3[1] + ";\n")
            tmpfile.write("A[" + str(cnt-1) + "]=" + mat1_row4[2] + ";\n")


            tmpfile.write( "B[0]=0 ;\n");
            tmpfile.write("B[" + str(cnt-3) + "]=" + mat2_row2[0] + ";\n")
            tmpfile.write("B[" + str(cnt-2) + "]=" + mat2_row3[1] + ";\n")
            tmpfile.write("B[" + str(cnt-1) + "]=" + mat2_row4[2] + ";#10;\n")

        if (cnt==5) :

            tmpfile.write( "A[0]=0 ;\n");
            tmpfile.write( "A[1]=0 ;\n");
            tmpfile.write("A[" + str(cnt-3) + "]=" + mat1_row3[0] + ";\n")
            tmpfile.write("A[" + str(cnt-2) + "]=" + mat1_row4[1] + ";\n")

            tmpfile.write( "B[0]=0 ;\n");
            tmpfile.write( "B[1]=0 ;\n");
            tmpfile.write("B[" + str(cnt-3) + "]=" + mat2_row3[0] + ";\n")
            tmpfile.write("B[" + str(cnt-2) + "]=" + mat2_row4[1] + ";#10;\n")

        if (cnt==6) :

            tmpfile.write( "A[0]=0 ;\n");
            tmpfile.write( "A[1]=0 ;\n");
            tmpfile.write( "A[2]=0 ;\n");
            tmpfile.write("A[" + str(cnt-3) + "]=" + mat1_row4[0] + ";\n")

            tmpfile.write( "B[0]=0 ;\n");
            tmpfile.write( "B[1]=0 ;\n");
            tmpfile.write( "B[2]=0 ;\n");
            tmpfile.write("B[" + str(cnt-3) + "]=" + mat2_row4[0] + ";#10;\n")

        cnt = cnt + 1
        if (cnt == 7) :
            tmpfile.write( "A[3]=0 ;\n");
            tmpfile.write( "B[3]=0 ;\n");
            break
    
    tmpfile.write(
        '#500\n'+
    '$finish;\n'+

    'end \n'+


    'mac_cell cell_00( // LEFT MOST CELL\n'+
    '    .a_in(A[0]),\n'+
    '    .b_in(B[0]),\n'+
    '    .clk(clk),\n'+
    '    .c(C_wire[0]),\n'+
    '    \n'+
    '    .a_out(a_out_t[0]),\n'+
    '    .b_out(b_out_t[0])\n'+
    '    );\n'+
    '    \n'+
    'mac_cell cell_10( // LEFT MOST CELL\n'+
    '    .a_in(A[1]),\n'+
    '    .b_in(b_out_t[0]),\n'+
    '    .clk(clk),\n'+
    '    .c(C_wire[4]),\n'+
    ' \n'+
    '    .a_out(a_out_t[4]),\n'+
    '    .b_out(b_out_t[4])\n'+
    '    );\n'+
    ' \n'+
    'mac_cell cell_20( // LEFT MOST CELL\n'+
    '    .a_in(A[2]),\n'+
    '    .b_in(b_out_t[4]),\n'+
    '    .clk(clk),\n'+
    '    .c(C_wire[8]),\n'+
    ' \n'+
    '    .a_out(a_out_t[8]),\n'+
    '    .b_out(b_out_t[8])\n'+
    '    );\n'+
    ' \n'+
    'mac_cell cell_30( // LEFT MOST CELL\n'+
    '    .a_in(A[3]),\n'+
    '    .b_in(b_out_t[8]),\n'+
    '    .clk(clk),\n'+
    '    .c(C_wire[12]),\n'+
    ' \n'+
    '    .a_out(a_out_t[12]),\n'+
    '    .b_out(b_out_t[12])\n'+
    '    );\n'+
    ' \n'+
    'genvar i;\n'+
    'generate\n'+
    '    for (i=1; i<4; i=i+1) begin\n'+
    '        mac_cell cells(\n'+
    '            .a_in(a_out_t[i-1]),\n'+
    '            .b_in(B[i]),\n'+
    '            .clk(clk),\n'+
    '            .c(C_wire[i]),\n'+
    ' \n'+
    '            .a_out(a_out_t[i]),\n'+
    '            .b_out(b_out_t[i])\n'+
    '            );\n'+
    '    end\n'+
    'endgenerate\n'+
    'generate\n'+
    '    for (i=5; i<8; i=i+1) begin\n'+
    '        mac_cell cells(\n'+
    '            .a_in(a_out_t[i-1]),\n'+
    '            .b_in(b_out_t[i-4]),\n'+
    '            .clk(clk),\n'+
    '            .c(C_wire[i]),\n'+
    ' \n'+
    '            .a_out(a_out_t[i]),\n'+
    '            .b_out(b_out_t[i])\n'+
    '            );\n'+
    '    end\n'+
    'endgenerate\n'+
    'generate\n'+
    '    for (i=9; i<12; i=i+1) begin\n'+
    '        mac_cell cells(\n'+
    '            .a_in(a_out_t[i-1]),\n'+
    '            .b_in(b_out_t[i-4]),\n'+
    '            .clk(clk),\n'+
    '            .c(C_wire[i]),\n'+
    ' \n'+
    '            .a_out(a_out_t[i]),\n'+
    '            .b_out(b_out_t[i])\n'+
    '            );\n'+
    '    end\n'+
    'endgenerate\n'+
    'generate\n'+
    '    for (i=13; i<16; i=i+1) begin\n'+
    '        mac_cell cells(\n'+
    '            .a_in(a_out_t[i-1]),\n'+
    '            .b_in(b_out_t[i-4]),\n'+
    '            .clk(clk),\n'+
    '            .c(C_wire[i]),\n'+
    ' \n'+
    '            .a_out(a_out_t[i]),\n'+
    '            .b_out(b_out_t[i])\n'+
    '            );\n'+
    '    end\n'+
    'endgenerate\n'+
    ' \n'+
    'integer k;\n'+
    'always @(posedge clk)\n'+
    'begin \n'+
    '    for(k=0;k<16;k++) begin\n'+
    '        C[k] = C_wire[k];\n'+
    '    end \n'+
    ' \n'+
    '    for (j=0; j<4; j=j+1) begin \n'+
    '        $display(\n'+
    '            "[%d]",C[4*j+0],"[%d]",C[4*j+ 1],"[%d]",C[4*j+ 2],"[%d]",C[4*j+ 3]\n'+
    '            );\n'+
    '    end\n'+
    '    $display("-----------------------------",);\n'+
    '    \n'+
    '    cnt = cnt + 1;\n'+
    '     \n'+
    'end \n'+

    'endmodule \n'
        )
    tmpfile.close()
    
    os.system("iverilog -o systolic_array automated_top_level.sv");
    os.system("vvp systolic_array > result_file");
    
    with open("result_file" , 'r') as f:
        visual_view.insert(INSERT, f.read())
    f.close()
    
    


b = Button(tab1, text="RUN    ",command=click )
b.grid(row=2,column=0)
#########################################################################################

# console_tab = ttk.Notebook(root)
# tab3 = ttk.Frame(console_tab)
# tab4 = ttk.Frame(console_tab)
# console_tab.add(tab3, text ='console') # adding tab
# console_tab.add(tab4, text ='console2') # adding tab
# console_tab.pack(expand = 1, fill ="both")

root.mainloop()
