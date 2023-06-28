from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="sick_safetyscanners2",
            executable="sick_safetyscanners2_node",
            name="sick_safetyscanners2_node",
            output="screen",
            emulate_tty=True,
            parameters=[
                {"frame_id": "scan",
                 "sensor_ip": "192.168.0.2",
                 "host_ip": "192.168.0.1",
                 "interface_ip": "0.0.0.0",
                 "host_udp_port": 0,
                 "channel": 0,
                 "channel_enabled": True,
                 "skip": 0,
                 "angle_start": 0.0,
                 "angle_end": 0.0,
                 "time_offset": 0.0,
                 "general_system_state": True,
                 "derived_settings": True,
                 "measurement_data": True,
                 "intrusion_data": True,
                 "application_io_data": True,
                 "use_persistent_config": False,
                 "min_intensities": 0.0,
                 "lidar_name": "front"}
            ]
        )
    ])
