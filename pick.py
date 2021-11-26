import numpy as np

global reg,memory
reg = np.zeros((16), dtype = np.uint8)
memory = np.zeros((16), dtype = np.uint8)
rows = 45
columns = 2
values = rows * columns
matrix = np.zeros((rows,columns), dtype = np.uint8)

def run_program(num_bytes):
  pc = 0
  sb = np.uint8
  fb = np.uint8
  m = np.uint8
  counter = np.uint8
  counter = (num_bytes/2)   #8
  print('counter onemli...',counter)
  print('PC denetiminzdeyiz..ZOR..',pc)
      
  while( pc < counter ):     # burası önemli...
      pc = pc + 1
      if pc == counter:
            break      
      print('PC denetimindeyiz....',pc)
      fb = matrix[pc,0]
      sb = matrix[pc,1]
      
      
      print('sb tur', sb)
      print('fb turlar...',fb)
      m = fb >> 4
    #  print('shiftlenmis hal...',m)
      
      if m == 0:                    # MOV Rn, direct
        reg[fb & 0x0f] = memory[sb]
        print("bu reg sıfır...",reg[0])
    #    print('sifir no' )  
      elif m == 1:                 # MOV direct, Rn
        memory[sb] = reg[fb & 0x0f]
    #    print('bir no')
      elif m == 2:                  #  MOV @Rn, Rm
        memory[reg[fb & 0x0f]]
        print('iki no')
      elif m == 3:                  # MOV Rn, #immed.
        reg[fb & 0x0f] = sb 
        # print("bu reg sifire gelecek second byte...",reg[0])
        # print("bu reg birrrrrrrr...",reg[1])
        # print("bu reg ikiiiiii...",reg[2])
        # print("bu reg uuuccccc...",reg[3])
        # print('uc no lu elifffff......')
      elif m == 4:                 # ADD Rn, Rm
        reg[fb & 0x0f] += reg[sb >> 4]
        print('dort no') 
      elif m == 5:                # SUB Rn, Rm
        reg[fb & 0x0f] -= reg[sb >> 4]
        print('bes no')          
      elif m == 6:               #  JZ Rn, relative
        pc = pc + sb  
        print('alti no') 
      else:
        print('wrong choice...')    

  return      
            

def  print_memory_contents():
      print("Printing memory")
      for i in range(0,16,1):
        print("Memory Address...",i,"Value...",memory[i])

def print_register_contents():
      print("Printing registers")
      for i in range(0,16,1):
        print("R [%d] : %d"%(i,reg[i]))
        
with open('tests.bin','rb') as file:
        # read HEX value 
  for x in range(0,rows,1):
    for y in range(0,columns,1):
       byte = file.read(2)        
       result_int = int(byte)
       matrix[x,y] = result_int
    
file.close()
print(matrix)

run_program(values)
print_memory_contents()
print_register_contents() 