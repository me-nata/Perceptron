from random import uniform
from data_base import DataBase

class PerceptronNetwork:
    @staticmethod
    def activation_function(x):
        return 0 if x <= 0 else 1


    def __init__(self, qtd_entradas:int, ta:float=0.3, max_epochs=-1) -> None:
        self.W = [uniform(-1, 1) for _ in range(qtd_entradas)]
        self.result = -1
        self.error = 1
        self.total_error = 1
        self.ta = ta
        self.max_epochs=max_epochs
        self.bias = uniform(-1, 1)


    def receiver_inputs(self, E):
        for i in range(len(E)):
            print(E[i], end='|')
            self.result += E[i]*self.W[i]

        self.result += self.bias
        self.result = PerceptronNetwork.activation_function(self.result)


    def update_error(self, expected_value:float):
        self.error = expected_value - self.result


    def update_weight(self, E):
        for i in range(len(E)):
            self.W[i] = self.W[i] + self.error*self.ta*E[i]
        
        self.bias = self.bias + self.ta*self.error 


    def process(self, E:list, expected_value:int):
        self.receiver_inputs(E)
        self.update_error(expected_value)
        self.update_weight(E)
        print(self.result if self.error == 0 else 
        f'{self.result} ERROR expected({expected_value}); New Weight: {list(round(w, 3) for w in self.W)}')


    def pick_db(self, db):
        epoch = 0
        
        print(f'Initial Weight: {list(round(w, 3) for w in self.W)}')
        
        while(self.total_error != 0):
            self.total_error = 0
            print(f'\n====epoch: {epoch}====')
            print(f'bias: {self.bias}')
            for instancia in db:
                perceptron.process([value for value in instancia[:-1]], instancia[-1])        
                self.total_error += abs(self.error)

            if self.max_epochs != -1:
                if epoch >= self.max_epochs:
                    break

            epoch+=1
            
        print('Finish')


db_or  = DataBase.generate(3, 'or')
db_and = DataBase.generate(3, 'and')
db_xor = DataBase.generate(3, 'xor')

perceptron = PerceptronNetwork(qtd_entradas=3, ta=0.3, max_epochs=1000)

perceptron.pick_db(db_xor)