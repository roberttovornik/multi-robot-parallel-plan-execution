# we get the plan
# SCENARIO 1
r_1_path = [[2, 0], [2, 1], [1, 1], [1, 2], [0, 2]]
r_2_path = [[2, 1], [1, 1], [0, 1]]
r_3_path = [[1, 0], [1, 0], [1, 0], [1, 1], [1, 2]]

# SCENARIO 2

# r_1_path = [[0, 0], [1, 0], [2, 0]]
# r_2_path = [[0, 1], [1, 1], [2, 1]]
# r_3_path = [[0, 2], [1, 2], [2, 2]]



#### 3 EXTRA - BRATKO

# r_1_path = [[2, 0], [2, 0], [2, 0], [2, 1], [2, 2]]
# r_2_path = [[2, 1], [2, 1], [2, 1], [1, 1], [2, 1]]
# r_3_path = [[2, 2], [1, 2], [1, 1], [1, 0], [2, 0]]


all_robot_paths = [r_1_path, r_2_path, r_3_path]
initial_robot_paths = [r_1_path[:], r_2_path[:], r_3_path[:]]

""" 4 ROBOTS MATCH-UP """

#### EXTRA - ROBERT

# r_1_path = [[1, 0], [1, 1], [1, 2], [2, 2]]
# r_2_path = [[2, 0], [1, 0], [1, 1], [1, 2]]
# r_3_path = [[1, 2], [2, 2], [2, 1], [2, 0]]
# r_4_path = [[2, 2], [2, 1], [2, 0], [1, 0]]


# SCENARIO 4  L, M, M, M
# r_1_path = [[1, 0], [1, 1], [1, 2]]
# r_2_path = [[0, 1], [0, 0], [1, 0], [2, 0], [2, 1]]
# r_3_path = [[1, 1], [0, 1], [0, 0], [1, 0], [1, 1]]
# r_4_path = [[2, 1], [2, 1], [1, 1], [0, 1]]

def swap_x_and_y_path(path):
    new_path = []
    for [x,y] in path:
        new_path.append([y,x])

    return new_path

# SCENARIO 5  L, M, M, M
# Start positions: [[2, 0], [1, 1], [0, 2], [2, 1]]
# End   positions: [[0, 1], [0, 2], [0, 0], [1, 0]]

# r_1_path = [[2, 0], [1, 0], [1, 1], [0, 1]]
# r_2_path = [[1, 1], [1, 2], [0, 2]]
# r_3_path = [[0, 2], [0, 1], [0, 0]]
# r_4_path = [[2, 1], [2, 1], [2, 0], [1, 0]]

# SCENE 6

# Start positions: [[1, 2], [0, 2], [2, 0], [2, 2]]
# End   positions: [[0, 2], [1, 2], [2, 2], [0, 0]]

# r_1_path = [[1, 2], [1, 1], [1, 0], [0, 0], [0, 1], [0, 2]]
# r_2_path = [[0, 2], [0, 1], [0, 1], [0, 2], [1, 2]]
# r_3_path = [[2, 0], [2, 0], [2, 0], [2, 0], [2, 1], [2, 2]]
# r_4_path = [[2, 2], [2, 1], [2, 1], [1, 1], [1, 0], [0, 0]]


# SCENE 7
# Start positions: [[0, 1], [2, 0], [0, 0], [1, 2]]
# End   positions: [[1, 0], [2, 2], [1, 1], [0, 0]]

# r_1_path = [[0, 1], [0, 1], [0, 0], [1, 0]]
# r_2_path = [[2, 0], [2, 0], [2, 0], [2, 1], [2, 2]]
# r_3_path = [[0, 0], [1, 0], [1, 1]]
# r_4_path = [[1, 2], [0, 2], [0, 2], [0, 1], [0, 0]]


# SCENARIO 8

# Start positions: [[0, 0], [2, 1], [2, 2], [1, 1]]
# End   positions: [[0, 1], [0, 0], [1, 1], [1, 0]]

# r_1_path = [[0, 0], [0, 0], [0, 1]]
# r_2_path = [[2, 1], [2, 0], [1, 0], [0, 0]]
# r_3_path = [[2, 2], [1, 2], [0, 2], [1, 2], [1, 1]]
# r_4_path = [[1, 1], [1, 1], [2, 1], [2, 0], [1, 0]]

# SCENARIO 4. 5
# all_robot_paths = [r_1_path, r_2_path, r_3_path, r_4_path]
# initial_robot_paths = [r_1_path[:], r_2_path[:], r_3_path[:], r_4_path[:]]

sum_unopti = 0

def get_point_to_goal_orientation(pos, next_pos):
    """
        Function accepts current position and next goal position both in form [x, y].
        Movement can only be made in 4 directions (up, down, left or right).
        Returns required goal orientation.
    """

    x_1 = pos[0]
    y_1 = pos[1]

    x_2 = next_pos[0]
    y_2 = next_pos[1]

    if x_1 > x_2 and y_1 == y_2:
        # moving up
        return "N"
    elif x_1 < x_2 and y_1 == y_2:
        # moving down
        return "S"
    elif x_1 == x_2 and y_1 > y_2:
        # moving left
        return "W"
    elif x_1 == x_2 and y_1 < y_2:
        # moving right
        return "E"
    else:
        return "SAME"

def get_theoretical_path_with_orientations(all_default_paths):
    """ Function takes all robot paths and returns a list of robot paths with their position orientations. """

    oriented_paths = [["N"] for p in all_default_paths]

    merged_paths = []

    for i, path in enumerate(all_default_paths):
        for j in range(len(path)):
            #print(" I ",i," J ",j)
            if j == len(path) - 1:
                # special case
                oriented_paths[i].append("N")
            else:
                new_orient = get_point_to_goal_orientation(path[j], path[j + 1])

                if new_orient == "SAME":
                    oriented_paths[i].append(oriented_paths[i][len(oriented_paths[i])-1])
                else:
                    oriented_paths[i].append(new_orient)

        merged_paths.append([path,oriented_paths[i]])

    return merged_paths

def is_double_rotation_required(orientations, index):
    if orientations[index] == "N" and orientations[index+1] == "S" or \
        orientations[index] == "S" and orientations[index + 1] == "N" or \
        orientations[index] == "W" and orientations[index + 1] == "E" or \
        orientations[index] == "E" and orientations[index + 1] == "W":
        return True
    else:
        return False

def is_rotation_required(orientations, index):
    if(orientations[index] == orientations[index+1]):
        return False
    else:
        return True

# do not use, better function: get_real_time_wait_times
def get_real_time_wait_times_depretacted(paths_with_orientations):
    """
        Function accepts all robot paths along with their pose orientations, and returns optimized path plan, corrected
        with the cost of required path rotations.
    """
    additional_hold_commands_required = [[] for r in paths_with_orientations ]

    for r_i, r_path_orientation in enumerate(paths_with_orientations):
        my_path = r_path_orientation[0]
        my_orientations = r_path_orientation[1]

        # go through each step and check successor step of other robots
        for step_i, step in enumerate(my_path):
            for r_j, r_j_path_orient in enumerate(paths_with_orientations):
                # do not compare with yourself
                if(
                    r_i == r_j    #nothing to compare
                    or
                    len(r_j_path_orient[0]) <= step_i + 1  # the other robot has already reached it's goal
                    or
                    step_i == len(my_path)-1    # last rotation is in place -> we do not care about it
                    or
                    not is_rotation_required(my_orientations, step_i)   # no rotation is required
                ):
                    continue    # go to next robot
                else:
                    # only append if my current step is same as his next (he is dependant of me)
                    ##### also append if he is waiting on me.. so while his position is equal to current, keep shifting
                    if step == r_j_path_orient[0][step_i+1]:
                        additional_hold_commands_required[r_j].append(step_i+1)

    # clean up hold commands (we do not wish to duplicate them more)
    return additional_hold_commands_required

# do not use, problems with delays ( works great for one-step, get's lost on previous step dependencies)
# missing global oversight
def get_real_time_wait_times(paths_with_orientations):
    """
        Function accepts all robot paths along with their pose orientations, and returns optimized path plan, corrected
        with the cost of required path rotations.
    """
    rotational_delays_of_robots = [[] for r in paths_with_orientations ]

    # first calculate delays based on own robot path
    for r_i, r_path_orientation in enumerate(paths_with_orientations):
        my_path = r_path_orientation[0]
        my_orientations = r_path_orientation[1]

        # until pre last element (don't look over the edge)
        for i in range(len(my_path)-1):
            if i == 0:
                if is_rotation_required(my_orientations, i):
                    rotational_delays_of_robots[r_i].append(1)
                else:
                    rotational_delays_of_robots[r_i].append(0)
            else:
                current_delays = rotational_delays_of_robots[r_i][len(rotational_delays_of_robots[r_i])-1]
                if is_rotation_required(my_orientations, i):
                    rotational_delays_of_robots[r_i].append(current_delays + 1)
                else:
                    rotational_delays_of_robots[r_i].append(current_delays)

    for i in rotational_delays_of_robots:
        print(i)

    additional_hold_commands_required = [[] for r in paths_with_orientations]

    for r_i, r_path_orientation in enumerate(paths_with_orientations):
        my_path = r_path_orientation[0]
        my_orientations = r_path_orientation[1]

        # go through each step and check successor step of other robots
        for step_i, step in enumerate(my_path):
            for r_j, r_j_path_orient in enumerate(paths_with_orientations):
                # do not compare with yourself
                if (
                    r_i == r_j  # nothing to compare
                    or
                    len(r_j_path_orient[0]) <= step_i + 1  # the other robot has already reached it's goal
                    or
                    step_i == len(my_path) - 1  # last rotation is in place -> we do not care about it
                    or
                    not is_rotation_required(my_orientations, step_i)  # no rotation is required
                ):
                    continue  # go to next robot
                else:
                    # only append if my current step is same as his next (he is dependant of me)
                    ##### also append if he is waiting on me.. so while his position is equal to current, keep shifting
                    if step == r_j_path_orient[0][step_i + 1]:
                        # i want you to add at index [step_i+1] rotational_delays_of_robots[r_i][step_i]] rotations
                        # (as much as i have to this point)
                        additional_hold_commands_required[r_j].append([step_i+1, rotational_delays_of_robots[r_i][step_i-1]])

    print("ADDITIONAL REQUESTS")
    for i in additional_hold_commands_required:
        print(i)

    #additional_hold_commands_required = [[[2,3], [1,1], [4,3]], [[2,4],[3,3],[3,5],[3,2]], [[3, 5], [3, 3], [4, 4], [3, 6]]]


    # clean up hold commands (we do not wish to duplicate them more), keep the maximum (toughest condition)
    print(additional_hold_commands_required)


    check_robot_indeces = [ [] for r in additional_hold_commands_required]

    for r_i in range(len(additional_hold_commands_required)):
        for pair in additional_hold_commands_required[r_i]:
            if pair[0] not in check_robot_indeces[r_i]:
                check_robot_indeces[r_i].append(pair[0])

    print("CHECK THESE INDICES")
    print(check_robot_indeces)

    cleaned_hold_commands = [[] for r in paths_with_orientations]
    for r_i in range(len(additional_hold_commands_required)):
        for indx in check_robot_indeces[r_i]:
            max_val = -1
            for k in additional_hold_commands_required[r_i]:
                if k[0] == indx:
                    if k[1] > max_val:
                        max_val = k[1]
            if(max_val != -1):
                cleaned_hold_commands[r_i].append([indx, max_val])

    print("CLEANED MAX COMMANDS")
    print(cleaned_hold_commands)

    ###### SORT INDICES BY SIZE:
    for r_i in range(len(cleaned_hold_commands)):
        for i in range(len(cleaned_hold_commands[r_i])):
            for j in range(len(cleaned_hold_commands[r_i])):
                if cleaned_hold_commands[r_i][i] < cleaned_hold_commands[r_i][j]:
                    cleaned_hold_commands[r_i][i], cleaned_hold_commands[r_i][j] = cleaned_hold_commands[r_i][j], cleaned_hold_commands[r_i][i]

    print("ORDERED HOLD COMMANDS")
    print(cleaned_hold_commands)

    ### subtract current from future
    for r_i in range(len(cleaned_hold_commands)):
        for i in range(len(cleaned_hold_commands[r_i])):
            for j in range(i+1, len(cleaned_hold_commands[r_i])):
                cleaned_hold_commands[r_i][j][1] -= cleaned_hold_commands[r_i][i][1]

    print("HOLD COMMAND VALUES FIXED")
    print(cleaned_hold_commands)

    print("=====================================")
    print(rotational_delays_of_robots)


    ### now subtract in rotational commands
    for r_i in range(len(rotational_delays_of_robots)):
        for i in range(len(rotational_delays_of_robots[r_i])):
            for j in range(i+1, len(rotational_delays_of_robots[r_i])):
                rotational_delays_of_robots[r_i][j] -= rotational_delays_of_robots[r_i][i]

    #### add all additional hold_commands to robot_delays

    for r_i in range(len(rotational_delays_of_robots)):
        for holds in cleaned_hold_commands[r_i]:
            if holds[1] > 0:
                rotational_delays_of_robots[r_i][holds[0]-1] += holds[1]

    print("FINAL HOLD COMMANDS")
    print(rotational_delays_of_robots)

    return rotational_delays_of_robots

def append_additional_hold_commands_to_robot_path(robot_paths, additonal_hold_cmds):
    new_paths = [[] for r in robot_paths]

    # expand new arrays in order to avoid indexation problems
    for r in range(len(robot_paths)):
        new_paths[r].extend([ "X" for i in range(len(robot_paths[r]) + len(additonal_hold_cmds[r]))])

    # print("NEW PATH LIST")
    # print(new_paths)

    # now override them with default values
    for i in range(len(robot_paths)):
        for j in range(len(robot_paths[i])):
            # print(i, j)
            new_paths[i][j] = robot_paths[i][j]

    # print("EXPANDED PATH LIST")
    # print(new_paths)

    # insert new hold commands
    # !!! FROM BACK FORTH !!! TO AVOID INDEX SHIFT
    for r, hold_cmds in enumerate(additonal_hold_cmds):
        i = len(hold_cmds)-1
        while i >= 0:
            insert_times = additonal_hold_cmds[r][i]
            for ins in range(0, insert_times):
                new_paths[r].insert(i, robot_paths[r][i])
            i -= 1
    # print("COMMANDS INSERTED")
    # print(new_paths)

    # create new arrays
    cleared_paths = [[] for r in robot_paths]
    for i, path in enumerate(new_paths):
        for j in path:
            if j != "X":
                cleared_paths[i].extend([j])

    # for i in range(len(cleared_paths)):
    #     print(i, " PATH: ", cleared_paths[i])

    return cleared_paths

def get_rotations_from_sequential_orientations(heading_1, heading_2):
    """ Function accepts heading_1 and heading_2 and returns required rotational operations. """

    if heading_1 == heading_2:
        return ["X"]

    # NORTH
    if heading_1 == "N":
        if heading_2 == "S":
            return ["R", "R"]
        elif heading_2 == "W":
            return ["L"]
        elif heading_2 == "E":
            return ["R"]

    # SOUTH
    elif heading_1 == "S":
        if heading_2 == "N":
            return ["R", "R"]
        elif heading_2 == "W":
            return ["R"]
        elif heading_2 == "E":
            return ["L"]

    # WEST
    elif heading_1 == "W":
        if heading_2 == "N":
            return ["R"]
        elif heading_2 == "S":
            return ["L"]
        elif heading_2 == "E":
            return ["R", "R"]

    # EAST
    elif heading_1 == "E":
        if heading_2 == "N":
            return ["L"]
        elif heading_2 == "S":
            return ["R"]
        elif heading_2 == "W":
            return ["R", "R"]

    # KEEP ORIENTATION
    else:
        return ["X"]

def delayed_path_to_positions_path(path):
    positions_path = []

    for i, p in enumerate(path):
        if p == "delay" or p == "rotate":
            positions_path.append(positions_path[i-1])
        else:
            positions_path.append(p)

    return positions_path

def validate_delay_removal(r1_path, r2_path, delay_i):
    # if we remove one, our current state will equal our next state
    compare_i = delay_i + 1

    r1_positions = delayed_path_to_positions_path(r1_path)
    r2_positions = delayed_path_to_positions_path(r2_path)

    r1_path_len = len(r1_positions)
    r2_path_len = len(r2_positions)

    ### FIX: VALIDATION BY LAST PLACE ADDED
    while compare_i < r1_path_len or compare_i - 1 < r2_path_len:

        if compare_i >= r1_path_len:
            if r1_positions[r1_path_len-1] == r2_positions[compare_i - 1]:
                return False
        elif compare_i - 1 >= r2_path_len:
            if r1_positions[compare_i] == r2_positions[r2_path_len-1]:
                return False
        else:
            if r1_positions[compare_i] == r2_positions[compare_i-1]:
                return False

        compare_i += 1

    # end of while ( compare )

    # no conflicts found
    return True


def swap_with_default_delays(path):

    # print("SWAPPING -------------------------------------------------------")


    new_path = path[:]
    n = len(new_path)

    ## check from back forth
    cmpr_i = n-1
    i = n-2


    # print("cmpr_i ", cmpr_i, " i ", i)
    while i >= 0:
        if new_path[i] == "delay" or new_path[i] == "rotate":
            # print("pass")
            pass
        else:
            # print(new_path[i], " vs ", new_path[cmpr_i])
            if new_path[i] == new_path[cmpr_i]:
                # new_path[cmpr_i] = "delay_s"
                new_path[cmpr_i] = "delay"
            cmpr_i = i
        i -= 1

    return new_path

def theoretical_paths_to_real_world_theoretical_paths(paths_with_orientations):
    """
        Function accepts and list of pairs [ robot_path, robot_orientations].
    """

    print("PATHS WITHOUT DELAYS: ")
    for r in paths_with_orientations:
        print(r[0])


    # find maximum path length
    max_path_length = -1
    for r in paths_with_orientations:
        # index 0 is path, index 1 is
        if len(r[0]) > max_path_length:
            max_path_length = len(r[0])

    print("MAX length: ", max_path_length)

    ## robot delay requests at index step
    robot_delay_request_index = []
    robot_double_delay_request_index = []
    for step in range(0, max_path_length-1): # one step less, due to 1 step overlook comparison
        for r_i, path_and_orient in enumerate(paths_with_orientations):
            # check if rotation is required
            if step < len(paths_with_orientations[r_i][0]) - 1:
                if is_double_rotation_required(paths_with_orientations[r_i][1], step):
                    robot_double_delay_request_index.insert(0, step)
                    break
                elif is_rotation_required(paths_with_orientations[r_i][1], step):
                    robot_delay_request_index.insert(0, step)
                    break

    print("ROBOT INDEX DELAY REQUESTS: ", robot_delay_request_index)
    print("ROBOT INDEX DOUBLE DELAY REQUESTS: ", robot_double_delay_request_index)

    # insert double delays (but not if robot has already reached it's goal)
    for r in paths_with_orientations:
        for delay_i in robot_double_delay_request_index:
            if delay_i < len(r[0])-1:
                if is_double_rotation_required(r[1], delay_i):
                    r[0].insert(delay_i + 1, "rotate")
                    r[0].insert(delay_i + 2, "rotate")
                    r[1].insert(delay_i + 1, r[1][delay_i])
                    r[1].insert(delay_i + 2, r[1][delay_i])
                else:
                    r[0].insert(delay_i + 1, "delay")
                    r[0].insert(delay_i + 2, "delay")
                    r[1].insert(delay_i + 1, r[1][delay_i])
                    r[1].insert(delay_i + 2, r[1][delay_i])

    print("PATHS WITH DOUBLE DELAYS: ")
    for r in paths_with_orientations:
        print(r[0])


    for i in robot_double_delay_request_index:
        j = 0
        while j < len(robot_delay_request_index):
            if robot_delay_request_index[j] >= i:
                robot_delay_request_index[j] += 2
            j += 1

    # insert delays (but not if robot has already reached it's goal)
    for r in paths_with_orientations:
        for delay_i in robot_delay_request_index:
            if delay_i < len(r[0])-1:
                if r[0][delay_i+1] != "delay" and r[0][delay_i+1] != "rotate":
                    if is_rotation_required(r[1], delay_i):
                        r[0].insert(delay_i + 1, "rotate")
                        r[1].insert(delay_i + 1, r[1][delay_i])
                    else:
                        r[0].insert(delay_i + 1, "delay")
                        r[1].insert(delay_i + 1, r[1][delay_i])

    print("PATHS WITH DELAYS ")
    for r in paths_with_orientations:
        print(r[0])

    print("UNOPTIMAL ", sum([len(x[0]) for x in paths_with_orientations]))
    print("ADDITIONAL STEP - SWAP AND APPEND DEFAULT HOLD OPREATIONS - delays ")

    for r in paths_with_orientations:
        r[0] = swap_with_default_delays(r[0])

    for r in paths_with_orientations:
            print(r[0])

    ## remove any delays, that do not affect other robots

    # find maximum path length (with delays)
    max_path_length_delays = -1
    for r in paths_with_orientations:
        # index 0 is path, index 1 is
        if len(r[0]) > max_path_length_delays:
            max_path_length_delays = len(r[0])

    print("MAX length (w delays): ", max_path_length_delays)

    ### delete all delays that cause problems


    # print("ENUMERATION: ")
    # for i,j in enumerate(paths_with_orientations):
    #     print(i,j)



    ### repeat delay correction as long as any robot makes changes (optimize without overlaps)
    check_optimization = 1

    while check_optimization:

        check_optimization = 0

        ### take each robot and study it's path
        for r, path_with_orient in enumerate(paths_with_orientations):
            # print("ROBOT ", r)
            current_robot_path = path_with_orient[0]
            current_robot_heading = path_with_orient[1]

            ## go over path, from back forth and check for any collision with other robots
            curr_path_len = len(current_robot_path)
            curr_step = curr_path_len - 2 # we don't care about the final position

            collision = 0

            while( curr_step > 0): # we don't care about the starting position either

                if current_robot_path[curr_step] == "delay":    # we don't care about rotations either, they are obligatory
                    ### check if we can remove it
                    # print("DELAY OF ", r , " AT ", curr_step)
                    for other_robot, other_path_with_orient in enumerate(paths_with_orientations):
                        if other_robot == r:
                            continue
                        # print("COMPARING : ", r, " with ", other_robot, " -------------------------------- ")
                        other_robot_path = other_path_with_orient[0]

                        ### WHILE VALIDATION CUT
                        if not validate_delay_removal(current_robot_path, other_robot_path, curr_step):
                            collision = 1

                        if collision > 0:
                            break

                    # end of for other_robot

                    if collision > 0:
                        break

                    current_robot_path.pop(curr_step)
                    current_robot_heading.pop(curr_step)
                    curr_path_len = len(current_robot_path)
                    check_optimization = 1

                curr_step -= 1
            # end of while step > 0
            # print("========================= NEXT ROBOT ============================")

    #end of check_optimization

    print("PATHS WITH DELAYS OPTIMIZED: ")
    for r in paths_with_orientations:
        print(r[0])

    for r in paths_with_orientations:
        for i in range(len(r[0])):
            if r[0][i] == "delay" or r[0][i] == "rotate":
                r[0][i] = r[0][i-1]

    # print("PATHS WITH POSITIONS")
    # for r in paths_with_orientations:
    #     print(r[0])

    new_paths = []

    for r in paths_with_orientations:
        new_paths.append(r[0])

    return new_paths

def theoretical_path_to_robot_path(default_path):
    """"
        Function accepts theoretical path in a form of a list of 2D coordinates (robot positions during movement),
        and returns a list of robot commands, such as move, rotate left, rotate right, hold,...

        Orientation is given in compass form (North - N, West - W, East - E, South - S).

        Initial orientation is presumed as North - N, same with final orientation.

        Path is also optimized.

        Optimization: when rotation is required, try to place it instead of hold operation. Rotate right after
        reaching current goal point (no need to wait in case of hold operation).
    """

    robot_path = ['Hold']
    orientation_sequence = ["N"]
    new_orient = ""
    required_rotation = []

    # First step - get a list of pose orientations
    for i in range(len(default_path)):
        if (i == len(default_path) - 1):
            # special case
            orientation_sequence.append("N")
        else:
            new_orient = get_point_to_goal_orientation(default_path[i], default_path[i + 1])

            if new_orient == "SAME":
                orientation_sequence.append(orientation_sequence[len(orientation_sequence)-1])
            else:
                orientation_sequence.append(new_orient)

    # FIX STEP REQUIRED - SYNCHRONIZE GOAL ROTATIONS AND MOVEMENT WITH OTHER ROBOTS
    print(orientation_sequence)


    # Second step - transform pose difference into moves (rotations)
    for i in range(len(default_path)):
        if (i == len(default_path) - 1):
            # special case
            required_rotation = get_rotations_from_sequential_orientations(orientation_sequence[i], "N")
            if required_rotation == ["X"]:
                pass
            else:
                if len(required_rotation) == 2 and len(robot_path) > 2 \
                        and robot_path[-1] == "Hold" and robot_path[-2] == "Hold":
                    robot_path.pop()
                    robot_path.pop()
                elif len(robot_path) > 1 and robot_path[-1] == "Hold":
                    robot_path.pop()

                robot_path.extend(required_rotation)

        else:
            required_rotation = get_rotations_from_sequential_orientations(orientation_sequence[i], orientation_sequence[i+1])
            if required_rotation == ["X"]:
                if default_path[i] == default_path[i+1]:
                    robot_path.extend(["Hold"])
                else:
                    robot_path.extend(["Move"])
            else:
                if len(required_rotation) == 2 and len(robot_path) > 2 \
                        and robot_path[-1] == "Hold" and robot_path[-2] == "Hold":
                    robot_path.pop()
                    robot_path.pop()
                elif len(robot_path) > 1 and robot_path[-1] == "Hold":
                    robot_path.pop()

                robot_path.extend(required_rotation)
                if default_path[i] != default_path[i+1]:
                    robot_path.extend(["Move"])

    # if robot_path[0] == "Hold":
    #     robot_path.pop(0)

    return robot_path

def get_robot_positions_based_on_commands(default_robot_path, robot_commands):
    """
        Function requires two arguments:
            - robot path: default robot path positions ( in coordinates )
            - robot commands: list of robot commands ( to predict position shifts )

        Returns a list of robot positions ( in coordinates ) throughout the command execution.
    """

    #### REMOVE DEFAULT GIVEN DELAYS
    default_path = default_robot_path[:]

    n = len(default_robot_path)

    i = 0
    while i < n-1:
        if default_path[i+1] == default_path[i]:
            default_path.pop(i+1)
            n -= 1
            i -= 1
        i += 1


    robot_positions = []

    # print("CMD - > POSE")
    # print(default_path)
    # print(robot_commands)

    pose = 0
    for cmd in robot_commands:
        if cmd == "L" or cmd == "R" or cmd == "Hold" or cmd == "Hold-S":
            robot_positions.append(default_path[pose])
        else:
            pose += 1
            robot_positions.append(default_path[pose])

    return robot_positions


def paths_free_of_collision(robot_path, other_path):
    j = 0
    for i, pose in enumerate(other_path):

        # manage indeces
        if i > len(robot_path) - 1:
            j = len(robot_path) - 1
        else:
            j = i

        if robot_path[j] == other_path[i]:
            # print(" CRASH AT ", i, " - ", j )
            return False


    ## no collision detected
    return True

def validate_merge_of_rotation_and_delay(r_index, delay_i, all_robot_paths, default_paths):

    for i, p in enumerate(all_robot_paths):
        if i == r_index:
            continue
        else:
            r_path = get_robot_positions_based_on_commands(default_paths[r_index], all_robot_paths[r_index])
            o_path = get_robot_positions_based_on_commands(default_paths[i], all_robot_paths[i])
            # print(r_path)
            # print(o_path)
            r_path.pop(delay_i)

            if paths_free_of_collision(r_path, o_path) == False:
                # print("CONFLICT AMONG ROBOTS ", r_index, " and ", i)
                # print(r_path)
                # print(o_path)
                return False

    # path is free of collision with all robots
    return True


def perform_rotations_before_hold(r_i, r_path, robot_paths, default_paths):
    """
        Function accepts full robot path, and optimizes it, by trading 1 rotational command for 1 wait (hold) command,
        in case they are sequential.
    """
    # print("---------------------------------")
    # print("OPTIMIZATION PROCESS")
    # print("Robot path: ", r_path)
    pop_elements = 0
    for i in range(len(r_path)-1):
        if r_path[i] == "Hold" and ( r_path[i+1] == "L" or r_path[i+1] == "R"):
            pop_elements += 1
            j = i

            while( j >= 0 and r_path[j] == "Hold"):
                #keep swapping these two items
                r_path[j], r_path[j+1] = r_path[j+1], r_path[j]
                j -= 1
    # print("Optimized robot path: ", r_path)

    ######### FIX REQUIRED >>> DOUBLE ROTATIONS REMOVAL R, R, Hold, Hold

    ### I BELIEVE FIX HAS BEEN APPLIED
    for i in range(len(r_path)-3):
        if (r_path[i] == "L" or r_path[i] == "R") and (r_path[i+1] == "L" or r_path[i+1] == "R") and \
                r_path[i + 2] == "Hold" and r_path[i + 3] == "Hold":
            r_path[i+1], r_path[i+2] = r_path[i+2], r_path[i+1]

    ###### SHOULD ONLY OPERATE ON PATHS LONGER THEN DEFAULT

    # if len(r_path) <= len(default_r_path):
    #     return r_path


    """
    print(r_path)
    ############# FIX - IMPORT DEFAULT PATH DELAYS - the non-removable
    # print("**************************** DEFAULT PATH DELAYS *********************** ")
    default_p = default_paths[r_i]
    cmd_path_pos = get_robot_positions_based_on_commands(default_paths[r_i], r_path)
    # print("DEFAULT PATH: ", default_p)
    # print("CMD PATH: ", cmd_path_pos)
    path_len = len(cmd_path_pos)

    def_i = 0
    cmd_i = 0

    print("============= COMMAND PATH && POSITIONS ==============")
    print(cmd_path_pos)
    print(default_p)
    print(r_path)


    while cmd_i < path_len - 1 and def_i < len(default_p) - 1:
        ## search for line-up
        if cmd_path_pos[cmd_i] == default_p[def_i]:
            ## check for any delays
            # print("MATCH FOUND")
            ## default delay found
            if default_p[def_i] == default_p[def_i+1]:

                print("DEFAULT DELAY FOUND")
                print("cmd_i ", cmd_i, " def_i ", def_i)

                delay_i = cmd_i +1
                while ( r_path[delay_i] == "Hold" or r_path[delay_i] == "L" or r_path[delay_i] == "R" ) and r_path[delay_i+1] == "Hold":
                    delay_i += 1
                print("rpath-delay_i: ", r_path[delay_i])
                r_path[delay_i] = "Hold-S"

            def_i += 1

        cmd_i += 1

    # print("**************************** DEFAULT PATH DELAYS END *********************** ")




    """
    
    """
        APPLY ADDIONAL CHECK-UPS- new removals od "Hold"
        +
        simultaneous removals    
    """


    # return r_path


    #### ROTATION MERGE

    # optimization_required = 1
    # while optimization_required:


    # print("**************************** MERGE L/R AND DELAY *********************** ")
    # print(r_path)
    # print(get_robot_positions_based_on_commands(default_paths[r_i], r_path))

    ########## FIX REQUIRED
    ### CHECK FROM END FORTH


    # for i in range(len(r_path)-pop_elements-1):
    #     if ( r_path[i] == "L" or r_path[i] == "R") and r_path[i+1] == "Hold" :
    #         r_path.pop(i+1)

    ## begin at last element
    # print("ROBOOT PATHS ")
    # print(robot_paths)


    # print(" VALIDATE ADDITIONAL REMOVALS ")
    i = len(r_path) -1


    opt_made = False

    while i > 0:
        if (r_path[i-1] == "L" or r_path[i-1] == "R") and r_path[i] == "Hold":
            ###validate removal

            if validate_merge_of_rotation_and_delay(r_i, i, robot_paths, default_paths):
                # print("CONFLICT FREE")
                # print(r_i, " ~ @ ", i, " === ", r_path)
                r_path.pop(i)
                opt_made = True
            else:
                # print("CONFLICT DETECTED")
                return r_path, opt_made

        i -= 1


    return r_path, opt_made

def optimize_final_rotations(robot_paths, default_robot_paths):

    robot_paths_opt = robot_paths[:]
    default_paths = default_robot_paths[:]

    # print(" OPTIMIZE REMOVAL OF FIRST HOLD ")
    ### DUE TO ADDITIONAL FIRST HOLD OPERATION - VALIDATE REMOVAL OF HOLD
    # for i, p in enumerate(robot_paths):
    #     if p[0] == "Hold" and validate_merge_of_rotation_and_delay(i, 0, robot_paths, default_paths):
    #         p.pop(0)

    # print(" OPTIMIZE REMOVAL OF HOLD_ROTATION")
    optimize = True
    while optimize:
        optimize = False
        for i, p in enumerate(robot_paths_opt):
            robot_paths_opt[i], opt = perform_rotations_before_hold(i, p, robot_paths_opt, default_paths)
            if opt:
                optimize = True

    # print(" OPTIMIZE REMOVAL OF FIRST HOLD ")
    ### DUE TO ADDITIONAL FIRST HOLD OPERATION - VALIDATE REMOVAL OF HOLD
    # for i, p in enumerate(robot_paths):
    #     if p[0] == "Hold" and validate_merge_of_rotation_and_delay(i, 0, robot_paths, default_paths):
    #         p.pop(0)



    return robot_paths_opt

def robot_path_to_state(robot_path):
    """
        Function accepts full robot path, and transforms it into aseba state path.
        Move - > State 1
        Turn Left -> State 2
        Turn Right -> State 3
        Wait - > State 4
    """

    for i, j in enumerate(robot_path):
        if j == "Move":
            robot_path[i] = 1
        elif j == "L":
            robot_path[i] = 2
        elif j == "R":
            robot_path[i] = 3
        elif j == "Hold":
            robot_path[i] = 4
        elif j == "Hold-S":
            robot_path[i] = 4
        else:
            robot_path[i] = 99

    return robot_path

def states_and_default_path_to_final_path(robot_states, def_robot_path):
    final_path = [def_robot_path[0]]

    step = 0
    length = len(def_robot_path)
    while step < length-1 :
        if def_robot_path[step] == def_robot_path[step+1]:
            length -= 1
            step -= 1
            def_robot_path.pop(step+1)

        step += 1

    step = 0
    # print(robot_states)
    for s in robot_states:
        # print(s)
        if s == 1:
            step += 1
            final_path.append(def_robot_path[step])
        elif s == 2 or s == 3 or 4:
            final_path.append(def_robot_path[step])
        else:
            final_path.append("ERROR")

    return final_path

#############
##### MAIN
#############

print(" ========== TRANSFORM INTO PAIRS OF PATH AND ORIENTATIONS ========== ")

# path_plus_orientation = get_theoretical_path_with_orientations(all_robot_paths)

print("MAX - ALL SINGLE: ", sum(map(len, all_robot_paths)))
path_plus_orientation = get_theoretical_path_with_orientations(all_robot_paths)

for [path, orient] in path_plus_orientation:
    print(path)
    print(orient)
    print("===============================================")

print("====================  REAL WORLD PATHS ===========================")
real_world_paths = theoretical_paths_to_real_world_theoretical_paths(path_plus_orientation)
for i in real_world_paths:
    print(i)

# print("====================  FIXED ORIENTATIONS FROM REAL WORLD PATHS ===========================")
#
#
# real_world_paths_fixed_orient = get_theoretical_path_with_orientations(real_world_paths)
# for [path, orient] in real_world_paths_fixed_orient:
#     print(path)
#     print(orient)
#     print("===============================================")
#
#
# print("REAL WORLD PATHS")
# print(real_world_paths)




# print("====================  REAL WORLD PATHS WITH ORIENTATIONS ===========================")
# real_world_paths_with_orientations = get_theoretical_path_with_orientations(real_world_paths)
# for i in real_world_paths_with_orientations:
#     print(i)

print("====================  REAL WORLD THEORETICAL PATHS ===========================")


robot_paths = []
for i in real_world_paths:
    ### MIND TO REMOVE THE INITAL HOLD OPERATION ( ONLY SERVES AS THE INITAL ORIENTATION GUIDE
    robot_paths.append(theoretical_path_to_robot_path(i)[1:])

for i in robot_paths:
    print(i)


# print("ROBOT PATH=======================================")
# print(robot_paths)

print("====================  OPTIMIZED PATH ROTATIONS ===========================")

robot_paths_with_optimized_rotations = optimize_final_rotations(robot_paths, initial_robot_paths)

for i, p in enumerate(robot_paths_with_optimized_rotations):
    print(p)
    print(get_robot_positions_based_on_commands(initial_robot_paths[i], p))

print("====================  ASEBA PATH COMMANDS ===========================")
robot_aseba_paths = []
for i in robot_paths_with_optimized_rotations:
    robot_aseba_paths.append(robot_path_to_state(i))

for i in robot_aseba_paths:
    print(i)

print("MAX LEN ASEBA: ", len(max(robot_aseba_paths, key=len)))

print("====================  FINAL FIELDS PATHS ===========================")
robot_final_field_paths = []
for i,j in enumerate(robot_aseba_paths):
    robot_final_field_paths.append(states_and_default_path_to_final_path(j,initial_robot_paths[i]))

for i in robot_final_field_paths:
    print(i)

print(" VS OPTIMIZED: ", sum(map(len, robot_aseba_paths)) )
"""
    TO DO:

        - implement check validation, to repeat switch rotation process for as long as changes appear

"""