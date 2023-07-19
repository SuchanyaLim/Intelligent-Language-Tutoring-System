
#naive_bayes classifier
#global variables
#prior probabilities for getting below B, B or C
priors = [0.08, 0.67, 0.25]

#probabilities of a range of scores for each level
# 0-30, 31-40, 41-50, 51-60, 61-70, 71-80, 81-90, 91-100
#each tuple represents 1 range for 3 outcomes (below B, B, C)
densities = [(0,0,0),(0.2,0,0),(0.4,0,0),(0.4,0.1,0),(0,0.4,0),(0,0.4,0.3),(0,0.1,0.5),(0,0,0.2)]
outputs_bayes = ["You do not qualify for level B just yet. See details for recommendations: ",
           "You will most likely get the B Level.\n",
           "Congratulations! Looks like you can get the C Level!\n",
           "You can easily get 100% on Level C. Why do you even learn French?? No recommendations for you."]
extra_output_B_C = ["However your score is below mean for this level. See recommendations to improve your score:",
                "Your level is above mean for this level! Good job, but see recommendations to keep your score."]
means = [71.3, 86.4] #means for scores B and C


def naive_bayes_classifier(results):
    final_score = round(float(results[len(results) - 1][0]))
    # final_score = 80 - YOU CAN PLAY WITH DIFFERENT VALUES WITHOUT CHANGING THE INPUT FILE, JUST TO SEE DIFFERENT OUTPUTS
    p_score_given_level = []
    # print(type(final_score), final_score)
    j=0
    #counter for tuples' indices
    if final_score <= 30:
        p_below_B = densities[0][j]
        p_level_B = densities[0][j+1]
        p_level_C = densities[0][j+2]
    elif 31 <= final_score <= 40:
        p_below_B = densities[1][j]
        p_level_B = densities[1][j+1]
        p_level_C = densities[1][j+2]
    elif 41 <= final_score <= 50:
        p_below_B = densities[2][j]
        p_level_B = densities[2][j + 1]
        p_level_C = densities[2][j + 2]
    elif 51 <= final_score <= 60:
        p_below_B = densities[3][j]
        p_level_B = densities[3][j + 1]
        p_level_C = densities[3][j + 2]
    elif 61 <= final_score <= 70:
        # print("I am here")
        p_below_B = densities[4][j]
        p_level_B = densities[4][j + 1]
        p_level_C = densities[4][j + 2]
    elif 71 <= final_score <= 80:
        p_below_B = densities[5][j]
        p_level_B = densities[5][j + 1]
        p_level_C = densities[5][j + 2]
    elif 81 <= final_score <= 90:
        p_below_B = densities[6][j]
        p_level_B = densities[6][j + 1]
        p_level_C = densities[6][j + 2]
    elif 91 <= final_score <= 100:
        # print("I am here")
        p_below_B = densities[7][j]
        p_level_B = densities[7][j + 1]
        p_level_C = densities[7][j + 2]


    p_score_given_level.append(p_below_B*priors[0])
    p_score_given_level.append(p_level_B*priors[1])
    p_score_given_level.append(p_level_C*priors[2])
    max_p = max(p_score_given_level)
    # print("done computing", p_score_given_level)
    # print ("max is", max_p)
    if max_p==0:
        output = outputs_bayes[0]
    else:
        for i in range(3):
            if p_score_given_level[i] == max_p:
                output = outputs_bayes[i]

        if (output == outputs_bayes[1]):
            if final_score < means[0]:
                output += extra_output_B_C[0]
            else:
                output += extra_output_B_C[1]
        elif (output == outputs_bayes[2]):
            if final_score < means[1]:
                output += extra_output_B_C[0]
            else:
                output += extra_output_B_C[1]

    return output

#Suchanya Limpakom
#Olga Manakina