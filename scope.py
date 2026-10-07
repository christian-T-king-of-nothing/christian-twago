global_var = 10

def print_global():
   global_var = global_var

   
   print(global_var)

   print_global(global_var)
