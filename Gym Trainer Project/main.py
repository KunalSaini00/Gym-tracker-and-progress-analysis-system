from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt

CALORIE_GOAL_LIMIT= 3000 #kcal
PROTEIN_GOAL= 180 #grams
FAT_GOAL= 80 #grams
CARBS_GOAL= 300 #grams

protein_sum=0
fats_sum=0
carbs_sum=0

todayFood = []
todayExercise = []
todayCalories=[]
Calories=0
TotalExercisesSum=0

@dataclass
class Food:
    name: str
    protein : int
    fat: int
    carbs: int
@dataclass  
class Exercises:
    pushups: int
    pullups: int
    deadlifts : int
    squat: int
    plank: int
    
done = False

while not done:
    print("""
    (1) Add a new food
    (2) Exercises
    (3) Visualize progress 
    (4) EXIT   
          """)
    
    choice = input("choose an option  ")
    
    if choice == "1":
        if Calories < CALORIE_GOAL_LIMIT:
          print("Adding a new food!")
          name=input("Name: ")
          protein= int(input("Protein: "))
          fat=int(input("Fat: "))
          carbs= int(input("Carbs: "))
          food=Food(name,protein,fat,carbs)
          todayFood.append(food)
          print("Successfully added!")
          protein_sum=protein_sum+protein
          fats_sum=fats_sum + fat
          carbs_sum= carbs_sum + carbs
          
          Calories=protein_sum + fats_sum + carbs_sum
          todayCal={"Cal":Calories}
          todayCalories.append(todayCal)
          
        else:
            print("Today's Calories Limit Reached")

    elif choice == "2":
        print("Adding Exercises")
        pushups=int(input("Pushups: "))
        pullups=int(input("Pullups: "))
        deadlifts= int(input("Deadlifts "))
        squat=int(input("squat: "))
        plank= int(input("plank "))
        exercises= Exercises(pushups,pullups,deadlifts,squat,plank)
        todayExercise.append(exercises)
        print("Successfully added!")
        
    
    
    elif choice == "3":
        #Food sum
        
        
        
        #Exercises sum
        
        pushups_sum=sum(exercises.pushups for exercises in todayExercise)
        pullups_sum=sum(exercises.pullups for exercises in todayExercise)
        deadlifts_sum=sum(exercises.deadlifts for exercises in todayExercise)
        squat_sum=sum(exercises.squat for exercises in todayExercise)
        plank_sum=sum(exercises.plank for exercises in todayExercise)
        
        if TotalExercisesSum < Calories:
          TotalExercisesSum= pushups_sum+pullups_sum+deadlifts_sum+squat_sum+plank_sum
        
        if TotalExercisesSum < Calories:
          fig, axs =plt.subplots(2,2)
          axs[0, 0].pie([protein_sum, fats_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"], autopct="%1.1f%%")
          axs[0, 0].set_title("Macronutrients Distribution")
          axs[0, 1].bar([0, 1, 2], [protein_sum,fats_sum,carbs_sum], width=0.4)
          axs[0, 1].bar([0.5, 1.5, 2.5], [PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL], width=0.4)
          axs[0, 1].set_title("Macronutrients Progress")
          axs[1, 0].pie([Calories, Calories - TotalExercisesSum], labels=["Calories Used","Remaining"], autopct="%1.1f%%")
          axs[1, 0].set_title("Calories Goal Progress")
          axs[1, 1].plot(list(range(len(todayFood))), np.cumsum([todayCal["Cal"] for todayCal in todayCalories ]), label="Calories Eaten")
          axs[1, 1].plot(list(range(len(todayFood))), [CALORIE_GOAL_LIMIT] * len(todayFood), label="Calorie Goal" )
          axs[1, 1].legend()
          axs[1, 1].set_title("Calories Goal Over Time")
        
        
          fig.tight_layout()
          plt.show()
          
        else:
              print("Calories is insufficient, eat more then do exercises")
        
    elif choice == "4":
        done = True
        
    else:
        print("Invalid Choice!")