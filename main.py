import scoring
import skills

if __name__ == '__main__':
    filepath = 'data_files\Example5.csv'
    results = skills.get_data(filepath)
    print(scoring.naive_bayes_classifier(results))
    print(skills.recommendation_string(skills.best_match(skills.ideal_set)))