

import random
import time 

# **************************** Target ***************************************
answer_model = [(1,5) , (2,6) , (3,4) , (1,1) , (0,5) , (1,1) ,(0,2) ,(0,13)]
# ***************************************************************************

POPULATION_SIZE = 100

def check(model):

    for data in model:

        if model.count(data) > 0:

            return False

    return True

class Gentic:


    @staticmethod
    def cunvented(best_population):

        model = []

        model1 = random.choice(best_population)["Models"]

        model2 = random.choice(best_population)["Models"]

        
        while len(model) != len(answer_model):

            random_ = random.random()

            if random_< 0.45:

                
                
                genome = random.choice(model1)

            elif random_ <= 0.90:

            
                genome = random.choice(model2)
 

            else:

                genome = Gentic.mutation()

            if model.count(genome) == 0:

                model.append(genome)


        return {"Models":model , "fitness":Gentic.fitness(model)}

    @staticmethod
    def fitness(model):

        answer_model_test = answer_model

        fitness = 0

        for x_y in model:

            if answer_model_test.count(x_y) == 0:

                fitness+=1

            elif answer_model_test.count(x_y) > 1:
                
                answer_model_test.remove(x_y)

        return fitness
    
    @staticmethod
    def mutation():


        x  = random.randint(0,15)
        y = random.randint(0,15)

        return (x,y)

    @staticmethod
    def generate_population(population_size):

        population = []

        for _ in range(population_size):

            model = []

            for _ in range(len(answer_model)):

                model.append(Gentic.mutation())

            fitness = Gentic.fitness(model)

            population.append({"Models":model , "fitness":fitness})
    
        return population
                




if __name__ == "__main__":

    population = Gentic.generate_population(POPULATION_SIZE)

    
    best = ""
    finish = False

    while finish == False:

        population=  sorted(population , key=lambda x: x["fitness"])
        
        print(population[0])

        if population[0]["fitness"] == 0:    
            

            print("Target: " , population[0]["Models"])

            finish == True

            break
        
        new_population = []

        last_population_count = (POPULATION_SIZE * 95) // 100

        best_population = population[0:last_population_count]

        while len(new_population) != (POPULATION_SIZE  * 95) // 100:  

            new_population.append(Gentic.cunvented(best_population))

        population= []
        population = new_population + best_population

        
        time.sleep(1.5)


            

