class DataBase:
    @staticmethod
    def _expacted_value(instance, op):
        result = instance[0]
        for v in instance[1:]:
            result = op(result, v)
        
        instance.append(result)


    @staticmethod
    def _generate_prox_inst(current_i, size):
        next_inst = list(int(x) for x in list(bin(current_i))[2:])
        return list(0 for _ in range(size - len(next_inst))) + next_inst 


    @staticmethod 
    def map_operation(type_op):
        op = lambda x, y: x|y
        if type_op == 'and':
            op = lambda x, y: x&y
        elif type_op == 'xor':
            op = lambda x, y: x^y

        return op

    @staticmethod
    def generate(size=2, type_operation='or'):
        op = DataBase.map_operation(type_operation)
        output = []
        for i in range(2**size):
            output.append(DataBase._generate_prox_inst(i, size))
            DataBase._expacted_value(output[i], op)
        
        return output