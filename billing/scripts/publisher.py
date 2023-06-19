#!/usr/bin/env python3
import rospy
from billing.msg import custom_bill


def publish_bill():
    rospy.init_node('publisher_node', anonymous=True)
    pub = rospy.Publisher('bill_topic', custom_bill, queue_size=10)
    rate = rospy.Rate(10)

    billnumber = 1  # First bill number

    while not rospy.is_shutdown():

        quantity = int(input("Enter number of products: "))
        price = int(input("Enter price of the profuct: "))

        # Create a new Bill message
        bill_msg = custom_bill()
        bill_msg.bill_number = billnumber
        billnumber = billnumber + 1
        bill_msg.timestamp = rospy.Time.now()
        bill_msg.Quantity = quantity
        bill_msg.Price = price
        bill_msg.Total = quantity*price

        pub.publish(bill_msg)

        rate.sleep()


if __name__ == '__main__':

    print("###### PUBLISHER ######")
    try:
        publish_bill()
    except rospy.ROSInterruptException:
        pass
