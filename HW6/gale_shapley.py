import sys

def parse_input(filename):
    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None, None, None

    n = int(lines[0])
    
    men_prefs = {}
    women_prefs = {}
    
    """
    # First n lines after count = men
    # Next n lines = women
    # However: 
    # Let's assume order is strictly N men then N women as per sample.
    """
    
    men_names = []
    
    for i in range(1, n + 1):
        parts = lines[i].split()
        man = parts[0]
        prefs = parts[1:]
        men_prefs[man] = prefs
        men_names.append(man)
        
    for i in range(n + 1, 2 * n + 1):
        parts = lines[i].split()
        woman = parts[0]
        prefs = parts[1:]
        women_prefs[woman] = prefs

    return men_names, men_prefs, women_prefs

def gale_shapley(men_names, men_prefs, women_prefs):
    # Init all men women as free
    free_men = list(men_names)
    
    
    matches = {} # partner info. Key: Woman, Value: Man
    
    # Keep track of which woman each man is currently proposing to
    man_next_proposal_idx = {man: 0 for man in men_names} # index in his pref list
    
    # Pre process women preferences. O(1) lookup: {Woman: {Man: Rank}}
    women_rankings = {}  # Note: lower is better, 0 = best
    for woman, prefs in women_prefs.items():
        women_rankings[woman] = {man: i for i, man in enumerate(prefs)}

    while free_men:
        man = free_men[0]
        
        proposal_idx = man_next_proposal_idx[man]  # Get woman he wants to propose to next
        
        # If he has proposed to everyone (wtf), break or error
        if proposal_idx >= len(men_prefs[man]):
            free_men.pop(0)
            continue
            
        woman = men_prefs[man][proposal_idx]
        man_next_proposal_idx[man] += 1
        
        if woman not in matches: # She free, engage them
            matches[woman] = man
            free_men.pop(0)
        else:
           
            current_partner = matches[woman] # She's currently match with current_partner
            
            # Check if she prefers 'man' > 'current_partner', by rank map
            if women_rankings[woman][man] < women_rankings[woman][current_partner]:
                # prefers new man
                matches[woman] = man
                free_men.pop(0) # abandon previous man
                free_men.append(current_partner)
            else:
                # Proposal reject, man still free will try next girl
                pass
                
    return matches

def run_test(filename):
    print(f"\n{'='*20} Testing {filename} {'='*20}")
    men_names, men_prefs, women_prefs = parse_input(filename)
    
    if men_names is None:
        return

    # Print Input. Cast if too large
    print("Input Summary:")
    print(f"Number of couples: {len(men_names)}")
    if len(men_names) <= 15:
        print("Men Preferences:")
        for m in men_names:
            print(f"  {m}: {men_prefs[m]}")
        print("Women Preferences:")
        for w in women_prefs:
            print(f"  {w}: {women_prefs[w]}")
    else:
        print("(Input too large to display fully)")

    matches = gale_shapley(men_names, men_prefs, women_prefs)
    
    print("\nStable Matches (Woman : Man):")
    for woman in sorted(matches.keys()):
        print(f"{woman} : {matches[woman]}")

if __name__ == "__main__":
    files = ['HW6/marraige_ten.txt', 'HW6/marriage_hundred.txt']
    # Note: marraige_thousand.txt might be too large to run quickly or print, 
    # but we can include it if needed. The prompt asks for "supplied input samples".
    # I'll stick to ten and hundred for the demo to keep output manageable, 
    # or I can add thousand but it will be very long.
    # Let's add thousand but relying on the truncation in print.
    
    # Checking if files exist before adding to list to avoid errors if user didn't download all
    import os
    if os.path.exists('HW6/marraige_thousand.txt'):
        files.append('HW6/marraige_thousand.txt')
        
    for f in files:
        run_test(f)
