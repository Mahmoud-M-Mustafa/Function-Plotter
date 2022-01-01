import re
class Poly_interpreter:
    def __init__(self) -> None:
        pass
    @classmethod
    def _coeffs(self,input):
        """
        paramater: a list of arithmatic terms
        returns a dictionary {keys--> power  values--> coeffs}
        """

        poly_dict={}
        track=[]
        key_tmp=None
        for itm in input:
            if re.fullmatch(r"-?\d+",itm):
                if '0' in track:
                    poly_dict['0']+=int(itm)
                else:
                    poly_dict['0']=int(itm)
                    track.append('0')
            elif re.fullmatch(r"x",itm):
                if '1' in track:
                    poly_dict['1']+=1
                else:
                    poly_dict['1']=1
                    track.append('1')

            elif re.fullmatch(r"-x",itm):
                if '1' in track:
                    poly_dict['1']-=1
                else:
                    poly_dict['1']=-1
                    track.append('1')

            elif re.fullmatch(r"x\^-?\d+",itm):
                key_tmp= itm[self.extract_power(itm):]
                if key_tmp in track:
                    poly_dict[key_tmp]+=1
                else:
                    poly_dict[key_tmp]=1
                    track.append(key_tmp)

            elif re.fullmatch(r"(-?\d+)[/*]x",itm):
                if '*' in itm:
                    if '1' in track:
                        poly_dict['1']+=int(itm[:self.extract_number(itm)])
                    else:
                        poly_dict['1']=int(itm[:self.extract_number(itm)])
                        track.append('1')
                else:
                    if '-1' in track:
                        poly_dict['-1']+=int(itm[:self.extract_number(itm)])
                    else:
                        poly_dict['-1']=int(itm[:self.extract_number(itm)])
                        track.append('-1')               

            else:
                key_tmp= itm[self.extract_power(itm):]
                if '*' in itm:
                    if key_tmp in track:
                        poly_dict[key_tmp]+=int(itm[:self.extract_number(itm)])
                    else:
                        poly_dict[key_tmp]=int(itm[:self.extract_number(itm)])
                        track.append(key_tmp)
                else:
                    if '-'+key_tmp in track:
                        poly_dict['-'+key_tmp]+=int(itm[:self.extract_number(itm)])
                    else:
                        poly_dict['-'+key_tmp]=int(itm[:self.extract_number(itm)])
                        track.append('-'+key_tmp)                    

        return poly_dict
    

    def extract_number(input):
        """
        returns the index of last digit of coeff
        """
        idx=0

        for i in range(0,len(input)):
            if input[i] in ['*','/']:
                idx=i

        return idx

    def extract_power(input):
        """
        returns the index of first digit in power
        """
        idx=0

        for i in range(0,len(input)):
            if input[i] =='^':
                idx=i

        return idx+1



