# https://www.codewars.com/kata/5818236ae7f457017b00022b
#
# attempt #1:
def bang_start_string(s, history):
    # note: "  " counts as 2 characters!
    # look for string starting with "  " + s
    cmd_idx = history.rfind("  " + s)
    if cmd_idx != -1:
        # check if found substring ends with "\n"
        idx_end = history[cmd_idx:].find("\n")

        if idx_end != -1:
            # cmd_idx + 2 because we want to ignore preceeding "  "
            return history[cmd_idx + 2:cmd_idx + idx_end]
        # if not, assume it's the last history entry
        else:
            # cmd_idx + 2 because we want to ignore preceeding "  "
            return history[cmd_idx + 2:]
    else:
        return f"!{s}: event not found"
#
# attempt #2:
def bang_start_string(s, history):
    hist = history.split("\n")
    hist = [i.strip() for i in hist]
    # remove numbers from hist entries
    hist = [" ".join(i.split()[1:]) for i in hist]
    # reverse the list because we look for most recent command
    hist = list(reversed(hist))
    
    for entry in hist:
        if entry.startswith(s):
            # parse found entry
            return entry

    return f"!{s}: event not found"
