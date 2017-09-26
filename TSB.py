import os
from pathlib import Path

class Tool_System_Builder:
    
    def __init__(self):
        self.func_defs = self.get_func_defs()
        self.functions = self.list_funcs()
        self.ult_defs = self.list_defs()
        self.dict_func_defs = self.get_dict_func_defs()
        
    def __repr__(self):
        
        # incomplete repr
        
        s = ''
        s += 'A toolbuilding system with the following tool functions: ' + '\n'
        for x in self.functions:
            s += x
        return s
    
##    methods for obtaining system info from user

    def get_func_def(self):
        func = str(input('Enter function (tool) name: '))
        definition = str(input('Define function: '))
        func_def = [func, definition]
        return func_def

    def recheck_yn_input(self, cont):
        enter_another_func_prompt = 'Would you like to enter another tool function? (y/n)'
        print('Please answer y or n')
        cont = str(input(enter_another_func_prompt))
        if cont not in 'yn':
            restart = self.recheck_yn_input(cont)
            return restart
        return cont

    def get_func_defs(self):
        """ gets a list of list pairs, of tool functions and their definitions.
        """
        enter_another_func_prompt = 'Would you like to enter another tool function? (y/n)'
        func_defs = []
        func_defs += [self.get_func_def()]
        
        cont = str(input(enter_another_func_prompt))
        if cont not in'yn':
            cont = self.recheck_yn_input(cont)
        while cont in 'yn':
            if cont == 'y':
                func_defs += [self.get_func_def()]
                cont = str(input(enter_another_func_prompt))
            elif cont == 'n':
                break
        
        return func_defs

##    methods and functions for manipulating input from user to prepare the creation of the toolbuilding system
    
    def list_funcs(self):
        func_list = []
        for func_def in self.func_defs:
            func_list += [func_def[0]]
        return func_list

    def list_defs(self):
        def_list = []
        for func_def in self.func_defs:
            def_list += [func_def[1]]
        return def_list
        
        
    def get_dict_func_defs(self):
        """ obtains the user's functions and definitions, storing them in a dictionary
        """

        dict_func_defs = {}
        
        for func_def in self.func_defs:
            dict_func_defs[func_def[0]] = func_def[1]

        return dict_func_defs

    def recommend(self, rec, this_ts_dir):
        rec_file = open(this_ts_dir + '_recommendations.txt', 'a') 
        s = 'The following function sequences may be interesting starting points: \n\n'
        for combo in rec:
            s += (combo + '\n\n')
        rec_file.write(s)
        rec_file.close

##    def categorize(self, self.functions):
##        s = 'Do any of your functions fit into a group or category? (y/n)'
##        cat_funcs = []
##        
##        cont = str(input(s))
##        if cont not in'yn':
##            cont = self.recheck_yn_input(cont)
##        while cont in 'yn':
##            if cont == 'y':
##                s1 = 'Enter the functions, separated by commas: '
##                funcs_in_cat = str(input(s1))
##                s2 = 'Enter name of category: '
##                cat_name = str(input(s2))
##                [x.strip() for x in funcs_in_cat.split(',')]
##                
##                categorized += [self.get_func_def()]
##                cont = str(input(enter_another_func_prompt))
##            elif cont == 'n':
##                break
        

##    methods to create system of appropriate directories in user's computer

    def make_3l_system(self):
        functions = self.functions
        ult_defs = self.dict_func_defs
        work_defs = ult_defs

        # create folder for Tool Systems, and subfolder for this tool system:
        
        init_dir = os.getcwd()
        gen_ts_dir = 'Tool Systems'
        if not os.path.exists(gen_ts_dir):
            os.mkdir(gen_ts_dir)
            os.chdir(gen_ts_dir)
        else:
            os.chdir(gen_ts_dir)
            
        this_ts_dir = str(input('Give your new tool system a title:'))
        os.mkdir(this_ts_dir)
        os.chdir(this_ts_dir)
        ts_loc = init_dir + '/' + gen_ts_dir + '/' + this_ts_dir
        
        num = len(functions)
        of = ' of'
        nl = '\n'
        rec1 = []
    
        count_1 = 1     # set counter 1
        
        for i1 in range(num):
            
            # initialize/reset content

            s = ''
            d1 = ''
            d2 = ''
            d3 = ''
            
            # create level 1

            w1_count = '(' + str(count_1) + ') '
            count_1 += 1
            i1_name = functions[i1]
            i1_path = w1_count + i1_name
            os.mkdir(i1_path)
            os.chdir(i1_path)       
    
            # add level 1

            s += (i1_name + of + ' :' + nl + nl)
            desc1 = ult_defs[functions[i1]]
            d1 += i1_name + ' =' + nl + desc1 + nl + nl
            i1_filename = ' * ' + i1_name + '_index.txt'
            i1_file = open(i1_filename, 'w')
                   
            count_2 = 1     # reset counter 2
            
            for i2 in range(num):
                
                # create level 2

                w2_count = '(' + str(count_2) + ') '
                count_2 += 1
                i2_name = i1_name + of + ' ' + functions[i2]
                i2_path = w2_count + i2_name
                os.mkdir(i2_path)
                os.chdir(i2_path)
    
                # add level 2

                desc2 = work_defs[functions[i1]] + of + nl + ult_defs[functions[i2]]
                d2 += i2_name + ' =' + nl + desc2 + nl + nl
                i2_filename = ' * ' + i2_name + '_desc.txt'
                i2_file = open(i2_filename, 'w')
                i2_file.write(desc2)
                i2_file.close
    
                count_3 = 1     # reset counter 3
                
                for i3 in range(num):
                    
                    # create level 3

                    w3_count = '(' + str(count_3) + ') '
                    count_3 += 1
                    i3_name = i2_name + of + ' ' + functions[i3]
                    i3_path = w3_count + i3_name
                    os.mkdir(i3_path)
                    os.chdir(i3_path)                                 
    
                    # add level 3

                    s += i3_name + nl
                    desc3 = work_defs[functions[i1]] + of + nl + work_defs[functions[i2]] + of + nl + ult_defs[functions[i3]]
                    d3 += i3_name + ' =' + nl + desc3 + nl + nl
                    if functions[i1] != functions[i2] and functions[i1] != functions[i3] and functions[i2] != functions[i3]:
                        rec1 += [desc3]
                        
                    i3_filename = w3_count + i3_name + '_desc.txt' 
                    i3_file = open(i3_filename, 'w')
                    i3_file.write(desc3)
                    i3_file.close
                    os.chdir(ts_loc + '/' + i1_path + '/' + i2_path)
                    
                s += nl
                d3 += nl + '----------------------------------------' + nl
                os.chdir(ts_loc + '/' + i1_path)

            d2 += nl + '----------------------------------------' + nl           
            os.chdir(ts_loc)
            
            i0_file = open(this_ts_dir + '_index.txt', 'a')
            i0_file.write(s)
            i0_file.close       
    
            i1_file.write(s)
            i1_file.close
                
            d1_file = open(this_ts_dir + '_1lvl_descriptions.txt', 'a')
            d1_file.write(d1)
            d1_file.close
            
            d2_file = open(this_ts_dir + '_2lvl_descriptions.txt', 'a')
            d2_file.write(d2)
            d2_file.close
            
            d3_file = open(this_ts_dir + '_3lvl_descriptions.txt', 'a')
            d3_file.write(d3)
            d3_file.close

        self.recommend(rec1, this_ts_dir)
        os.chdir(init_dir)
        return ts_loc

