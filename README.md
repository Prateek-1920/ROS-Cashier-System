## APPROACH UNDERTAKEN
* Three nodes are made, publisher node that publishes input from the user, subscriber node that processes the input and updates the inventory, and finally the monitor node that displays the output.
* A ROS parameter server is used to store maintain the inventory and income.
* A ROS service is used to update these parameters. A service call is made from the subscriber node to update the inventory and income parameters with received bill information.

## ROS TOPICS LIST
```
/bill_topic
/rosout
/rosout_agg
```

## YOUTUBE VIDEO LINK
https://youtu.be/8u2SUzZYLSc
