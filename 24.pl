% Facts: diet(Disease, Diet).
diet(diabetes, 'Low sugar, high fiber, whole grains, vegetables, lean protein').
diet(hypertension, 'Low sodium, high potassium, fruits, vegetables, whole grains').
diet(heart_disease, 'Low saturated fats, high fiber, fruits, vegetables, whole grains').
diet(obesity, 'Low calorie, balanced diet with fruits, vegetables, whole grains, lean protein').
diet(anemia, 'High iron, vitamin C, lean meats, leafy greens, beans, fortified cereals').

% Rule to suggest diet based on disease.
suggest_diet(Disease, Diet) :-
    diet(Disease, Diet).

% Catch-all for diseases not in the database.
suggest_diet(Disease, 'Diet information not available') :-
    \+ diet(Disease, _).

% Example diseases
disease(diabetes).
disease(hypertension).
disease(heart_disease).
disease(obesity).
disease(anemia).
