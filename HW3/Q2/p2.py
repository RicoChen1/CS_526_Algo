# My idea:
#  Use recursion to generate all substrings, then check
# Recursive fn(start, end), represent range of sub-string
# R terminate when start > n-1
# In each R layer, pin start, then let end from start+1 to n, recurse next start

# pscode
# fn gen_substrings(s, start):
#   if start >= len(s): end
#   for end from start+1 to len(s):
#       substring = s[start:end]
#       add to global_Set
#   gen_substrings(s,start+1)

def unique_substring(s):
    """ Find all uniq sub_s. Return sub_s set and number"""
    global_set = set() # 字串集合

    def gen_substrings(start):
        """generate all sub_s starting with Start, from Start position"""
        
        # Base case: if start out of string range, end
        if start >= len(s):
            return
        
        # Generation
        for end in range(start+1, len(s)+1):
            substring = s[start:end]
            global_set.add(substring)
            # optional
            # print(f"生成子串: {substring} (位置:{start}-{end-1})")

        gen_substrings(start + 1) # Deal with next start postion
    
    # Start the recursion
    gen_substrings(0)
    return global_set, len(global_set) # 返回集合及尺寸
    
# Test code. AI Assist print and file casting issue. Really stragne issue.
# AI analysis believes that it is the display limitation of powershell terminal, emmmmm
# What's interesting is that cmd/bash doesn't have this problem
if __name__ == "__main__":
    input_str = 'abcab'
    result_set, count = unique_substring(input_str)
    
    # Print results
    print(f"Input: {input_str}")
    output_str = ", ".join(sorted(result_set, key=lambda x: (len(x), x)))
    print(f"Output: {output_str} -> {count}")
    
    # Also save to file for verification
    with open('p2_output.txt', 'w') as f:
        f.write(f"Input: {input_str}\n")
        f.write(f"Output: {output_str} -> {count}\n")