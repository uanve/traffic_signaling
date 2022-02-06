## Different traffic light programs
#### if an intersection has 1 street -> traffic light always green
#### otherwise:
- basic: each street is green for 1 second respectively
- queue_weight: green light assign depending on the queue at each street (Random choice with probability proportional to the queue)


|   | score   | N_cars_arrived | N_cars_total | running time |
|---|---------|----------------|--------------|--------------|
| a | 1001    | 1              | 2            | 0.003        |
| a | 1002    | 1              | 2            | 0.002        |
| b | 4565642 | 1000           | 1000         | 43.480       |
| b | 4569004 | 1000           | 1000         | 48.863       |
| c | 2116578 | 983            | 1000         | 89.879       |
| c | 2206151 | 999            | 1000         | 75.978       |
| d | 968685  | 690            | 1000         | 1181.658     |
| d | 2135987 | 973            | 1000         | 22.087       |
| e | 1044297 | 765            | 1000         | 0.654        |
| e | 1196914 | 891            | 1000         | 0.676        |
| f | 589737  | 268            | 1000         | 25.549       |
| f | 2136626 | 974            | 1000         | 23.210       |

# Results - basic traffic light
|   | score   | N_cars_arrived | N_cars_total | running time |
|---|---------|----------------|--------------|--------------|
| a | 1001    | 1              | 2            | 0.003        |
| b | 4565642 | 1000           | 1000         | 43.480       |
| c | 2116578 | 983            | 1000         | 89.879       |
| d | 968685  | 690            | 1000         | 1181.658     |
| e | 1044297 | 765            | 1000         | 0.654        |
| f | 589737  | 268            | 1000         | 25.549       |

# Results - dynamic traffic light
|   | score   | N_cars_arrived | N_cars_total | running time |
|---|---------|----------------|--------------|--------------|
| a | 1002    | 1              | 2            | 0.002        |
| b | 4569004 | 1000           | 1000         | 48.863       |
| c | 2206151 | 999            | 1000         | 75.978       |
| d | 2135987 | 973            | 1000         | 22.087       |
| e | 1196914 | 891            | 1000         | 0.676        |
| f | 2136626 | 974            | 1000         | 23.210       |


<table>
<tr><th>basic traffic light</th><th>dynamic traffic light</th></tr>
<tr><td>


|   | score   | arrived | total | running time |
|---|---------|----------------|--------------|--------------|
| a | 1001    | 1              | 2            | 0.003        |
| b | 4565642 | 1000           | 1000         | 43.480       |
| c | 2116578 | 983            | 1000         | 89.879       |
| d | 968685  | 690            | 1000         | 1181.658     |
| e | 1044297 | 765            | 1000         | 0.654        |
| f | 589737  | 268            | 1000         | 25.549       |

</td><td>


|   | score   | arrived | total | running time |
|---|---------|----------------|--------------|--------------|
| a | 1002    | 1              | 2            | 0.002        |
| b | 4569004 | 1000           | 1000         | 48.863       |
| c | 2206151 | 999            | 1000         | 75.978       |
| d | 2135987 | 973            | 1000         | 22.087       |
| e | 1196914 | 891            | 1000         | 0.676        |
| f | 2136626 | 974            | 1000         | 23.210       |

</td></tr> </table>
