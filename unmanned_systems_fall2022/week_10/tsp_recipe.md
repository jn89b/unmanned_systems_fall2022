# TSP example
```
cost_list = []
for loop to go through each permuation:
    - cost = 0
    - for loop to go each individual wp 
        - current cost = compute distance(wp_curr, wp_next) 
        - cost = cost + current_cost 
    - cost_list.append(cost)

min_index = find_min_index(cost_list)
best_solution = list(permuations[min_index])
```

