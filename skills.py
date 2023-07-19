import csv

# KEY for skill names
legend = {"V": "Vocabulary", "A": "Word Agreement", "S": "Spelling", "Gen": "Gender", "Per": "Persons", "G": "Grammar", "T": "Tenses", "Past": "Past Tenses", "Fut": "Future Tenses", "M": "Modes", "Sub": "Subjunctive Mode", "Hyp": "Hypothetical Mode", "Pro": "Professional Communication", "Pron": "Pronouns", "Prep": "Prepositions"}
# contains total mistakes made by students && skill_weights.values() is the vector
student_mistakes = {"V": 0, "A": 0, "S": 0, "Gen": 0, "Per": 0, "G": 0, "T": 0, "Past": 0, "Fut": 0, "M": 0, "Sub": 0, "Hyp": 0, "Pro": 0, "Pron": 0, "Prep": 0}
skill_weights = {"V": 0, "A": 0, "S": 0, "Gen": 0, "Per": 0, "G": 0, "T": 0, "Past": 0, "Fut": 0, "M": 0, "Sub": 0, "Hyp": 0, "Pro": 0, "Pron": 0, "Prep": 0}
# weights for calculating student vector
mistake_per_skill = [4, 1, 4, 2, 2, 11, 7, 3, 2, 3, 1, 1, 4, 2, 1]
#weight_by_test = [0.2, 0.05, 0.2, 0.1, 0.1, 0.55, 0.35, 0.15, 0.1, 0.15, 0.05, 0.05, 0.2, 0.1, 0.05]
# is the "ideal" exercise set based on mistakes made by student
ideal_set = []

exercises = []


def get_data(filepath):
    '''
    reads data from csv files
    '''

    txt_file = open(filepath, "r")

    results = list(csv.reader(txt_file, delimiter = ","))
    for i in range(20):     #there are 20 questions, so we will count it manually
        if (results[i][0] == '2'): continue         #skip questions with full marks

        skill_list = results[i][1].split(",")       #get all skills

        if (results[i][0] == '1'):                  #if 1 then first skill mastered, skip and get the rest
            skill_list.remove(skill_list[0])

        for skill in skill_list:                    #add 1 to all skills
            student_mistakes[skill] += 1

    i = 0
    for key,value in student_mistakes.items():
        skill_weights[key] = (value/mistake_per_skill[i])
        if (skill_weights[key] >= 0.1): ideal_set.append(1)
        else: ideal_set.append(0)
        i+=1
    
    txt_file.close()

    with open("data_files\exercises.csv", newline='') as csvfile:
          reader = csv.reader(csvfile, delimiter=',', quotechar='|')
          j = 0
          for row in reader:
            exercises.append([])
            for item in row:
                exercises[j].append(int(item))
            j+=1

    return results


def matching_skills(ideal, exercise):
    '''
    Computes how close an exercise is to all the areas that need practice
    '''
    total_matches = 0
    for i in range(len(ideal)):
        if ideal[i] == 1 and ideal[i]-exercise[i] == 0:
            total_matches += 1
    return total_matches


def best_match(ideal):
    '''
    Finds exercise that best match the skills that need practice
    '''
    matched = {}
    index = 0
    for exercise in exercises:
        matched[index] = matching_skills(ideal, exercise)
        index+=1
    
    exercise_list = {}
    the_one = [key for key, value in matched.items() if value == max(matched.values())]
    exercise_list[the_one[0]] = exercises[the_one[0]]
    matched.pop(the_one[0])
    the_one = [key for key, value in matched.items() if value == max(matched.values())]
    exercise_list[the_one[0]] = exercises[the_one[0]]
    matched.pop(the_one[0])
    the_one = [key for key, value in matched.items() if value == max(matched.values())]
    exercise_list[the_one[0]] = exercises[the_one[0]]

    return exercise_list

def recommendation_string(dict_exercises):
    '''
    Formatted output for skill recommendations
    '''
    text = "You should focus on: \n"
    skill_dict = {k: v for k, v in sorted(skill_weights.items(), key = lambda item: item[1])}
    skills_to_practice = [key for key, value in skill_dict.items() if value >= 0.7]
    if len(skills_to_practice) == 0:
        skills_to_practice = [key for key, value in skill_dict.items() if value >= 0.4]
        if len(skills_to_practice) == 0: 
            skills_to_practice = [key for key, value in skill_dict.items() if value > 0]
            if len(skills_to_practice) == 0:
                return "You got 100% in this test keep up the good work"
    for i in skills_to_practice:
        text += "{} \n".format(legend[i])
    text += "Based on that we recommend the following practice sets: \n"
    for key,value in dict_exercises.items():
        i = 0
        text += "Exercise set {}: focuses on ".format(key+1)
        for skill in legend.values():
            if value[i] == 1:
                text += "{}, ".format(skill)
            i+=1
        text = text[:len(text)-2]
        text += "\n"

    text = text[:len(text)-2]
    return text


#Suchanya Limpakom
#Olga Manakina