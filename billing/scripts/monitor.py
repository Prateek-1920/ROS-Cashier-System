import rospy
from billing.msg import custom_bill


def bill_callback(data):
    inventory = rospy.get_param('/inventory')
    income = rospy.get_param('/income')
    rospy.loginfo(data)
    rospy.loginfo("Inventory: %d", inventory)
    rospy.loginfo("Income: %d /-", income)


def display():
    rospy.init_node('monitor_node', anonymous=True)
    rospy.Subscriber('bill_topic', custom_bill, bill_callback)

    rospy.spin()


if __name__ == '__main__':

    print("###### MONITOR ######")

    try:
        display()
    except rospy.ROSInterruptException:
        pass
