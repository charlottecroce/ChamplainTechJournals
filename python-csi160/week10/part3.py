final_election_results = {}

def record_candidate_votes(election_results, candidate, num_votes, precinct):
    """Records votes for a particular candidate in one precinct in the election_results.

    The precinct is not used for the function currently.

    Optional tip: Using method .get() can allow you to avoid needing a if or try statement

    params:
    election_results (dict): Dictionary to be modified by recording the votes for a candidate in a precinct
    cadidate (string): The name of a candidate.  Used as the 'key' in the election_results dictionary.
    num_votes (int): The number of votes to add to the candidate's total
    """
    if candidate in election_results:
        # If candidate exists, add to the existing total
        election_results[candidate] += num_votes
    else:
        # If candidate doesn't exist, create a new entry
        election_results[candidate] = num_votes



# This section is for testing purposes, do not modify
# FYI: These numbers are made up for example purposes only
record_candidate_votes(final_election_results,'Miro Weinberger', 100, 'Ward 1')
record_candidate_votes(final_election_results,'Max Tracy', 140, 'Ward 1')
record_candidate_votes(final_election_results,'Ali Dieng', 27, 'Ward 1')
record_candidate_votes(final_election_results,'Miro Weinberger', 50, 'Ward 2')
record_candidate_votes(final_election_results,'Max Tracy', 150, 'Ward 2')
record_candidate_votes(final_election_results,'Ali Dieng', 35, 'Ward 2')
record_candidate_votes(final_election_results,'Miro Weinberger', 100, 'Ward 3')
record_candidate_votes(final_election_results,'Max Tracy', 100, 'Ward 3')
record_candidate_votes(final_election_results,'Ali Dieng', 56, 'Ward 3')
record_candidate_votes(final_election_results,'Miro Weinberger', 320, 'Ward 4')
record_candidate_votes(final_election_results,'Max Tracy', 213, 'Ward 4')
record_candidate_votes(final_election_results,'Ali Dieng', 175, 'Ward 4')
print(final_election_results)