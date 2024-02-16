## General informations

- **Scenario manager** need *dialog* node to running `roslaunch dialog websocket.launch`
- **Smart table** have to run on system that has a sensor connected to it
- **Smart table** need to have access to proper USB port to work `sudo chmod 777 /dev/ttyUSB0` (or other USB number, depends on configuration)
- **Smart table** is turned on by default right now but signal to turn it on manually might be usefull `rostopic pub /table/sgn_on std_msgs/Bool "data: true"`


## Setup virtual environment

Go to repository folder
```
source ./setup.sh
```

### Inteligent table node
```
python3 ./smart_table.py
```

### Scenario node
```
python3 ./scenario_manager.py
```

## Rico docking
<details>
  <summary>Undock robot</summary>
  
```
rostopic pub /undocker_server/goal laser_servoing_msgs/UndockActionGoal "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: ''
goal_id:
  stamp:
    secs: 0
    nsecs: 0
  id: ''
goal: {}"
```
</details>

<details>
  <summary>Dock robot</summary>
  
```
rostopic pub /go_and_dock/goal dock_charge_sm_msgs/GoAndDockActionGoal "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: ''
goal_id:
  stamp:
    secs: 0
    nsecs: 0
  id: ''
goal:
  retry_delay:
    secs: 0
    nsecs: 0
  use_current_pose: true"
```
</details>
