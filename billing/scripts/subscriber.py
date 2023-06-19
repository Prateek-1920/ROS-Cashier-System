#!/usr/bin/env python3
import rospy
from billing.msg import custom_bill
from billing.srv import update

# Default inventory and initial income
rospy.set_param("/inventory", 100)
rospy.set_param("/income", 0)


def bill_callback(data):
    quantity = data.Quantity
    total = data.Total

    rospy.wait_for_service('update_params')

    update_params = rospy.ServiceProxy('update_params', update)
    response = update_params(quantity, total)
    if response.status:
        rospy.loginfo("Parameters updated Successfully.")
    else:
        rospy.loginfo("Failed to update parameters.")


def update_param(request):
    inventory = rospy.get_param("/inventory")
    income = rospy.get_param("/income")

    rospy.set_param("/inventory", inventory-request.Quantity)
    rospy.set_param("/income", income+request.Total)
    return ("Updated")


def subscribe_to_bill_topic():
    rospy.init_node('subscriber_node', anonymous=True)
    rospy.Subscriber('bill_topic', custom_bill, bill_callback)
    rospy.Service('update_params', update, update_param)

    rospy.spin()


if __name__ == '__main__':

    print("###### SUBSCRIBER ######")
    try:
        subscribe_to_bill_topic()
    except rospy.ROSInterruptException:
        pass
