import json
import math
import sys
import os


def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def find_nearest_agent(warehouse_location, agents):
    nearest_agent = None
    shortest_distance = float("inf")

    for agent_id, agent_location in agents.items():

        distance = calculate_distance(
            agent_location,
            warehouse_location
        )

        if distance < shortest_distance:
            shortest_distance = distance
            nearest_agent = agent_id

    return nearest_agent, shortest_distance


# -----------------------------------------
# GET INPUT FILE FROM COMMAND
# -----------------------------------------

if len(sys.argv) != 2:
    print("Usage:")
    print("python main.py .\\test_cases\\test1.json")
    sys.exit(1)


input_file = sys.argv[1]


# -----------------------------------------
# READ THE SELECTED TEST CASE
# -----------------------------------------

try:
    with open(input_file, "r") as file:
        data = json.load(file)

except FileNotFoundError:
    print(f"ERROR: File not found: {input_file}")
    sys.exit(1)

except json.JSONDecodeError:
    print(f"ERROR: Invalid JSON: {input_file}")
    sys.exit(1)


# -----------------------------------------
# GET DATA
# -----------------------------------------

warehouses = data["warehouses"]
agents = data["agents"]
packages = data["packages"]


# -----------------------------------------
# PROCESS PACKAGES
# -----------------------------------------

agent_totals = {
    agent_id: 0.0
    for agent_id in agents
}

package_results = []


for package in packages:

    package_id = package["id"]

    warehouse_id = package["warehouse"]

    destination = package["destination"]

    warehouse_location = warehouses[warehouse_id]


    # Find nearest agent to warehouse
    assigned_agent, agent_to_warehouse_distance = (
        find_nearest_agent(
            warehouse_location,
            agents
        )
    )


    # Warehouse to destination
    warehouse_to_destination_distance = calculate_distance(
        warehouse_location,
        destination
    )


    # Total distance for package
    total_distance = (
        agent_to_warehouse_distance
        + warehouse_to_destination_distance
    )


    # Add to agent total
    agent_totals[assigned_agent] += total_distance


    # Save package result
    package_results.append({
        "package_id": package_id,
        "warehouse": warehouse_id,
        "assigned_agent": assigned_agent,
        "agent_to_warehouse_distance": round(
            agent_to_warehouse_distance,
            2
        ),
        "warehouse_to_destination_distance": round(
            warehouse_to_destination_distance,
            2
        ),
        "total_distance": round(
            total_distance,
            2
        )
    })


# -----------------------------------------
# MOST EFFICIENT AGENT
# -----------------------------------------

most_efficient_agent = min(
    agent_totals,
    key=agent_totals.get
)


# -----------------------------------------
# CREATE REPORT
# -----------------------------------------

report = {
    "packages": package_results,

    "agent_totals": {
        agent_id: round(distance, 2)
        for agent_id, distance in agent_totals.items()
    },

    "most_efficient_agent": most_efficient_agent
}


# -----------------------------------------
# REPORT FILE NAME
# -----------------------------------------

test_name = os.path.splitext(
    os.path.basename(input_file)
)[0]

report_file = f"report_{test_name}.json"


# -----------------------------------------
# SAVE REPORT
# -----------------------------------------

with open(report_file, "w") as file:
    json.dump(
        report,
        file,
        indent=4
    )


# -----------------------------------------
# DISPLAY RESULT
# -----------------------------------------

print("Mystery Delivery System")
print("=" * 60)

print()
print(f"Input file: {input_file}")
print(f"Packages processed: {len(packages)}")

print()
print("Agent Total Distances:")

for agent_id, distance in report["agent_totals"].items():
    print(f"{agent_id} → {distance}")

print()
print(
    f"Most Efficient Agent: {most_efficient_agent}"
)

print()
print(
    f"Report created successfully: {report_file}"
)

print("=" * 60)