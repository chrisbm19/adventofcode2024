def main():
    # declare variables
    reports = []
    safe_count = 0

    # load reports into list
    with open("puzzle_input.txt", "r", encoding=None) as input:
        for line in input:
            reports.append(line)

    # convert reports to ints
    for s in range(len(reports)):
        reports[s] = list(map(int, reports[s].split()))
    
    # iterate over reports, evaluating each level for safe vs unsafe
    for report in reports:
        inc = all(x < y for x, y in zip(report, report[1:])) # checks to see if strictly increasing
        dec = all(x > y for x, y in zip(report, report[1:])) # checks to see if strictly decreasing
        diff = all(abs(x-y) > 0 and abs(x-y) < 4 for x, y in zip(report, report[1:])) # checks to see if difference is in acceptable range
        if (inc or dec) and diff:
            safe_count += 1
        else:
            # test the report for safety if each value is removed
            for l in range(len(report)):
                temp = report.copy()
                temp.pop(l)
                inc = all(x < y for x, y in zip(temp, temp[1:])) # checks to see if strictly increasing
                dec = all(x > y for x, y in zip(temp, temp[1:])) # checks to see if strictly decreasing
                diff = all(abs(x-y) > 0 and abs(x-y) < 4 for x, y in zip(temp, temp[1:])) # checks to see if difference is in acceptable range
                if (inc or dec) and diff:
                    safe_count += 1
                    break

    # print safe count
    print(f"Safe Count: {safe_count}")
    return

main()