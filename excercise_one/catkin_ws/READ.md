
**Robotignite ACADEMY**

In this Quiz, you will create a code to make the robot avoid the wall that is in front of him. To help you achieve this, let's divide the project down into smaller units:<br />

Create a Publisher that writes into the /cmd_vel topic in order to move the robot.<br />
Create a Subscriber that reads from the /kobuki/laser/scan topic. This is the topic where the laser publishes its data.<br />
Depending on the readings you receive from the laser's topic, you'll have to change the data you're sending to the /cmd_vel topic, in order to avoid the wall. This means, use the values of the laser to decide.<br />

**HINT 1**: The data that is published into the /kobuki/laser/scan topic has a large structure. For this project, you just have to pay attention to the 'ranges' array.<br />

**HINT 2**: The 'ranges' array has a lot of values. The ones that are in the middle of the array represent the distances that the laser is detecting right in front of him. This means that the values in the middle of the array will be the ones that detect the wall. So in order to avoid the wall, you just have to read these values.<br />
**HINT 3**: The laser has a range of 30m. When you get readings of values around 30, it means that the laser isn't detecting anything. If you get a value that is under 30, this will mean that the laser is detecting some kind of obstacle in that direction (the wall).<br />
**HINT 4**: The scope of the laser is about 180 degrees from right to left. This means that the values at the beginning and at the end of the 'ranges' array will be the ones related to the readings on the sides of the laser (left and right), while the values in the middle of the array will be the ones related to the front of the laser.<br />
