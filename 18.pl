% Facts: name(Name, DOB).
name('John Doe', '1990-01-01').
name('Jane Smith', '1985-05-23').
name('Alice Johnson', '1992-07-15').
name('Bob Brown', '1978-12-03').

% Rule to find DOB by name
find_dob(Name, DOB) :-
    name(Name, DOB).

% Rule to find name by DOB
find_name(DOB, Name) :-
    name(Name, DOB).
