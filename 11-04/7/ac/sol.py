from collections import namedtuple
Activity = namedtuple('Activity', ['name', 'excitement', 'cost'])

def convert(s):
    # Convert s from XXXXXXX.YY to XXXXXXXYY 
    return int(s.replace('.', ''))

def recurse(final_excitement, max_excitement, total_cost, all_activities, planned_activities, current_excitement, current_cost, answers):

    if current_excitement == final_excitement and current_cost <= total_cost:
        answers.append(list(planned_activities))

    for activity in all_activities:
        new_excitement = current_excitement + activity.excitement
        new_cost = current_cost + activity.cost
        if new_excitement <= max_excitement and new_cost <= total_cost:
            recurse(final_excitement, max_excitement, total_cost, all_activities, planned_activities + [activity.name], new_excitement, new_cost, answers)


def main():
    cases = int(input())
    for case in range(1, cases + 1):
        num_activities, final_excitement, max_excitement, total_cost = map(convert, input().split())

        activities = []
        for _ in range(num_activities):
            name, excitement, cost = input().split()
            excitement, cost = convert(excitement), convert(cost)
            activities.append(Activity(name, excitement, cost))

        print(activities)
        print('CASE: {}'.format(case))
        results = []
        recurse(final_excitement, max_excitement, total_cost, activities, [], 0, 0, results)

        results.sort(key = lambda x: ''.join(x))
        results.sort(key = lambda x: len(x))

        if results:
            for result in results:
                print(' -> '.join(result))
        else:
            print('IMPOSSIBLE')

        print()

main()
