% Facts: disease(Disease, Symptom).
disease(flu, fever).
disease(flu, headache).
disease(flu, chills).
disease(flu, body_ache).

disease(common_cold, sneezing).
disease(common_cold, sore_throat).
disease(common_cold, runny_nose).
disease(common_cold, headache).

disease(strep_throat, sore_throat).
disease(strep_throat, fever).
disease(strep_throat, swollen_lymph_nodes).

disease(covid_19, fever).
disease(covid_19, cough).
disease(covid_19, tiredness).
disease(covid_19, loss_of_taste_or_smell).

disease(allergy, sneezing).
disease(allergy, runny_nose).
disease(allergy, itchy_eyes).
disease(allergy, watery_eyes).

% Rule to diagnose disease based on symptoms.
diagnose(Disease) :-
    write('Enter symptoms one by one (type "done" to finish):'), nl,
    read_symptoms(Symptoms),
    diagnose_disease(Disease, Symptoms).

% Read symptoms from the user until "done" is entered.
read_symptoms(Symptoms) :-
    read(Symptom),
    ( Symptom == done ->
        Symptoms = []
    ;
        read_symptoms(RestSymptoms),
        Symptoms = [Symptom | RestSymptoms]
    ).

% Check which disease matches all symptoms provided.
diagnose_disease(Disease, Symptoms) :-
    disease(Disease, _), % Get all diseases
    check_symptoms(Disease, Symptoms).

% Check if all symptoms match the disease.
check_symptoms(_, []).

check_symptoms(Disease, [Symptom | RestSymptoms]) :-
    disease(Disease, Symptom),
    check_symptoms(Disease, RestSymptoms).

% Main predicate to start the diagnosis.
start_diagnosis :-
    write('Welcome to the medical diagnosis system!'), nl,
    write('Please enter your symptoms to get a diagnosis.'), nl,
    diagnose(Disease),
    write('Based on the symptoms, you might have: '), write(Disease), nl.
