# 🤖 ROS 2 Workspace Template

This is a reusable ROS 2 workspace template designed for scalable
robotics development using:

-   ROS 2 (ament_python)
-   colcon build system
-   Launch-based execution
-   Docker support (optional)


# 📁 Workspace Structure

```bash
ws/
├── src/ # All ROS 2 packages go here
│ └── my_package/ # Example package
├── build/ # Generated (DO NOT EDIT)
├── install/ # Generated (DO NOT EDIT)
├── log/ # Build logs
├── docker/ # Docker setup (optional)
└── README.md
```

# 📦 ROS 2 Package Structure

Each Python ROS 2 package follows this layout:

```bash
my_package/
├── my_package/ # Python module (nodes live here)
│ ├── **init**.py
│ └── my_node.py
├── launch/ 
│ └── my_node.launch.py #Launch files
├── resource/ 
│ └── my_package
├── test/ # Lint and tests
├── package.xml
├── setup.py
└── setup.cfg
```

# 🚀 Build & Run

## Build workspace
```bash
colcon build --symlink-install
```
## Source environment
```bash
source install/setup.bash
```
## Run a node directly
```bash
ros2 run my_package my_node
```
## Run via launch file (recommended)
```bash
ros2 launch my_package my_node.launch.py
```


# 🧠 How to create a new package

## 1. Create package
```bash
cd src ros2 pkg create my_new_package --build-type ament_python
```


## 2. Rename package references

package.xml: `<name>`{=html}my_new_package`</name>`{=html}

setup.py: ```package_name = 'my_new_package'```

```python
entry_points = { 'console_scripts':
                 [ 'my_node = my_new_package.my_node:main', ],
               }
```


## 3. Folder rename
```bash
mv src/my_package src/my_new_package mv src/my_new_package/my_package
src/my_new_package/my_new_package
```


## 4. resource rename
```bash
mv resource/my_package resource/my_new_package
```

# 🤖 How to add a new node

Create: ```my_new_package/my_new_package/another_node.py```

Add to setup.py: ```'another_node = my_new_package.another_node:main'```

Rebuild: ```colcon build --symlink-install source install/setup.bash```

Run: ```ros2 run my_new_package another_node```



# ⚠️ Important ROS 2 Rules

Always source: ```source install/setup.bash```

Rebuild after changes: ```colcon build --symlink-install```

Launch files must be installed via setup.py: ```(os.path.join('share',
package_name, 'launch'), glob('launch/\*.py'))```



# 🧱 Design Philosophy

-   scalable multi-package systems
-   Docker-friendly robotics projects
-   clean ROS / logic separation
-   launch-driven execution
