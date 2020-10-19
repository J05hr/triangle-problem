

def triangle(filename):
    try:
        # open the file in read mode
        fle = open(filename, "r")

        # keep track of the results
        sums = []

        # loop through the lines
        for lne in fle:
            # strip newline
            line = lne.strip()
            # get an array of nodes for each line
            nds = line.split(" ")
            # map to ints
            nodes = list(map(int, nds))
            # loop through the array indexes and add to sums, traverse right to left
            for nidx in reversed(range(len(nodes))):

                # if we are at the right side insert a new sum or add the root node
                if nidx == len(nodes) - 1:
                    # check for previous parents, if none than add root node, else add the sum from the last line idx-1
                    if nidx == 0:
                        sums.insert(nidx, nodes[nidx])
                    else:
                        sums.insert(nidx, nodes[nidx] + sums[nidx - 1])

                # if we are at the left side add to the existing sum
                elif nidx == 0:
                    sums[nidx] += nodes[nidx]

                # if we are in the middle check both parents and add the max sum
                else:
                    sums[nidx] = max(sums[nidx] + nodes[nidx], sums[nidx-1] + nodes[nidx])

        return max(sums)

    except Exception as e:
        print("failed to open or read the file")
        print(e)
        return -1


if __name__ == '__main__':
    fnm = "triangle.txt"
    print("The max sum of the triangle is: %d" % triangle(fnm))