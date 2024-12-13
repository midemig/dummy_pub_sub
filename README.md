# dummy_pub_sub

This package contains dummy publisher and subscriber nodes for testing purposes. The dummy publishers publish messages of specified types (`Image` or `Odometry`) at a given frequency to specified topics. The dummy subscribers subscribe to these topics and receive the messages, but they do not process the data.

Additionally, the package includes delayed publishers and subscribers. Delayed publishers start publishing messages after a specified delay, while delayed subscribers start subscribing to topics after a specified delay.

To modify the parameters of the launch file to create your own scenario, you can edit the `pub_params`, `sub_params`, `delay_sub_params`, and `delay_pub_params` lists in the `generate_launch_description` function in the `launch` file. Each list contains parameters for the nodes:

- `pub_params`: `[frequency, topic_name, message_type]`
- `sub_params`: `[topic_name, message_type]`
- `delay_sub_params`: `[topic_name, message_type, delay (s)]`
- `delay_pub_params`: `[frequency, topic_name, message_type, delay (s)]`

By adjusting these parameters, you can customize the topics, message types, frequencies, and delays to fit your testing needs.