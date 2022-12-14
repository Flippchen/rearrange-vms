'Find the best VM distribution for each host'
from ortools.linear_solver import pywraplp


def extract_data(filename):
    with open(filename, 'r') as file:
        names = []
        capacities = []
        for line in file:
            stripped_line = line.strip()
            values = stripped_line.split(",")
            names.append(values[0])
            capacities.append(values[1])
        del names[0]
        del capacities[0]
        capacities = [int(x) for x in capacities]
    return names, capacities


def rearrange_vms(filename, number_of_hosts, host_capacity, desired_load):
    names = []
    weights = []
    result = {}
    names, weights = extract_data(filename)
    try:
        number_of_hosts = int(number_of_hosts)
        host_capacity = int(host_capacity)
        desired_load = int(desired_load)
        if desired_load > 100 or desired_load < 0 or host_capacity <= 0 or number_of_hosts <= 0:
            result["status"] = "Invalid input"
            return result
    except ValueError:
        print("Invalid input")
        result["status"] = "Invalid input"
        return result
    # Capacities of the hosts
    # Length of this list is the number of hosts
    desired_load = desired_load / 100
    capacities_unedited = [host_capacity] * number_of_hosts
    capacities = [int(x * desired_load) for x in capacities_unedited]

    data = {'weights': weights, 'names': names}
    assert len(data['weights']) == len(data['names'])
    data['num_items'] = len(data['weights'])
    data['all_items'] = range(data['num_items'])

    data['bin_capacities'] = capacities
    data['num_bins'] = len(data['bin_capacities'])
    data['all_bins'] = range(data['num_bins'])

    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if solver is None:
        print('SCIP solver unavailable.')
        return

    # x[i, b] = 1 if VM i is put in Host b.
    x = {}
    for i in data['all_items']:
        for b in data['all_bins']:
            x[i, b] = solver.BoolVar(f'x_{i}_{b}')

    # Constraints.
    # Each VM only goes into one host.
    for i in data['all_items']:
        solver.Add(sum(x[i, b] for b in data['all_bins']) <= 1)

    # The amount put in one Host cannot exceed its capacity.
    for b in data['all_bins']:
        solver.Add(
            sum(x[i, b] * data['weights'][i]
                for i in data['all_items']) <= data['bin_capacities'][b])

    # Objective.
    # Maximize total value of packed items.
    objective = solver.Objective()
    for i in data['all_items']:
        for b in data['all_bins']:
            objective.SetCoefficient(x[i, b], data['weights'][i])
    objective.SetMaximization()

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        total_weight = 0
        assigned_vms = 0
        for b in data['all_bins']:
            host_result = {}
            bin_weight = 0
            for i in data['all_items']:
                if x[i, b].solution_value() > 0:
                    host_result[f"{data['names'][i]}"] = data['weights'][i]
                    bin_weight += data['weights'][i]
                    assigned_vms += 1
            host_result["ram_consumption"] = f"{bin_weight}/{str(capacities[b])} Gb"
            host_result["utilization"] = f"{round(bin_weight / host_capacity * 100, 2)} %"
            host_result["capacity"] = f"{data['bin_capacities'][b]} Gb"
            result[f"{b}"] = host_result
            total_weight += bin_weight
        result["total_ram_consumption"] = f"{total_weight} Gb"
        if not assigned_vms == len(data['names']):
            result["status"] = "Not all VMs have been assigned to a host"
            result["assigned_vms"] = assigned_vms
            return result
        else:
            result["status"] = f"All {assigned_vms} VMs have been assigned to a host"
            print(result)
            return result
    else:
        print('Unsolvable problem.')
        result = {"status": "Unsolvable problem."}
        return result
