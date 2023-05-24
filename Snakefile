rule count:
    input:
        input1 = "coursesTaken-A.csv",
        input2 = "coursesTaken-B.csv"
    output:
        output1 = "coursesTaken-A.count",
        output2 = "coursesTaken-B.count"
    shell:
        "python3 count.py {input.input1} {output.output1};python3 		count.py {input.input2} {output.output2}"
        
