import time 
import client
import matrix_generator


tests = [[200,200], [200,500], [1000,1000], [500,1000], [1000,5000]]

f = open("results.txt", "w")

for i in range(5):
    matrix_generator.run_gen(tests[i][0], tests[i][1], "A.dat", "X.dat")  
    start = time.time()
    client.run_client()
    stop = time.time()
    f.write(f"{tests[i][0]}x{tests[i][1]}: {stop-start}\n")
    
    
f.close()
    
    
