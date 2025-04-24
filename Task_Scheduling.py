def max_tasks(tasks):
    # Sort tasks by deadline (earliest first)
    sorted_tasks = sorted(tasks, key=lambda x: x['deadline'])
    
    current_time = 0
    completed = []
    
    for task in sorted_tasks:
        if current_time + task['duration'] <= task['deadline']:
            completed.append(task['name'])
            current_time += task['duration']
    
    return completed

# Example usage
tasks = [
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 1, 'duration': 2},
]

result = max_tasks(tasks)
print("Maximum tasks that can be completed:", result)
print("Number of tasks:", len(result))