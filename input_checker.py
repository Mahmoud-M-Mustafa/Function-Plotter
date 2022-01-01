import re
from input_interpreter import Poly_interpreter
class Validator:
    

    term="((-?\d+[*/])?x(\^-?\d)?|-?\d+)"
    pattern= re.compile(f"{term}([+-]{term})*")

    def __init__(self):
        pass
    def inp_x(self,input):
        """
            checks if input is a valid integer or not
        """
        try:
            float(input)
            return True
        except:
            return False

    
    def function_check(self,input):
        """
        checks the validity of the input using regular expressions
        """
        polynomial=input.replace(" ","")
        polys=[]
        if re.fullmatch(self.pattern,polynomial):
            for x in re.finditer(self.term,polynomial):
                polys.append(polynomial[x.start():x.end()])
            return Poly_interpreter._coeffs(polys)
    
        return

        


